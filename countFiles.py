#!/usr/bin/env python

import os

def countFiles(path):
	total=0
	for subdir, dir, files in os.walk(path):
		for file in files:
			total += 1
	return (total)

from sys import stdout,stdin,argv


total = countFiles(argv[1])
stdout.write('Total files: %d\n' % total)	
