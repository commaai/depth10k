#!/usr/bin/env python3
import os

f = open("index.html", "w")
f.write("<html><body>\n")
for x in sorted(os.listdir("imgs")):
  f.write('<img src="imgs/%s"></img><br/>\n' % x)
  #f.write('<img src="segs/%s"></img><br/>\n' % x)
f.close()

