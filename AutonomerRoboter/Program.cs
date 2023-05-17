using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

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
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            Comms.BefehlGeben("", "", "");
        }
    }
}
