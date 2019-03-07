import codecs,string
count = 0
str = ""
lineno = []
linesset = set()
linesset.add("\n")
with codecs.open('train_removed.en', encoding='utf-8') as f:
    input=f.read().split("\n");    
    for lines in input:
    
        count=count+1
        if(lines not in linesset):		
          linesset.add(lines)
          lineno.append(count)

print(lineno)
f1=codecs.open('train192k.gu','w','utf-8')		  
count=0 
k=0
with codecs.open('train_removed.gu', encoding='utf-8') as f:
    input=f.read().split("\n");    
    for lines in input:
       count+=1
       flag=0
       if(k<len(lineno) and count==lineno[k]):
             print("Writing to line ",count,"......\n") 	
             for i in lines:
              f1.write(i)   		 
             f1.write("\n");
             k+=1
       	   
print("Finished removing gujarati\n")		

f3=codecs.open('train192k.en','w','utf-8')		  
count=0 
k=0
with codecs.open('train_removed.en', encoding='utf-8') as f:
    input=f.read().split("\n");    
    for lines in input:
       count+=1
       flag=0
       if(k<len(lineno) and count==lineno[k]):
             print("Writing to line ",count,"......\n") 	
             for i in lines:
              f3.write(i)   		 
             f3.write("\n");
             k+=1
       	   
print("Finished removing english\n")		
