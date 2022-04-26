import json
from sentences import Sentences
from words import Words
from wordvector import WordVector

dlist = []
xlist = []
ylist = []
dict = {}

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

# vector with tf-idf
ivect = WordVector(dlist, tfidf = "tf-idf")
vect = ivect.load()

# bag of words
vectbow = ivect.bow()

dict["vector"] = vect
dict["bow"] = vectbow
dict["sentok"] = dlist

# dump json
json.dump(dict, open("data.json", "w"))

# load json
d = json.load(open("data.json"))
print("load json: \n", d)

vect2 = d["vector"]
vectbow2 = d["bow"]
vectsent2 = d["sentok"]

# search tf-idf of word
inp = input("word: ")
for i in vectsent2:
    countw = 0
    for j in i:
        countw += 1
        if j == inp:
            print("{}:{}".format(j, vect2[vectsent2.index(i)][countw -1]))

# tf-idf of words without 0
for i in dlist:
    for j in i:
        if vect[dlist.index(i)][i.index(j)] != 0:
            ylist.append((j, vect[dlist.index(i)][i.index(j)]))

print("tf-idf\n", ylist)
