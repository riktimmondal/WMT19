w_set=set()
with open("vocab.hi") as f:
    with open("vocab.char.hi", "w") as f1:
        for line in f:
            words=list(line.strip().split('\t'))
            f1.write(words[0]+'\n') 
