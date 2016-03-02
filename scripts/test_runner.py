#!/usr/bin/env python

import os
import sys
import subprocess

test_dir = os.path.abspath(sys.argv[1])
test_executable = sys.argv[2]
stamp_path = os.path.abspath(sys.argv[3])
os.chdir(test_dir)
try:
  subprocess.check_call([test_executable])
  with open(stamp_path, 'a'):
    os.utime(stamp_path, None)
except:
  print("Problem running tests")
