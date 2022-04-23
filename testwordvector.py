from sentences import Sentences
from words import Words
from wordvector import WordVector
import corpus

xlist = []
ylist = []

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

# bag of words
vectbow = ivect.bow()

# list with lists of tokenized sentences
vectsent = ivect.linetokenize()

for i in vectsent:
    for j, x in enumerate(vect[vectsent.index(i)]):
        if x != 0:
            ylist.append((vectbow[j], x))

print("tf-idf\n", ylist)
