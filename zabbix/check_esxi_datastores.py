#!/usr/bin/python

# Check ESXi datastores: return status, write FS autodetect JSON

from pysphere import VIServer, VIProperty
import sys

def main(argv=None):

    if argv is None:
    argv = sys.argv

    server = VIServer()
    server.connect(sys.argv[1], sys.argv[2], sys.argv[3])

    print "{"
    print "\t\"data\":[\n"
    first = 1

    for ds_mor, name in server.get_datastores().items():
        props = VIProperty(server, ds_mor)
    if not first:
        sys.stdout.write(",")
    first = 0

    pfree = float(props.summary.freeSpace) / float(props.summary.capacity) * 100

    print "\n\t{"
        print "\t\t\"{#DSNAME}\":\"%s\"," % name
        print "\t\t\"{#DSACCESS}\":\"%d\"," % props.summary.accessible
        print "\t\t\"{#DSCAP}\":\"%s\"," % props.summary.capacity
        print "\t\t\"{#DSFREE}\":\"%s\"," % props.summary.freeSpace
        print "\t\t\"{#DSPFREE}\":\"%s\"" % pfree
        sys.stdout.write("\t}") 

    print "\n\t]"
    print "}"

    server.disconnect()


if __name__ == '__main__':
    sys.exit(main())
