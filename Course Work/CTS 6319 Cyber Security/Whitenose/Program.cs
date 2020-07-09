using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Whitenose
{

    class Program
    {
     
        static void Main(string[] args)
        {

            ///------------------------------------------------------->
            /// Software Design Description: 
            /// Whitenose.API.cs - REST WebService for querying local JSON DB
            /// Whitenose.Reader.cs - WinPCAP/SharpPcap file reader
            /// Whitenose.Manager.cs - Settings & Helper functions
            /// Whitenose.Probe.cs - Identifies probe events from packet flows
            /// Whitenose.Storage.cs - R/W local JSON DB of probe event objs.
            /// Whitenose.Enriched.cs - Additional feature datastreams
            ///------------------------------------------------------->
            var mgr = new Manager();
            mgr.GetConfig();

            ///------------------------------------------------------->
            ///Start thread to host a Web Service REST API
            ///------------------------------------------------------->
            Task api = Task.Run(() =>
            {

                System.Threading.Thread.CurrentThread.Name = "API";
                Console.WriteLine("Starting Web API");
                API.LaunchServer(mgr.settings.WebAPI_URI);
            });


            ///------------------------------------------------------->
            ///Start thread to dump found probe events to local file
            ///------------------------------------------------------->
            Task storage = Task.Run(() =>
            {
                Console.WriteLine("Starting Local Storage thread");
                Storage.StartRecording(mgr.settings.StorageFile);
            });


            ///------------------------------------------------------->
            ///Start thread to analyze packets for probe events
            ///------------------------------------------------------->
            Task probe = Task.Run(() =>
            {
                Console.WriteLine("Starting Packet Analyzer");
                try
                {
                    while (true)
                    {
                        Probe.StartAnalyzer();
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                }
            });


            ///------------------------------------------------------->
            ///Start thread to collect enrichment data for probe events
            ///------------------------------------------------------->
            Task enrich = Task.Run(() =>
            {
                Console.WriteLine("Starting Enrichment");
                try
                {
                    while (true)
                    {
                        Enriched.GeoLocator.StartCapture(mgr.settings.GeoDataFile);
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                }
            });



            ///------------------------------------------------------->
            ///Start thread to read packets from device (pcapfile)
            ///------------------------------------------------------->

            //read all pcaps from folder and split into 
            //seperate tasks for each pcap file in folder.
            //var groupsOfFiles = Manager.GetGroupOfFiles(mgr.settings.PcapFolder);
            var pcapFiles = Manager.GetAllFiles(mgr.settings.PcapFolder);
            var readerTasks = new List<Task>();
            foreach (var file in pcapFiles)
            {
                var device = new SharpPcap.LibPcap.CaptureFileReaderDevice(file);
                if (!Reader.DeviceStats.TryAdd(device.Name, new Reader.FileStatistics()
                {
                    fileSize = device.FileSize,
                    fileName = device.FileName,
                    fileBytesRead = 0,
                    packetsRead = 0,
                    status = "pending",
                    startCaptureTime = "NA"

                }))
                {
                    Console.WriteLine("Could Not add Device stats for  {0}", device.FileName);
                }

                var t = new Task(() =>
                {
                    var r_running = Reader.DeviceStats.Values.Where(x => x.status == "running").Count();
                    if (r_running > 50)
                    {
                        //wait until the running tasks are completed
                        System.Threading.Thread.Sleep(10000);
                    }
                    else
                    {
                        Reader.StartCapture(file);
                    }
                });
                readerTasks.Add(t);
            }

            readerTasks.ForEach(t => t.Start());

            Console.WriteLine("Started {0} Read Packet Tasks", readerTasks.Count);



          



            try
            {
                Task.WaitAll(new Task[] { api ,probe,storage});
              
            }
            catch (AggregateException ae)
            {
                Console.WriteLine("One or more exceptions occurred:");
                foreach (var ex in ae.InnerExceptions)
                    Console.WriteLine(" {0}: {1}", ex.GetType().Name, ex.Message);
            }
            
        }
        
        
    }

 
}
