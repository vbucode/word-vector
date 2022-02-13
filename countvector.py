# module to count vector

from words import Words

def vector(getlist, tf = 1):
    klist = []
    nlist = []
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
            for i in nlist:
                for j in i:
                    c = 0
                    if k == j:
                        c += 1
                        klist[nlist.index(i)][instv.index(k)] = c / len(instv)
    else:
        for i in range(len(nlist)):
            klist.append([0]*len(instv))
        for k in instv:
            for i in nlist:
                for j in i:
                    if k == j:
                        klist[nlist.index(i)][instv.index(k)] = 1
    return klist
