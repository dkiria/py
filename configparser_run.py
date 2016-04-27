#!/usr/bin/python3
import configparser
from configparser import SafeConfigParser
import getopt
import sys

def get_cfg_value(configfile, category, what, strict = 'yes'):
    ret = None
    parser = SafeConfigParser()
    # FIXME make the path configurable
    parser.read(configfile)

    try:
        ret = parser.get(category, what)
    except configparser.NoSectionError:
        print('No section [%s] found in config file. Fix your config file' % category)
        if strict == 'yes':
            exit(1);
    except configparser.NoOptionError:
        print('No option %s= found in config file. Fix your config file' % what)
        if strict == 'yes':
            exit(1);

    return ret
