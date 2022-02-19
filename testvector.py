from sentences import Sentences
from words import Words
from punctuation import Punctuation
from lemmatize import Lemmatize
import corpus
import vector

xlist = []

# to awoid some problems with not good writting text
# для избежания возможной ошибки при неправильном форматировании данных
with open("data.txt", "r") as file:
    for row in file:
        if not row:
            continue
        else:
            xlist.append(row)
        varstring = " ".join(xlist)

# tokenise to sentences
s = Sentences(varstring)
sl = s.load()
print("Sentences\n", sl)

# vector with tf-idf
vect = vector.vector(sl, tfidf = "tfidf")

# vectors words
vectwords = vector.linetokenize()
print("vectors words\n", vectwords)

# max
for i in vect:
    for j in i:
        if j == max(i):
            try:
                print("out: ", vectwords[vect.index(i)][i.index(j)], j)
            except IndexError:
                pass
        else:
            continue

