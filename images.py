#!/bin/env python3

import os, requests

exts = ['png', 'jpg', 'gif', 'svg']

sess = requests.Session()

for base in [ 'https://schoolofbitcoin.com/', 'https://schoolofbitcoin.com/what-is-money/', 'https://schoolofbitcoin.com/what-is-bitcoin/', 'https://schoolofbitcoin.com/your-first-bitcoin/' ]:
	print(base)
	dir = base.split('/')[3]
	if len(dir) > 0 and not os.access(dir, os.R_OK):
		os.mkdir(dir)
	headers = {'Referer':base, 'Pragma':'no-cache', 'Cache-Control':'no-cache'}
	for i in range(0, 1000):
		found = False
		for ext in exts:
			fn = '%simg%d.%s' % (dir + '/' if len(dir) > 0 else '', i, ext)
			if os.access(fn, os.R_OK):
				found = True
				break
		if found:
			continue
		for ext in exts:
			fn = 'img%d.%s' % (i, ext)
			url = base + 'data/' + fn
			print('trying %s' % url)
			r = sess.get(url, stream=True, headers=headers)
			if r.status_code != 200:
				print('%s %s' % (r.status_code, r.reason))
				continue
			if len(dir) > 0:
				fn = dir + '/' + fn
			print('writing %s' % fn)
			with open(fn, 'wb') as f:
				for chunk in r.iter_content(1024):
					f.write(chunk)
			found = True
			break
		if not found:
			print('%d not found' % i)
			break
