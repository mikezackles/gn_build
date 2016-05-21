#!/usr/bin/env python

import sys

with open(sys.argv[1], 'w') as outfile:
    with open(sys.argv[2], 'r') as infile:
        outfile.write('namespace {0} {{\n'.format(sys.argv[3]))
        outfile.write('char const* {0} =\n'.format(sys.argv[4]))
        outfile.write('R"SHADER(\n')
        outfile.write(infile.read())
        outfile.write('\n)SHADER"\n')
        outfile.write('}')
