import math
from words import Words

def linetokenize():
    global nlist
    instnlist = nlist
    return instnlist

def bow():
    global instv
    instb = instv
    return instb

def vector(getlist, tfidf = 0):
    global instv
    global nlist
    klist = []
    nlist = []
    c = 0
    varstring = " ".join(getlist)
    instvect = Words(varstring)
    instv = instvect.load()
    for i in getlist:
        insth = Words(i)
        w = insth.load()
        nlist.append(w)
    for i in range(len(nlist)):
            klist.append([0]*len(instv))
    if tfidf == "tf":
        for i in nlist:
            for j in i:
                c = instv.count(j)
                klist[nlist.index(i)][instv.index(j)] = c / len(instv)

    elif tfidf == "idf":
        for i in nlist:
            for j in i:
                klist[nlist.index(i)][instv.index(j)] = math.log10(len(nlist)/sum([1.0 for i in nlist if j in i]))

    elif tfidf == "tfidf":
        for i in nlist:
            for j in i:
                c = instv.count(j)
                vartf = c / len(instv)
                varidf = math.log10(len(nlist)/sum([1.0 for i in nlist if j in i]))
                klist[nlist.index(i)][instv.index(j)] = vartf * varidf

    elif tfidf == 0:
        for i in nlist:
            for j in i:
                klist[nlist.index(i)][instv.index(j)] = 1

    return klist
