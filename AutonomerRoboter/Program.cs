﻿using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Sql;
using System.Data.SqlClient;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.IO;

namespace AutonomerRoboter
{
    public class Comms
    {
        public static void BefehlGeben(string Ziel, string Arg1, string Arg2)
        {
            System.Diagnostics.Process.Start("https://" + Ziel + "/<name.py>?" + Arg1 + "=" + Arg2);

            var BrowserProcess = Process.GetProcesses().
            Where(pr => pr.ProcessName == "msedge"); // without '.exe'

            foreach (var process in BrowserProcess)
            {
                process.Kill();
            }
        }
        
        public DataTable WegAbfrage(string Start, string Ziel)
        {
            using(SqlConnection conn = new SqlConnection("Server=In21DB;Database=AutonomerRoboter;User Id=Admin;Password=Admin;"))
            {
                conn.Open();
                string query = "exec Wegfindung " + Start +" " + Ziel;
                SqlCommand cmd = new SqlCommand(query, conn);

                DataTable dt = new DataTable();
                dt.Load(cmd.ExecuteReader());
                conn.Close();
                return dt;
            }
        }

        public static string Lokale_HTTP_Request()
        {
            string html = string.Empty;
            string url = @"http://localhost/test";

            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            request.AutomaticDecompression = DecompressionMethods.GZip;

            using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())
            using (Stream stream = response.GetResponseStream())
            using (StreamReader reader = new StreamReader(stream))
            {
                html = reader.ReadToEnd();
            }
            return html;
        }
       
    }
    internal class Program
    {
        static void Main(string[] args)
        {
        }
    }
}
