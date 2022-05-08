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
xdict["bow"] = vectbow
xdict["sentok"] = dlist

# dump json
json.dump(xdict, open("data.json", "w"))

# load json
d = json.load(open("data.json"))
print("load json: \n", d)

vect2 = d["vector"]
vectbow2 = d["bow"]
vectsent2 = d["sentok"]

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


def main():
    # search tf-idf of word
    inp = input("word: ")
    countw = 0
    flag = 0
    for i in vectsent2:
        if flag == 0:
            for j in i:
                countw += 1
                if j == inp:
                    print("{}:{}".format(j, vect2[vectsent2.index(i)][countw -1]))
                    flag = 1
                    break
        if countw == len(vectbow2):
            print("the word does not exist in the documents")

while True:
    main()
