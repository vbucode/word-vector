from sentences import Sentences
from words import Words
from punctuation import Punctuation
from lemmatize import Lemmatize
import corpus
import vector

xlist = []
outdict = {}

with open("data.txt", "r") as file:
    for line in file:
        if not line:
            continue
        else:
            xlist.append(line)
    varstring = " ".join(xlist)

# tokenise to sentences(sometime need make tokenize sentences only dot)
s = Sentences(varstring, dot = 1)
sl = s.load()

# vector with tf-idf
vect = vector.vector(sl, tfidf = "tfidf")

# vectors words
vectwords = vector.linetokenize()

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
print(wsv)
