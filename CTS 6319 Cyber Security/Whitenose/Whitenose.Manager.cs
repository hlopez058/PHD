using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;

namespace Whitenose
{
    public class Manager
    {
        public class Settings
        {
            public string WebAPI_URI { get; set; }
            public string PcapFile { get; set; }
            public string StorageFile { get; internal set; }
            public string GeoDataFile { get; internal set; }
            public string PcapFolder { get; internal set; }
        }
        public Settings settings { get; private set; }
        public void GetConfig()
        {
            this.settings = new Settings()
            {
                WebAPI_URI = ConfigurationManager.AppSettings["WebAPI_URI"].ToString(),
                PcapFile = ConfigurationManager.AppSettings["PCAP_FileName"].ToString(),
                PcapFolder = ConfigurationManager.AppSettings["PCAP_Folder"].ToString(),

                StorageFile = ConfigurationManager.AppSettings["Storage_FileName"].ToString(),
                GeoDataFile = ConfigurationManager.AppSettings["GeoData_FileName"].ToString()
            };
            
        }
        public Helper helper { get; }
        public class Helper
        {
        }

        internal static List<List<string>> GetGroupOfFiles(string pcapFolder)
        {
            var listOfFile = System.IO.Directory.GetFiles(pcapFolder);

            //split list of files by 10 
            var take = listOfFile.Length/10;
            if (take < 1)
                take = 1;
            var groups = new List<List<string>>();
           

           for(int i=0; i < listOfFile.Length; i+=take)
            {
                var group = new List<string>();
                for (int j=i; j<i+take; j++)
                {
                    if(j<listOfFile.Length)
                       group.Add(listOfFile[j]);
                }
                groups.Add(group);
            }

            return groups;
        }

        internal static List<string> GetAllFiles(string pcapFolder)
        {
            try
            {
                if (!System.IO.Directory.Exists(pcapFolder))
                    throw new ConfigurationException(pcapFolder + " does not exist");

                return System.IO.Directory.GetFiles(pcapFolder).ToList();
            }catch(Exception ex)
            {
                Console.WriteLine(ex.Message);
                return null;
            }
        }
        
    }

 
}
