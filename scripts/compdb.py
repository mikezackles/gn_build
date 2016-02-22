#!/usr/bin/env python

import sys
from subprocess import call

outpath = sys.argv[2]
with open(outpath, "w") as outfile:
  outdir = sys.argv[1]
  command = ["ninja", "-C", outdir, "-t", "compdb", "cxx"]
  call(command, stdout=outfile)
