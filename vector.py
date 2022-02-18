# module to count vector

from words import Words

def linetokenize():
    global nlist
    instnlist = nlist
    return instnlist

def bow():
    global instv
    instb = instv
    return instb

def vector(getlist, tf = 1):
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
    if tf == 1:
        for i in range(len(nlist)):
            klist.append([0]*len(instv))
        for k in instv:
            c = instv.count(k)
            for i in nlist:
                for j in i:
                    if k == j:
                        klist[nlist.index(i)][instv.index(k)] = c / len(instv)
                        c = 0
    else:
        for i in range(len(nlist)):
            klist.append([0]*len(instv))
        for k in instv:
            for i in nlist:
                for j in i:
                    if k == j:
                        klist[nlist.index(i)][instv.index(k)] = 1
    return klist
