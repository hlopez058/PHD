using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Whitenose
{
    public class Storage
    {
        public static string fileName { get; set; }
        public static int lastWriteCount { get; set; }
        public static int EventsStored { get; set; }
        public static void StartRecording(string fileName = "db.json")
        {
            //set the file to dump data too.
            Storage.fileName = fileName;
            Storage.lastWriteCount = 2;
            while (true)
            {

                Storage.EventsStored = GetStorage().Count();

                System.Threading.Thread.Sleep(5000);
                
                //record probe events to local json file format
                if (Probe.Events.Count() > lastWriteCount)
                {
                    var fileData = Newtonsoft.Json.JsonConvert.SerializeObject(Probe.Events.Values);
                 
                    File.WriteAllText(fileName, fileData);

                    lastWriteCount = Probe.Events.Count() + 2;

                    //-----
                    //Clean up the reader flow 
                    
                    Reader.FlowDictionaryGC();
                    Probe.EventDictionaryGC();
                }
            }
        }
        public static bool StorageAvailable()
        {
            return File.Exists(Storage.fileName);
        }
        public static List<Probe.ProbeEvent> GetStorage()
        {
            try
            {
                if (File.Exists(Storage.fileName)){
                    var fileData = File.ReadAllText(Storage.fileName);
                    return Newtonsoft.Json.JsonConvert.DeserializeObject<List<Probe.ProbeEvent>>(fileData);
                }
                else { throw new FileNotFoundException(); }

            }
            catch(Exception ex)
            {
                Console.WriteLine(ex.Message);
                return new List<Probe.ProbeEvent>();
            }
        }
    }

 
}
