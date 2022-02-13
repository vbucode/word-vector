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
        for j in nlist:
            for k in j:
                for i, x in enumerate(instv):
                    c = 0
                    if x != k:
                        klist.append(0)
                    else:
                        c += 1
                        klist.append(c / len(instv))
    else:
        for i in range(len(nlist)):
            klist.append([0]*len(instv))
        for k in instv:
            for i in nlist:
                for j in i:
                    if k == j:
                        klist[nlist.index(i)][instv.index(k)] = 1
    return klist
