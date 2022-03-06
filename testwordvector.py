from sentences import Sentences
import wordvector

xlist = []
outdict = {}

with open("data.txt", "r") as file:
    for line in file:
        if not line:
            continue
        else:
            xlist.append(line)
        varstring = " ".join(xlist)

# tokenise to sentences(sometime need make tokenize sentences only dot give argument dot = 1)
s = Sentences(varstring)
sl = s.load()

# vector with tf-idf
vect = wordvector.vector(xlist, tfidf = "tfidf")

# vectors words
vectwords = wordvector.linetokenize()
#print("vectors words\n", vectwords)

for i in vect:
    for j in i:
        if j != 0:
            try:
                outdict[vectwords[vect.index(i)][i.index(j)]] = j
            except IndexError:
                pass
sv = sorted(outdict.values())
wsv = {}
for i in sv:
    for j in outdict.keys():
        if outdict[j] == i:
            wsv[j] = outdict[j]
            break
print("tf-idf\n", wsv)