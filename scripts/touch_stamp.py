#!/usr/bin/env python

import sys
import os

stamp_path = os.path.abspath(sys.argv[1])
with open(stamp_path, 'a'):
  os.utime(stamp_path, None)
