#!/usr/bin/python
import sys

if len(sys.argv) != 3:
    print 'usage : <path_to_originFile> \nYou must specify the path to the origin file as the first arg'
    sys.exit(1)


def get_file(filename = sys.argv[1]):
    try:
        lis =list()
        for line in open(filename):
            if line != '\n':
                ldir = line.rstrip()
                lis.append(ldir)

        print lis
        filename2 = sys.argv[2]
        target = open(filename2, 'w')
        try:
            for item in lis:
                target.write("%s\n" % item)
        except Exception as e:
            print (e)

        for i in lis:
            print (i)

    except Exception:
        print "This file doesn't exist or can't be read from"
        sys.exit(1)


read_Seq=get_file()


