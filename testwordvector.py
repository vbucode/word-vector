import json
from sentences import Sentences
from words import Words
from wordvector import WordVector

wlist = []
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
    instwords = Words(i)
    iwords = instwords.load()
    wlist.append(iwords)

# vector with tf-idf
ivect = WordVector(wlist, tfidf = "tf-idf")
vect = ivect.load()
dict["vector"] = vect

# bag of words
vectbow = ivect.bow()
dict["bow"] = vectbow

# list with lists of tokenized sentences
vectsent = ivect.senttokenize()
dict["sentok"] = vectsent

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
for i in sent:
    for j, x in enumerate(vect[sent.index(i)]):
        if x != 0:
            ylist.append((vectbow[j], x))

print("tf-idf\n", ylist)
