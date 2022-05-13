import json
from sentences import Sentences
from words import Words
from wordvector import WordVector

dlist = []
xdict = {}
ydict = {}
vectbow = []

with open("data.txt", "r") as file:
    f = file.read()

# tokenize to sentences
instsent = Sentences(f)
sent = instsent.load()

# tokenize sentences to words
for i in sent:
    w = Words(i)
    wl = w.load()
    dlist.append(wl)

# bag of words
for i in dlist:
    for j in i:
        vectbow.append(j)

# vector with tf-idf
ivect = WordVector(dlist, tfidf = "tf-idf")
vect = ivect.load()

xdict["vector"] = vect
xdict["sentok"] = dlist

# dump json
json.dump(xdict, open("data.json", "w"))

# tf-idf of words without 0
count = 0
for i in dlist:
    for j in i:
        count += 1
        if vect[dlist.index(i)][count - 1] != 0:
            ydict[j] = vect[dlist.index(i)][count - 1]

listd1 = list(ydict.items())
listd1.sort(key = lambda k: k[1])
for i in listd1:
    print(i[0], "-", i[1])
