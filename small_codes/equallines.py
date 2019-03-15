import codecs,string
count = 0

f1=codecs.open('eng_mono.tok.en','w','utf-8')
with codecs.open('eng_dataset.en.tok', encoding='utf-8') as f:
    input=f.read().split("\n");    
    for lines in input:
                
        count=count+1
        if(count<3974326):
          print("Writing to line ",count,"......\n")		
          f1.write(lines)
          f1.write("\n");
        
            


       	   
print("Finished completing final data in eng\n")	
