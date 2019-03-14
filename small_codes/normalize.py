from __future__ import unicode_literals
import unicodedata

import codecs
import re
import sys
#f1=codecs.open('gujen.nor.en','w','utf-8')
f=open("KDE4.en","r")
f1=open("KDE4.nor.en","w")    
"""with codecs.open('gujen.en', encoding='utf-8') as f:
  input=f.read().split("\n");
  for line in input:
    line = line.strip()
    line = unicodedata.normalize('NFC', line.encode('utf-8'))
    line = line.replace(u"«", u"“").replace(u"»", u"”")
    line = line.encode('utf8').sub(r'(^|[^S\w])#([A-Za-z0-9_]+)', '\\1｟#\\2｠')
    f1.write(line)
    f1.write("\n")"""


input=f.read().split("\n");
for line in input:
  #line = unicode(text,"utf-8")
  line = line.strip()
  line = unicodedata.normalize('NFC', line)
  line = line.replace(u"«", u"“").replace(u"»", u"”")
  line = re.sub(r'(^|[^S\w])#([A-Za-z0-9_]+)', '\\1｟#\\2｠',line)
  f1.write(line)
  f1.write("\n")	