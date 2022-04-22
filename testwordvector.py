from sentences import Sentences
from wordvector import WordVector

outdict = {}

with open("data.txt", "r") as file:
    f = file.read()

instsent = Sentences(f)
sent = instsent.load()

# vector with tf-idf
ivect = WordVector(sent, tfidf = "tfidf")
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
