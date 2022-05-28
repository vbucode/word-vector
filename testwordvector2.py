import json
from sentences import Sentences
from words import Words
from wordvector import WordVector
import corpus

dlist = []
xdict = {}
ydict = {}
vectbow = []

with open("data.txt", "r") as file:
    f = file.read()

ner = corpus.ner()

# tokenize to sentences
instsent = Sentences(f)
sent = instsent.load()

# tokenize sentences to words
for i in sent:
    w = Words(i)
    wl = w.load()
    dlist.append(wl)

# vector
ivect = WordVector(dlist, *ner, tfidf = "custom")
vect = ivect.load()

# words without 0
count = 0
for i in dlist:
    for j in i:
        count += 1
        if isinstance(vect[dlist.index(i)][count - 1], str):
            ydict[j] = vect[dlist.index(i)][count - 1]

listd1 = list(ydict.items())
for i in listd1:
    print(i[0], "-", i[1])
