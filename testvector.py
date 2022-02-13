from sentences import Sentences
from words import Words
from punctuation import Punctuation
import corpus
import vector

llist = []
rlist = []
nlist = []
ylist = []
with open("data.txt", "r") as file:
    for line in file:
        if not line:
            continue
        else:
            left, right, *res = line.split(":")
            llist.append(left)
            rlist.append(right)

"""
for i in llist:
    insth = Words(i)
    w = insth.load()
    nlist.append(w)
for i in nlist:
    stop = corpus.stopwords("russian")
    stopfiltered = [str(x) for x in i if x not in stop]
    ylist.append(stopfiltered)
"""
vect = vector.vector(llist)
print(vect)
