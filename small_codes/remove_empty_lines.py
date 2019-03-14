import codecs,string
f1=codecs.open('dev1.gu','w','utf-8')

with codecs.open('dev.gu', encoding='utf-8') as f:
	input=f.read().split("\n");
	for lines in input:
		if not lines.strip():continue
		f1.write(lines)