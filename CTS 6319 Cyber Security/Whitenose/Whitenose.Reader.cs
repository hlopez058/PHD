
using PacketDotNet;

using SharpPcap;
using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Whitenose
{
    public class Reader
    {
        public static ConcurrentDictionary<long,Flow> Flows = new ConcurrentDictionary<long,Flow>();
        public static int FlowCount { get; set; }
        public static ConcurrentDictionary<string,FileStatistics> DeviceStats = new ConcurrentDictionary<string,FileStatistics>();
       
        public class FileStatistics
        {
            public long fileSize { get; set; }
            public string fileName { get; set; }
            public string startCaptureTime { get; set; }
            public int fileBytesRead { get; set; }
            public int packetsRead { get; set; }
            public double percentComplete
            {
                get
                {
                    try
                    {
                        var perc = ((Convert.ToDouble(this.fileBytesRead) /
                            Convert.ToDouble(this.fileSize))) * 100.0;

                        return perc;
                    }
                    catch
                    {
                        return 0.0;
                    }
                }
            }

            public string status { get; internal set; }
        }
        public static void StartCapture(string pcapFile, int id = 0)
        {
            try
            {
                var device = new SharpPcap.LibPcap.CaptureFileReaderDevice(pcapFile);
                //update the stats for this device
                DeviceStats.TryGetValue(device.Name, out FileStatistics thisFileStats);
                var newFileStats = thisFileStats;
                newFileStats.status = "running";
                newFileStats.startCaptureTime = DateTime.Now.ToLongTimeString();
                DeviceStats.TryUpdate(device.Name, newFileStats, thisFileStats);

                // Register our handler function to the 'packet arrival' event
                device.OnPacketArrival += new PacketArrivalEventHandler(device_OnPacketArrival);
                // Start capture 'All Bytes in File' number of packets
                // This method will return when EOF reached.
                device.Capture(-1);
                Console.WriteLine("EOF-device-{0}", pcapFile);

                //update the stats for this device
                newFileStats.status = "done";
                DeviceStats.TryUpdate(device.Name, newFileStats, thisFileStats);
                

            }
            catch(Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
        public class Flow
        {
            public ConcurrentBag<SniffedPacket> packets = new ConcurrentBag<SniffedPacket>();
            public DateTime lastPacketCapturedTime { get { return this.packets.OrderBy(x => x.posixTime.Date).Select(y => y.posixTime.Date).Last(); } }
            
            //combination key
            public long IPKey { get; set; }
        }
        private static void device_OnPacketArrival(object sender, CaptureEventArgs e)
        {
            try
            {
                //read a new packet and convert into a simpler "sniffed" packet object
                var sniff = ExtractTCPPacket(e);
                var b = sniff.transport.SourceAddress.GetAddressBytes();
                var key = BitConverter.ToInt32(b, 0);

                if (Flows.ContainsKey(key))
                {
                    //update
                    Flows.TryGetValue(key, out Flow oldflow);
                    var newflow = oldflow;
                    newflow.packets.Add(sniff);
                    Flows.TryUpdate(key, newflow, oldflow);
                }
                else
                {
                    //add
                    var flow = new Flow()
                    {
                        IPKey = key,
                        packets = new ConcurrentBag<SniffedPacket>() { sniff }
                    };


                    Flows.TryAdd(key, flow);

                    FlowDictionaryGC();

                    FlowCount++;
                }


                //update the stats for this device
                DeviceStats.TryGetValue(e.Device.Name, out  FileStatistics thisFileStats);
                var newFileStats = thisFileStats;
                newFileStats.fileBytesRead += e.Packet.Data.Count();
                newFileStats.packetsRead += 1;
                DeviceStats.TryUpdate(e.Device.Name,newFileStats,thisFileStats);

                System.Threading.Thread.Sleep(10); // sleep so that the thread has time to read device

            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }

        public static void FlowDictionaryGC()
        {
            var flowCopy = Reader.Flows.ToArray();

            if (flowCopy.Length > 1000)
            {

                try
                {   //remove the flow with the oldest packet data
                    var ordered = flowCopy.OrderBy(x => x.Value.lastPacketCapturedTime);
                    var oldestFlowKeys = ordered.Take(100).Select(k => k.Key);
                    foreach (var f in oldestFlowKeys)
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

        private static SniffedPacket ExtractTCPPacket(CaptureEventArgs e)
        {

            var sniff = new SniffedPacket();
            try
            {
                //Sniff hte Incomming packet
                var packet = PacketDotNet.Packet.ParsePacket(LinkLayers.Ethernet, e.Packet.Data);
                sniff.physical = packet;
                sniff.posixTime = e.Packet.Timeval;
                if (packet is PacketDotNet.EthernetPacket)
                {
                    var eth = ((PacketDotNet.EthernetPacket)packet);
                    sniff.network = eth;
                    var ip = (PacketDotNet.IPPacket)packet.Extract(typeof(PacketDotNet.IPPacket));
                    if (ip != null)
                    {
                        sniff.transport = ip;
                        sniff.sessionID = ip.SourceAddress.ToString() + ":" + ip.DestinationAddress.ToString();
                        if (sniff.transport.Protocol == IPProtocolType.TCP)
                        {
                            var tcp = (PacketDotNet.TcpPacket)packet.Extract(typeof(PacketDotNet.TcpPacket));
                            sniff.application.tcp = tcp;

                        }
                        if (sniff.transport.Protocol == IPProtocolType.UDP)
                        {

                            var udp = (PacketDotNet.UdpPacket)packet.Extract(typeof(PacketDotNet.UdpPacket));
                            sniff.application.udp = udp;
                        }
                        if (sniff.transport.Protocol == IPProtocolType.ICMP)
                        {
                            var icmp = (PacketDotNet.ICMPv4Packet)packet.Extract(typeof(PacketDotNet.ICMPv4Packet));
                            sniff.application.icmp = icmp;
                        }

                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }

            return sniff;
        }
        public static SniffedPacketJSON ToJSON(SniffedPacket p)
        {
            try
            {
                var jPacket = new SniffedPacketJSON();
                
                jPacket.timestamp = p.posixTime.Date.ToUniversalTime().ToString("yyyy'-'MM'-'dd'T'HH':'mm':'ss'.'fff'Z'");
                jPacket.sourceAddress = p.transport.SourceAddress.ToString();
                jPacket.destinationAddress = p.transport.DestinationAddress.ToString();
                jPacket.timeToLive = p.transport.TimeToLive.ToString();
                jPacket.sourceHwAddress = p.network.SourceHwAddress.ToString();
                jPacket.destinationHwAddress = p.network.DestinationHwAddress.ToString();
                jPacket.protocol = p.transport.Protocol.ToString();

                if (p.application.tcp != null) {
                    jPacket.sourcePort = p.application.tcp.SourcePort.ToString();
                    jPacket.destinationPort = p.application.tcp.DestinationPort.ToString();
                    jPacket.sequenceNumber = p.application.tcp.SequenceNumber.ToString();
                    jPacket.allFlags = p.application.tcp.AllFlags.ToString();


                }
                if (p.application.udp != null)
                {
                    jPacket.sourcePort = p.application.udp.SourcePort.ToString();
                    jPacket.destinationPort = p.application.udp.DestinationPort.ToString();
                    jPacket.sequenceNumber = "NA";
                    jPacket.allFlags = "NA";
                }

                jPacket.five_tuple = string.Join(",", jPacket.destinationAddress, jPacket.destinationPort, jPacket.sourceAddress, jPacket.sourcePort, jPacket.protocol);
                return jPacket;
            }catch(Exception ex)
            {

                return null;
            }
        }
        public class SniffedPacket
        {
            public PosixTimeval posixTime;
            public Packet physical { get; set; }
            public PacketDotNet.EthernetPacket network { get; set; }
            public PacketDotNet.IPPacket transport { get; set; }
            public ApplicationLayer application = new ApplicationLayer();
            public string sessionID { get; set; }
          

        }
        [Serializable]
        public class SniffedPacketJSON
        {
            public string timestamp { get; internal set; }
            public string sourceAddress { get; internal set; }
            public string destinationAddress { get; internal set; }
            public string five_tuple { get; set; }
            public string timeToLive { get; internal set; }
            public string sourceHwAddress { get; internal set; }
            public string destinationHwAddress { get; internal set; }
            public string sourcePort { get; internal set; }
            public string destinationPort { get; internal set; }
            public string sequenceNumber { get; internal set; }
            public string allFlags { get; internal set; }
            public string protocol { get; internal set; }
        }
        public class ApplicationLayer
        {
            public PacketDotNet.TcpPacket tcp { get; set; }
            public PacketDotNet.UdpPacket udp { get; set; }
            public ICMPv4Packet icmp { get; internal set; }
        }

    }


}
