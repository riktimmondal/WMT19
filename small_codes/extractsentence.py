import codecs,string
count = 0
str = ""
lineno = []
linenoori = []
linesset = set()
linesset.add("\n")
with codecs.open('train_removed.gu.shuf', encoding='utf-8') as f:
    input=f.read().split("\n");    
    for lines in input:
        lines=lines.split()        
        count=count+1
        if(len(lines) > 8 and len(lineno)<=3000):	         
          lineno.append(count)
        else:
            linenoori.append(count)
            

print(lineno)
f1=codecs.open('testsent.gu','w','utf-8')		  
count=0 
k=0
with codecs.open('train_removed.gu.shuf', encoding='utf-8') as f:
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

f3=codecs.open('testsent.en','w','utf-8')		  
count=0 
k=0
with codecs.open('train_removed.en.shuf', encoding='utf-8') as f:
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

f4=codecs.open('final38k.gu','w','utf-8')
count=0 
k=0
with codecs.open('train_removed.gu.shuf', encoding='utf-8') as f:
    input=f.read().split("\n");    
    for lines in input:
       count+=1
       flag=0
       if(k<len(linenoori) and count==linenoori[k]):
             print("Writing to line ",count,"......\n") 	
             for i in lines:
              f4.write(i)   		 
             f4.write("\n");
             k+=1
       	   
print("Finished completing final data in guj\n")	

f5=codecs.open('final38k.en','w','utf-8')
count=0 
k=0
with codecs.open('train_removed.en.shuf', encoding='utf-8') as f:
    input=f.read().split("\n");    
    for lines in input:
       count+=1
       flag=0
       if(k<len(linenoori) and count==linenoori[k]):
             print("Writing to line ",count,"......\n") 	
             for i in lines:
              f5.write(i)   		 
             f5.write("\n");
             k+=1
       	   
print("Finished completing final data in eng\n")	
