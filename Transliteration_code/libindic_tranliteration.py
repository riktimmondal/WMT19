# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from transliteration import getInstance
import re
#from transliteration import Transliterator
#T=Transliterator
t = getInstance()

filepath='train.gu'
ouput='train.romanised.gu'

with open(filepath) as f:
    with open(ouput, "w") as f1:
        for line in f:
                l=list(line.split())
		#print type(l)
                t_text=''
                for word in l:
			#print type(word)
                        if not re.match(r'^\w+$', word): 
                                text=unicode(word, "utf-8")
				#text=u' '.join((word)).encode('utf-8')
                                w = t.transliterate(text, "en_IN")
                                #t_text=T.transliterate_hi_en(text)
                                #t_text.append(w)
				#print w
				f1.write(w.encode('utf-8'))
                        else:
				#print "hi"
                                f1.write(word)
		f1.write('\n')
                       # print word

                #fwrite(t_text)

#t_text = t.transliterate(text, "ml_IN")
#print t_text





