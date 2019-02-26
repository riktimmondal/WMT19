
w_set=set()
with open("train.en",encoding="utf8") as f:
    with open("vocab_own.en", "w",encoding="utf8") as f1:
        for line in f:
            for word in line:
                if word not in w_set:
                    w_set.add(word)
                    f1.write(word+'\n') 
