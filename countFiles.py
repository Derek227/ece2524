#!/usr/bin/env python

import os
from sys import stdout,stdin,argv

total=0

for subdir, dir, files in os.walk(argv[1]):
	for file in files:
		total += 1

stdout.write('Total files: %d\n' % total)	
