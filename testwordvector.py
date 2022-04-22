from sentences import Sentences
from words import Words
from wordvector import WordVector
import corpus

outdict = {}
xlist = []

with open("data.txt", "r") as file:
    f = file.read()

# tokenize to sentences
instsent = Sentences(f)
sent = instsent.load()

# load stop words
stop = corpus.stopwords("russian")

# tokenize sentences before remove stopwords
for i in sent:
    w = Words(i)
    wl = w.load()
    stopfiltered = [str(x) for x in wl if x not in stop]
    varstring = " ".join(stopfiltered)
    xlist.append(varstring)

# vector with tf-idf
ivect = WordVector(xlist, tfidf = "tfidf")
vect = ivect.load()

# vectors words
vectwords = ivect.linetokenize()
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
