#!/usr/bin/python
# -*- encoding: utf-8 -*-
from __future__ import division

import errno
import os
import os.path
import sys
from urlparse import urlparse
import urllib

from bs4 import BeautifulSoup

def fetch_url(url_string):
	url = urlparse(url_string)
	dest_path = "attachments" + url.path
	dest_dir = os.path.dirname(dest_path)

	try:
		os.makedirs(dest_dir)
	except OSError as e:
		if e.errno == errno.EEXIST and os.path.isdir(dest_dir): pass
		else: raise

	print "Fetching %s..." % (url_string,)
	urllib.urlretrieve(url_string, dest_path)

xml_filename = sys.argv[1]
with open(xml_filename, 'r') as f:
	soup = BeautifulSoup(f, "xml")
	for attachment in soup.find_all("attachment_url"):
		fetch_url(attachment.text)
