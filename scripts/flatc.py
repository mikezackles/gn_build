#!/usr/bin/env python

import sys
from subprocess import call

command = ["flatc"] + sys.argv[1:];
call(command)
