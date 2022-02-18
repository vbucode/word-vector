# module to count vector
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
    if tfidf == "tf":
        for i in range(len(nlist)):
            klist.append([0]*len(instv))
        for k in instv:
            c = instv.count(k)
            for i in nlist:
                for j in i:
                    if k == j:
                        klist[nlist.index(i)][instv.index(k)] = c / len(instv)
                        c = 0

    elif tfidf == "idf":
        for i in range(len(nlist)):
            klist.append([0]*len(instv))
        for k in instv:
            for i in nlist:
                for j in i:
                    if k == j:
                        klist[nlist.index(i)][instv.index(k)] = math.log10(len(nlist)/sum([1.0 for i in nlist if k in i]))

    elif tfidf == "tfidf":
        for i in range(len(nlist)):
            klist.append([0]*len(instv))
        for k in instv:
            c = instv.count(k)
            for i in nlist:
                for j in i:
                    if k == j:
                        vartf = c / len(instv)
                        varidf = math.log10(len(nlist)/sum([1.0 for i in nlist if k in i]))
                        klist[nlist.index(i)][instv.index(k)] = vartf * varidf
                        c = 0
        
    elif tfidf == 0:
        for i in range(len(nlist)):
            klist.append([0]*len(instv))
        for k in instv:
            for i in nlist:
                for j in i:
                    if k == j:
                        klist[nlist.index(i)][instv.index(k)] = 1

    return klist
