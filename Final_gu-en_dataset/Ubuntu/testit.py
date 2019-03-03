import codecs,string
def detect_language(character):
    maxchar = max(character)
    #print(character)
    if (u'\u0a80' <= maxchar <= u'\u0aff') or (u'\u0020' <= maxchar <= u'\u002e') or (maxchar == u'\u000a') or (maxchar == u'\u003f') or (maxchar == u'\u002e') or (u'\u0030' <= maxchar <= u'\u0039'):
        return 'GUjarati'
    else:	
        return 'unknown'
f1=codecs.open('train_clean.gu','w','utf-8')
count = 0
str = ""
lineno = []
with codecs.open('Ubuntu.nor.tok.gu', encoding='utf-8') as f:
    input=f.read().split("\n");    
    for lines in input:
       count+=1
       for i in lines:
           isEng=detect_language(i)
           if(isEng == "unknown"):
              lineno.append(count)
              break
        


print("No. of found lines",len(lineno),"\n")    
#print(lineno)
count=0 
k=0
with codecs.open('Ubuntu.nor.tok.gu', encoding='utf-8') as f:
    input=f.read().split("\n");    
    for lines in input:
       count+=1
       flag=0
       if((k>=len(lineno)) or (count < lineno[k])):
             print("Writing to line ",count,"......\n") 	
             for i in lines:
              f1.write(i)   		 
             f1.write("\n");
       if(k<len(lineno) and count==lineno[k]):  
          k+=1	   
print("Finished cleaning hindi\n")			 
			 

f3=codecs.open('train_clean.en','w','utf-8')		 
count=0 
k=0
with codecs.open('Ubuntu.nor.tok.en', encoding='utf-8') as f:
    input=f.read().split("\n");    
    for lines in input:
       count+=1
       flag=0
       if((k>=len(lineno)) or (count < lineno[k])):
             print("Writing to line ",count,"......\n") 			 
             for i in lines:
                f3.write(i)			 
             f3.write("\n");
       if(k<len(lineno) and count==lineno[k]):
          k+=1	   
print("Finished cleaning english\n")
