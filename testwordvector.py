import json
from sentences import Sentences
from words import Words
from wordvector import WordVector

dlist = []
xlist = []
ylist = []
xdict = {}
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
            ylist.append((j, vect[dlist.index(i)][count - 1]))

print("tf-idf\n", ylist)


def main():
    # search tf-idf of word
    inp = input("word: ")
    countw = 0
    flag = 0
    for i in vectsent2:
        for j in i:
            countw += 1
            if j == inp and flag == 0:
                print("{}:{}".format(j, vect2[vectsent2.index(i)][countw -1]))
                flag = 1
            if countw * len(vect2) == len(vectbow2):
                print("not in documents")

while True:
    main()
