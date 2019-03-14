import codecs,string

f1=codecs.open('dev.gu','w','utf-8')

with codecs.open('test1.sgm', encoding='utf-8') as f:
	input=f.read().split("\n");
	for lines in input:
		flag=0;
		for i in lines:
			if(i=='<'):
				flag=0
			
			if(flag==1):
				f1.write(i)
			
			if(i=='>'):
				flag=1
			
			
		f1.write("\n")