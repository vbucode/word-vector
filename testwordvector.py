import json
from sentences import Sentences
from words import Words
from wordvector import WordVector
import corpus

xlist = []
ylist = []
dict = {}

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
dict["vector"]= vect

# bag of words
vectbow = ivect.bow()
dict["bow"] = vectbow

# list with lists of tokenized sentences
vectsent = ivect.senttokenize()
dict["sentok"] = vectsent

json.dump(dict, open("data.json", "w"))

d = json.load(open("data.json"))
print(d)

vect2 = d["vector"]
vectbow2 = d["bow"]
vectsent2 = d["sentok"]

inp = input("search word: ")
for i in vectsent2:
    for j, x in enumerate(vect2[vectsent2.index(i)]):
        if inp == vectbow2[j] and x != 0:
            print("{}:{}".format(vectbow2[j], x))

for i in vectsent:
    for j, x in enumerate(vect[vectsent.index(i)]):
        if x != 0:
            ylist.append((vectbow[j], x))

print("tf-idf\n", ylist)
