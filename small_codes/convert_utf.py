# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#import sys
#if sys.version_info[0] >= 3:
#    unicode = str


filepath='vocab.char.hi'
output='output.hi'

with open(filepath) as f:
	with open(output, "w") as f1:
		for line in f:
			text=unicode(line[0], "utf-8")
			f1.write(text.encode('utf-8')+'\n')