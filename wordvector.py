import math

class WordVector:
    def __init__(self, getlist, tfidf = "01"):
        self.getlist = getlist
        self.tfidf = tfidf
    def load(self):
        global instv
        global nlist
        klist = []
        nlist = []
        instv = []
        for i in self.getlist:
            nlist.append(i)
        for i in nlist:
            for j in i:
                instv.append(j)
        for i in range(len(nlist)):
            klist.append([0]*len(instv))
        if self.tfidf == "tf":
            countw = 0
            for i in nlist:
                for j in i:
                    countw += 1
                    c = instv.count(j)
                    klist[nlist.index(i)][countw - 1] = c / len(instv)

        elif self.tfidf == "idf":
            countw = 0
            for i in nlist:
                for j in i:
                    countw += 1
                    klist[nlist.index(i)][countw - 1] = math.log10(len(nlist)/sum([1.0 for i in nlist if j in i]))

        elif self.tfidf == "tf-idf":
            countw = 0
            for i in nlist:
                for j in i:
                    countw += 1
                    c = instv.count(j)
                    vartf = c / len(instv)
                    varidf = math.log10(len(nlist)/sum([1.0 for i in nlist if j in i]))
                    klist[nlist.index(i)][countw - 1] = vartf * varidf

        elif self.tfidf == "01":
            countw = 0
            for i in nlist:
                for j in i:
                    countw += 1
                    klist[nlist.index(i)][countw - 1] = 1
        return klist

    def senttokenize(self):
        global nlist
        instnlist = nlist
        return instnlist
    def bow(self):
        global instv
        instb = instv
        return instb
