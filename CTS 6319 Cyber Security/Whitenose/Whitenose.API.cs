using System;
using System.Collections.Generic;
using System.Data.Odbc;
using System.Diagnostics;
using System.Linq;
using System.ServiceModel;
using System.ServiceModel.Description;
using System.ServiceModel.Web;

namespace Whitenose
{


    [ServiceContract]
    public interface IAPI
    {
        [OperationContract]
        [WebInvoke(Method = "GET", UriTemplate = "/test", ResponseFormat = WebMessageFormat.Json)]
        string TestMethod();
        

        [OperationContract]
        [WebInvoke(Method = "GET", UriTemplate = "/stats", ResponseFormat = WebMessageFormat.Json)]
        API.Stat GetStats();

        [OperationContract]
        [WebInvoke(Method = "GET", UriTemplate = "/flows?count={count}", ResponseFormat = WebMessageFormat.Json)]
        List<API.FlowStat> GetFlows(string count);

        [OperationContract]
        [WebInvoke(Method = "GET", UriTemplate = "/tasks?status={status}&count={count}", ResponseFormat = WebMessageFormat.Json)]
        Reader.FileStatistics[] GetTasks(string status ="", string count ="10");


        [OperationContract]
        [WebInvoke(Method = "GET", UriTemplate = "/probes?srcIP={srcIP}&dstIP={dstIP}&startTime={startTime}&endTime={endTime}&type={type}&rate={rate}&target={target}&results={results}", ResponseFormat = WebMessageFormat.Json)]
        Probe.ProbeEvent[] GetProbes(string srcIP = null, string dstIP = null, string startTime = null,
            string endTime = null, string type = null, string rate = null,string target =null,string results =null);

    }


    public class API : IAPI
    {

        public static void LaunchServer(string WebAPI_URI)
        {
            ///------------------------------------------------------->
            ///Start an API and publish results of the packet sniffing
            ///------------------------------------------------------->
            //Must run cmd line below to register port:
            //netsh http add urlacl url = http://+:8090/ user=\Everyone
            Console.WriteLine("Admin rights required to register port for API.");
            Process p = new Process();
            p.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            p.StartInfo.FileName = "netsh.exe";
            p.StartInfo.Arguments = @"http add urlacl url = " + WebAPI_URI + @" user=\Everyone";
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.Verb = "runas";
            p.Start();
            //Self-Host WCF
            Uri httpUrl = new Uri(WebAPI_URI);
            var host = new WebServiceHost(typeof(API), httpUrl);
            var binding = new WebHttpBinding(); // NetTcpBinding();
            host.AddServiceEndpoint(typeof(IAPI), binding, "api");
            ServiceDebugBehavior stp = host.Description.Behaviors.Find<ServiceDebugBehavior>();
            stp.HttpHelpPageEnabled = false;
            host.Open();
            Console.WriteLine("API is now hosted on " + WebAPI_URI);
            //keep it open
            Console.ReadKey();
            host.Close();

        }

        /// <summary>
        /// TEST METHOD
        /// </summary>
        /// <returns></returns>
        public string TestMethod()
        {
            var all = Probe.Events.Values.ToList();
            var json = Newtonsoft.Json.JsonConvert.SerializeObject(all,Newtonsoft.Json.Formatting.Indented);
            return json;
        }


       public class EventStats
        {
            public int eventsDetected { get; set; }
            public int eventsRecorded { get; set; }
            public int verticalProbes { get; set; }
            public int horizontalProbes { get; set; }
            public int strobeProbes { get; set; }
        }

        public class Stat
        {
            public string flowsIdentified { get; set; }
            public int packetsRead { get; set; }
            public RunStatus readerTasks { get; set; }
            public string scanCompleted { get; set; }
            public EventStats eventStats = new EventStats();
            public string throughput { get; set; }
        }
        public class RunStatus
        {
            public int running { get; set; }
            public int done { get; set; }
            public int pending { get; set; }
        }
        /// <summary>
        /// Retrieve the stats of the application for monitoring health
        /// </summary>
        /// <returns></returns>
        public Stat GetStats()
        {


            var stats = new Stat();


            stats.flowsIdentified = Reader.FlowCount.ToString();
            
            var r_pending = Reader.DeviceStats.Values.Where(x => x.status == "pending").Count();
            var r_done = Reader.DeviceStats.Values.Where(x => x.status == "done").Count();
            var r_running = Reader.DeviceStats.Values.Where(x => x.status == "running").Count();

            

            stats.readerTasks = new RunStatus
            {
                pending =r_pending,
                done = r_done,
                running = r_running,

            };

            var totalBytesRead = Convert.ToDouble(Reader.DeviceStats.Values.ToList().Select(x => x.fileBytesRead).Sum());
            var totalBytes = Convert.ToDouble(Reader.DeviceStats.Values.ToList().Select(x => x.fileSize).Sum());


            var totalPercentComplete =  ( totalBytesRead/totalBytes)*100.0;

            stats.scanCompleted = string.Format("{0:G3}", totalPercentComplete) + "%";
            stats.packetsRead = Reader.DeviceStats.Values.ToList().Select(x => x.packetsRead).Sum();

            try
            {
                var packetsRead = Convert.ToDouble(stats.packetsRead);
                var timeStarted = Reader.DeviceStats.Values
                                        .OrderBy(x => x.startCaptureTime)
                                        .Select(y => y.startCaptureTime)
                                        .First();

                var timespanStarted = Convert.ToDouble((DateTime.Now - DateTime.Parse(timeStarted)).TotalSeconds);
                stats.throughput = string.Format("{0:G6}", (packetsRead / timespanStarted)) + " packets/sec";

            }
            catch
            {
                Console.WriteLine("API call , stats not ready");
            }

            if (Storage.StorageAvailable())
            {
                var events = Storage.GetStorage();

                stats.eventStats.eventsDetected = events.Count();
                stats.eventStats.eventsRecorded = Storage.EventsStored;
                stats.eventStats.verticalProbes = events.Select(x => x.type).Where(t => t == "vertical").Count();
                stats.eventStats.horizontalProbes = events.Select(x => x.type).Where(t => t == "horizontal").Count();
                stats.eventStats.strobeProbes = events.Select(x => x.type).Where(t => t == "strobe").Count();
            }
            else
            {
                stats.eventStats.eventsDetected = 0;
                stats.eventStats.eventsRecorded = 0;
                stats.eventStats.verticalProbes = 0;
                stats.eventStats.horizontalProbes =0;
                stats.eventStats.strobeProbes = 0;

            }


            return stats;
        }

        public Reader.FileStatistics[] GetTasks(string status = "" , string count = "10")
        {
            var l = new List<Reader.FileStatistics>();
            
            if (status !="")
            {
               l = Reader.DeviceStats.Values.Where(x => x.status == status).ToList();
            }
            else
            {
               l = Reader.DeviceStats.Values.OrderBy(x => x.status).ToList();

            }

            if (int.TryParse(count, out int cnt))
            {
                return l.Take(cnt).ToArray();
            }
            else
            {
                return l.Take(10).ToArray();
            }
        }

        [Serializable]
        public class FlowStat
        {
            public string source_ip;
           
            public Reader.SniffedPacketJSON[] packets;
        }
        public List<FlowStat> GetFlows(string count)
        {
            var t = Reader.Flows.Values;
            var r =  t.Take(int.Parse(count)).ToArray();
            var flowstats = new List<FlowStat>();
            foreach (var flow in r)
            {
                var flowstat = new FlowStat();
                var sPackets = flow.packets.ToList() ;
                var jPackets = new List<Reader.SniffedPacketJSON>();
                foreach(var s  in sPackets)
                {
                    jPackets.Add(Reader.ToJSON(s));
                }

                flowstat.source_ip = jPackets.First().sourceAddress.ToString();
                flowstat.packets = jPackets.ToArray();
                flowstats.Add(flowstat); 
            }

            return flowstats;
        }
        
        public Probe.ProbeEvent[] GetProbes(
            string srcIP = null,
            string dstIP = null,
            string startTime = null,
            string endTime = null,
            string type = null,
            string rate = null,
            string target = null,
            string results = null)
        {


            //var events = Probe.Events.Values;
            var events = Storage.GetStorage();
            //check each query parameter
            if (srcIP != null)
            {
                //pull back query with a particular srcIP
                events = events.Where(x => x.srcIP.Contains(srcIP)).ToList();
            }

            if (dstIP != null)
            {
                //pull  back query with a particular dstIP
                events = events.Where(x => x.dstIP.Contains(srcIP)).ToList();
            }

            if (startTime != null)
            {
                try
                {
                    //get records that are greater than this time
                    events = events
                        .Where(x => Convert.ToDateTime(x.startTime)
                        >= Convert.ToDateTime(startTime))
                        .OrderByDescending(k => k.startTime)
                        .ToList();
                }
                catch
                {
                    return null;
                }
            }

            if (endTime != null)
            {
                try
                {

                    //get records that are less than this time
                    events = events
                         .Where(x => Convert.ToDateTime(x.endTime)
                         >= Convert.ToDateTime(endTime))
                         .OrderByDescending(k => k.endTime)
                         .ToList();
                }
                catch
                {
                    return null;
                }
            }

            if (type != null)
            {
                //get records that are of this type
                //type of probing, horizontal, vertical or strobed
                events = events.Where(x => x.type== type).ToList();
            }
            if (target != null)
            {
                //get records that are of this type
                //type of probing, horizontal, vertical or strobed
                events = events.Where(x => x.target.Contains(target)).ToList();
            }


            if (rate != null)
            {
                try
                {
                    //sort objects by rate
                    events = events
                      .Where(x => float.Parse(x.rate)
                      <= float.Parse(rate))
                      .OrderByDescending(k => float.Parse(k.rate))
                      .ToList();
                }
                catch
                {
                    return null;
                }
            }

            events.OrderBy(k => k.attacker);

            Probe.ProbeEvent[] evts;
            if (results != null)
            {
                //get records that are of this type
                //type of probing, horizontal, vertical or strobed
                 evts = events.Take(Convert.ToInt16(results)).ToArray();

                
            }
            else
            {
                //return in chunks of 10
                evts= events.Take(10).ToArray();
            }

            //update geodata
            List<Probe.ProbeEvent> enriched_evts= new List<Probe.ProbeEvent>();
            foreach (var evt in evts)
            {
                var enr = evt;
                enr.geoData = Enriched.GeoLocator.Get(evt.attacker);
                enriched_evts.Add(enr);
            }
            return enriched_evts.ToArray();

        }

    }
}
