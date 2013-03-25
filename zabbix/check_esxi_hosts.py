#!/usr/bin/python

# Check ESXi hosts resources, return 1 if OK

from pysphere import VIServer, VIProperty
import sys

def main(argv=None):

    if argv is None:
    argv=sys.argv

    server = VIServer()
    try:
        server.connect(sys.argv[1], sys.argv[2], sys.argv[3])

    hosts = server.get_hosts()
        for h_mor, h_name in hosts.items():
            props = VIProperty(server, h_mor)
        try:
            f = open("/tmp/esxi_hosts_" + sys.argv[1] + ".txt", "w")
            try:
            f.write("memorySize=" + str(props.hardware.memorySize) + "\n")
            f.write("overallCpuUsage=" + str(props.summary.quickStats.overallCpuUsage) + "\n")
                    f.write("overallMemoryUsage=" + str(props.summary.quickStats.overallMemoryUsage) + "\n")
            f.write("uptime=" + str(props.summary.quickStats.uptime) + "\n")
                # $CPUTotalMhz = $_.Summary.hardware.CPUMhz * $_.Summary.Hardware.NumCpuCores
                # $row."CpuUsage%" = [math]::round( ($row.CpuUsageMhz / $CPUTotalMhz), 2) * 100
                f.write("cpuMhz=" + str(props.summary.hardware.cpuMhz) + "\n")
                f.write("numCpuCores=" + str(props.summary.hardware.numCpuCores) + "\n")
            finally:
                f.close()
        except IOError:
            print "0"
            sys.exit(0)	
    print "1"
        server.disconnect()
    except Exception, e:
    print "0"

if __name__ == '__main__':
    main()
