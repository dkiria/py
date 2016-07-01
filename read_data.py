#!/usr/bin/python
import sys

def read_line_file():
    try:
        lis = list()
        for line in open('cpe_manager_debug_wlan_ap'):
            if line != '\n':
                ldir = line.rstrip()
                lis.append(ldir)

    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except ValueError:
        print "Could not convert data to an integer."
    except:
        print "Unexpected error:", sys.exc_info()[0]
    print lis
    print "\n"


read_line_file()

