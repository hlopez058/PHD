using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using static Whitenose.Reader;

namespace Whitenose
{
    public class Probe
    {
        public class ProbeEvent
        {
            private List<Reader.SniffedPacketJSON> packets = new List<Reader.SniffedPacketJSON>();
            public List<Reader.SniffedPacketJSON> GetPackets()
            {
                return packets;
            }
            public void SetPackets(List<Reader.SniffedPacketJSON> _packets)
            {
                this.packets = _packets;
            }
            public string attacker { get; set; }
            public List<string> srcIP { get; set; }
            public List<string> dstIP { get; set; }
            public List<string> ftuples { get; set; }
            public string type { get; set; }
            public string startTime { get; set; }
            public string endTime { get; set; }
            public string rate { get; set; }
            public string target { get; set; }
            public Enriched.GeoLocator.GeoData geoData { get; set; }
            public void Create(List<SniffedPacket> _packets, string type, string target)
            {
                var packetsJson = new List<SniffedPacketJSON>();
                foreach (var packet in _packets)
                {
                    packetsJson.Add(Reader.ToJSON(packet));
                }
                Create(packetsJson, type, target);
                
            }
            public void Create(List<SniffedPacketJSON> _packetsJson, string type, string target)
            {
                SetPackets(_packetsJson);
                
                this.target = target;

                this.type = type;
                this.srcIP = packets.Select(x => x.sourceAddress).Distinct().Select(p => p.ToString()).ToList();
                this.attacker = this.srcIP[0];
                this.dstIP = packets.Select(x => x.destinationAddress).Distinct().Select(p => p.ToString()).ToList();

                this.ftuples = packets.Select(x => x.five_tuple).Distinct().ToList();

                var firstPacket = packets.OrderBy(p => Convert.ToDateTime(
                    DateTime.ParseExact(p.timestamp, "yyyy'-'MM'-'dd'T'HH':'mm':'ss'.'fff'Z'", CultureInfo.InvariantCulture)))
                    .First();
               

                this.startTime = firstPacket.timestamp;

                var lastPacket =  packets.OrderBy(p => Convert.ToDateTime(
                    DateTime.ParseExact(p.timestamp, "yyyy'-'MM'-'dd'T'HH':'mm':'ss'.'fff'Z'", CultureInfo.InvariantCulture)))
                    .Last();

                this.endTime = lastPacket.timestamp;

                var start = Convert.ToDateTime(
                          DateTime.ParseExact(firstPacket.timestamp,
                            "yyyy'-'MM'-'dd'T'HH':'mm':'ss'.'fff'Z'", CultureInfo.InvariantCulture));

                var end = Convert.ToDateTime(
                          DateTime.ParseExact(lastPacket.timestamp,
                                            "yyyy'-'MM'-'dd'T'HH':'mm':'ss'.'fff'Z'", CultureInfo.InvariantCulture));

                var timeIntervalSec = end.Subtract(start).TotalSeconds;
                double numOfPackets = this.packets.Count;
                this.rate = string.Format("{0:G2}",(numOfPackets / timeIntervalSec)) + " packets/sec";
                
            }

        }

        public static ConcurrentDictionary<long, ProbeEvent> Events = new ConcurrentDictionary<long, ProbeEvent>();

        public static void StartAnalyzer(long flowKey = 0)
        {
            List<long> keyList = new List<long>(Reader.Flows.Keys);
            
            if (flowKey != 0)
            {
                AnalyzeFlow(flowKey);
            }
            else
            {
                foreach (var key in keyList)
                {
                    try
                    {
                        AnalyzeFlow(key);
                     
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine(ex.Message);
                    }
                }


            }
            
        }

        public static void EventDictionaryGC()
        {
            var eventCopy = Probe.Events.ToArray();

            if (eventCopy.Length > 1000)
            {

                try
                {   //remove the flow with the oldest packet data
                    var ordered = eventCopy.OrderBy(x => x.Value.endTime);
                    var oldestEventKeys = ordered.Take(10).Select(k => k.Key);
                    foreach (var f in oldestEventKeys)
                    {
                        Reader.Flows.TryRemove(f, out Reader.Flow remFlow);
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                }
            }
        }
        public static void AnalyzeFlow(long key)
        {
            if (Reader.Flows.ContainsKey(key))
            {
                if (Reader.Flows.TryGetValue(key, out Flow src))
                {
                    var src_packets = src.packets;

                    var pingProbeList = PingScanAnalysis(src, src_packets);

                    var vertProbeList = VerticalAnalysis(src, src_packets);

                    var horzProbeList = HorizontalAnalysis(src, src_packets);

                    var strobeProbeList = StrobeAnalysis(vertProbeList, horzProbeList);

                    var probes = new List<ProbeEvent>();
                    probes.AddRange(pingProbeList);
                    probes.AddRange(vertProbeList);
                    probes.AddRange(horzProbeList);
                    probes.AddRange(strobeProbeList);

                    var filteredProbes = CommonPortAnalysis(probes);

                    foreach (var p in filteredProbes)
                    {
                        if (Events.ContainsKey(key))
                        {
                            //update
                            Probe.Events.TryRemove(key, out ProbeEvent oldProbe);
                            Probe.Events.TryAdd(key, p);
                            //Console.WriteLine("Updated probe event {0}", p.attacker);
                        }
                        else
                        {
                            //add
                            Probe.Events.TryAdd(key, p);
                            Console.WriteLine("Added probe event {0}", p.attacker);
                        }
                    }
                    //Console.WriteLine("Flow analyzed {0}", src.IPKey);
                }
            }
        }

        private static List<ProbeEvent> CommonPortAnalysis(List<ProbeEvent> probes)
        {
            //filter out probes that are of known behaviour


            return probes;
        }

        private static List<ProbeEvent> StrobeAnalysis(List<ProbeEvent> vertProbeList, List<ProbeEvent> horzProbeList)
        {
            //look for probes from same attacker identified as horizontal and vertical
            //use the common probes and combine them into a strobe event probe
            var strobeAttackers = vertProbeList.Select(v => v.attacker)
                .Intersect(horzProbeList.Select(h => h.attacker));
            var strobeProbeList = new List<ProbeEvent>();
            foreach (var attacker in strobeAttackers)
            {
                var vertProbe = vertProbeList.Find(x => x.attacker == attacker);
                var vertProbePackets = vertProbe.GetPackets();
                var horzProbe = horzProbeList.Find(x => x.attacker == attacker);
                var horzProbePackets =horzProbe.GetPackets();
                //add packets to strobe array
                var strobeProbePackets = vertProbePackets;
                strobeProbePackets.AddRange(horzProbePackets);

                //should broadcasted udp packets be considered?
                //if (strobeProbePackets[0].protocol == "UDP") { continue; }
                
                //strobe event
                var p = new ProbeEvent();
                p.Create(strobeProbePackets, "strobe", vertProbe.target + "," + horzProbe.target);
                strobeProbeList.Add(p);
            }

            return strobeProbeList;
        }

        private static List<ProbeEvent> PingScanAnalysis(Flow src, IEnumerable<SniffedPacket> src_packets)
        {

            var ping_ProbeList = new List<ProbeEvent>();
            try
            {
                //analyze each unique src ip found in stream
                //look for tcp probe event as horizontal
                //by grouping by destination ports and counting 
                //how many unique destination addresses there are
                var pings = src_packets.Where(p => p.application.icmp != null);
                if (pings
                    .Select(x => x.transport.DestinationAddress)
                    .Distinct()
                    .Count() > 6)
                {
                    //ping scan since this src has pinged more than 20 distinct computers 
                    var p = new ProbeEvent();
                    p.Create(pings.ToList(), "pingscan", "ICMP");
                    ping_ProbeList.Add(p);

                }
            }
            catch (Exception ex)
            {
                //missing tcp packet in list.. ingore
            }
            return ping_ProbeList;
        }

        private static List<ProbeEvent> HorizontalAnalysis(Flow src, IEnumerable<SniffedPacket> src_packets)
        {

            var horz_ProbeList = new List<ProbeEvent>();
            try
            {
                //analyze each unique src ip found in stream
                //look for tcp probe event as horizontal
                //by grouping by destination ports and counting 
                //how many unique destination addresses there are
 
                var tcp_src = src_packets.Where(p => p.transport.Protocol == PacketDotNet.IPProtocolType.TCP);

                foreach (var s in tcp_src.GroupBy(x => x.application.tcp.DestinationPort))
                {
                    if (s
                        .Select(x => x.transport.DestinationAddress)
                        .Distinct()
                        .Count() >= 10)
                    {
                        //vertical probe event
                        var p = new ProbeEvent();
                        p.Create(s.ToList(), "horizontal", "TCP:" + s.First().application.tcp.DestinationPort.ToString());
                        horz_ProbeList.Add(p);
                    }

                }



                var udp_src = src_packets.Where(p => p.transport.Protocol == PacketDotNet.IPProtocolType.UDP);

                foreach (var s in udp_src.GroupBy(x => x.application.udp.DestinationPort))
                {
                    if (s
                        .Select(x => x.transport.DestinationAddress)
                        .Distinct()
                        .Count() >= 10)
                    {
                        //vertical probe event
                        var p = new ProbeEvent();
                        p.Create(s.ToList(), "horizontal", "UDP:" + s.First().application.udp.DestinationPort.ToString());
                        horz_ProbeList.Add(p);
                    }
                }
            }
            catch (Exception ex)
            {
                //missing tcp packet in list.. ingore
              //  Console.WriteLine("h:" + ex.Message);
            }
            return horz_ProbeList;
        }

        private static List<ProbeEvent> VerticalAnalysis(Flow src, IEnumerable<SniffedPacket> src_packets)
        {

            var vert_ProbeList = new List<ProbeEvent>();
            //analyze each unique src ip found in stream
            //look for tcp probe event as vertical
            //by grouping each destrination address
            //and counting how many unique ports there are
            try
            {

                var tcp_src = src_packets.Where(p => p.transport.Protocol == PacketDotNet.IPProtocolType.TCP);

                foreach (var s in tcp_src.GroupBy(x => x.transport.DestinationAddress))
                {
                    var target = s.First().transport.DestinationAddress.ToString();

                    var ports = s.Select(x => x.application.tcp.DestinationPort);
                    if (ports.Distinct().Count() >= 5)
                    {
                        //vertical probe event tcp
                        var p = new ProbeEvent();
                        p.Create(s.ToList(), "vertical", target + " TCP:" + string.Join(",", ports.Distinct()));
                        vert_ProbeList.Add(p);
                    }

                }


                var udp_src = src_packets.Where(p => p.transport.Protocol == PacketDotNet.IPProtocolType.UDP);

                foreach (var s in udp_src.GroupBy(x => x.transport.DestinationAddress))
                {
                    var target = s.First().transport.DestinationAddress.ToString();

                    var ports = s.Select(x => x.application.udp.DestinationPort);
                    if (ports.Distinct().Count() >= 5)
                    {
                        //vertical probe event tcp
                        var p = new ProbeEvent();
                        p.Create(s.ToList(), "vertical", target + " UDP:" + string.Join(",", ports.Distinct()));
                        vert_ProbeList.Add(p);
                    }

                }
            }
            catch (Exception ex)
            {
               // Console.WriteLine("v:" + ex.Message);
            }
            return vert_ProbeList;
        }
    }

 
}
