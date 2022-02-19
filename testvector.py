from sentences import Sentences
from words import Words
from punctuation import Punctuation
from lemmatize import Lemmatize
import corpus
import vector

xlist = []
outdict = {}

# to awoid some problems with not good writting text
# для избежания возможной ошибки при неправильном форматировании данных
with open("data.txt", "r") as file:
    for line in file:
        if not line:
            continue
        else:
            xlist.append(line)
        varstring = " ".join(xlist)

# tokenise to sentences(sometime need make tokenize sentences only dot)
s = Sentences(varstring, dot = 1)
sl = s.load()
print("Sentences\n", sl)

# vector with tf-idf
vect = vector.vector(sl, tfidf = "tfidf")

# vectors words
vectwords = vector.linetokenize()
print("vectors words\n", vectwords)

for i in vect:
    for j in i:
        if j == max(i):
            try:
                outdict[vectwords[vect.index(i)][i.index(j)]] = j
            except IndexError:
                pass
        elif j == 0:
            pass
        else:
            try:
                outdict[vectwords[vect.index(i)][i.index(j)]] = j
            except IndexError:
                pass

print(outdict)
