#!/usr/bin/env python

import os
import sys
import subprocess

print(sys.argv)
test_executable = os.path.abspath(sys.argv[1])
stamp_path = os.path.abspath(sys.argv[2])
command = [test_executable]
try:
  subprocess.check_call(command)
  with open(stamp_path, 'a'):
    os.utime(stamp_path, None)
except:
  print("Problem running tests")
