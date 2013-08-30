#!/usr/bin/env python
import os
import re
import sys
import time

LAST=3
NEEDLE=''

if sys.argv[1:]:
	arg = sys.argv[1]
	if arg.isdigit():
		LAST=int(arg)
	else:
		NEEDLE=arg

urls = [None]
i = 1
min_time = time.time() - 3600 # 1 hour
for dirpath, dirnames, filenames in os.walk(os.path.join(os.environ['HOME'], '.purple', 'logs')):
	for filename in filenames:
		shown = False
		filepath = os.path.join(dirpath, filename)
		if os.stat(filepath).st_mtime < min_time:
			continue
		found = re.findall(r'https?://\S+', open(filepath).read())
		for url in [u for u in found if NEEDLE in u][-LAST:]:
			if not shown:
				print os.path.basename(os.path.dirname(filepath))
				shown = True
			urls.append(url)
			print '{0}) {1}'.format(i, url)
			i += 1

choice = raw_input('Choice? ')
choice = int(choice)
os.system('chrome {0}'.format(urls[choice]))


