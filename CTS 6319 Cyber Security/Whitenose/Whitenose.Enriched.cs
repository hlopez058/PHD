using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;

namespace Whitenose
{
    public static class Enriched
    {
        public static class GeoLocator
        {
            public static DateTime TimeOfLastAPICall;

            public static GeoData Get(string ip)
            {
                var t = DateTime.Now;
                while(t.Subtract(TimeOfLastAPICall).Seconds < 0.45)
                {
                    //wait before calling the api
                    System.Threading.Thread.Sleep(100);
                }
                var r = new RESTConsumer();
                var resp = r.Get("http://ip-api.com/json/" + ip);
                TimeOfLastAPICall = DateTime.Now;
                return Newtonsoft.Json.JsonConvert.DeserializeObject<GeoData>(resp);
            }

            public class GeoData
            {
               public string status { get; set; }
                public string country { get; set; }
                public string  countryCode { get; set; }
                public string region { get; set; }
                public string regionName { get; set; }
                public string city { get; set; }
                public string zip { get; set; }
                public string lat { get; set; }
                public string lon { get; set; }
                public string timezone { get; set; }
                public string isp { get; set; }
                public string org { get; set; }
                public string As { get; set; }
                public string query { get; set; }
            }

            internal static GeoData GetLocal(string ip,string geodataDBfile = "db.geodata.json")
            {
                var fileData = "";
                if (File.Exists(geodataDBfile))
                {
                    fileData = File.ReadAllText(geodataDBfile);


                    var completedData = Newtonsoft.Json.JsonConvert.DeserializeObject<List<KeyValuePair<string, GeoData>>>(fileData);

                    
                    if (completedData.Where(x=>x.Key == ip).Count()>0)
                    {
                        var geodata = completedData.FirstOrDefault(x => x.Key == ip);

                        return geodata.Value;
                    }
                    else
                    {
                        try
                        {

                            return Get(ip);
                        }
                        catch
                        {
                            return null;
                        }
                    }
                }
                else
                {
                    try
                    {

                        return Get(ip);
                    }
                    catch
                    {
                        return null;
                    }
                }

             }

                internal static void StartCapture(string geodataDBfile = "db.geodata.json")
            {
                while (true)
                {
                    var geodataList = new List<KeyValuePair<string, GeoData>>();
                    var probes = Storage.GetStorage();
                    var attackers = probes.Select(p => p.attacker);

                    var fileData = "";
                    if (File.Exists(geodataDBfile))
                    {
                        fileData = File.ReadAllText(geodataDBfile);


                        var completedData = Newtonsoft.Json.JsonConvert.DeserializeObject<List<KeyValuePair<string, GeoData>>>(fileData);

                        foreach (var attacker in attackers)
                        {
                            if (!completedData.Any(p => p.Key == attacker))
                            {
                                var geodata = Get(attacker);
                                var kvp = new KeyValuePair<string, GeoData>(attacker, geodata);
                                geodataList.Add(kvp);
                            }
                            else
                            {
                                geodataList.Add(completedData.First(x => x.Key == attacker));
                            }
                        }

                    }

                    var data = Newtonsoft.Json.JsonConvert.SerializeObject(geodataList);

                    File.WriteAllText(geodataDBfile, data);

                    System.Threading.Thread.Sleep(10000);
                }

            }
            
        }

        public class RESTConsumer
        {
            public string Get(string uri)
            {
                var request = (System.Net.HttpWebRequest)WebRequest.Create(uri);

                request.Method = "GET";
                
                var response = (HttpWebResponse)request.GetResponse();

                string content = string.Empty;
                using (var stream = response.GetResponseStream())
                {
                    using (var sr = new StreamReader(stream))
                    {
                        content = sr.ReadToEnd();
                    }
                }

                return content;

            }
        }
    }

 
}
