import math

class WordVector:
    def __init__(self, getlist, customlist = None, tfidf = "01"):
        self.getlist = getlist
        self.customlist = customlist
        self.tfidf = tfidf
    def load(self):
        klist = []
        instv = []
        c = 0
        countw = 0
        for i in self.getlist:
            if type(i) == list:
                for j in i:
                    instv.append(j)
            else:
                instv.append(i)
        for i in range(len(self.getlist)):
            klist.append([0]*len(instv))
        if self.tfidf == "tf":
            for i in self.getlist:
                for j in i:
                    countw += 1
                    c = instv.count(j)
                    klist[self.getlist.index(i)][countw - 1] = c / len(instv)

        elif self.tfidf == "idf":
            for i in self.getlist:
                for j in i:
                    countw += 1
                    klist[self.getlist.index(i)][countw -1] = math.log10(len(self.getlist)/sum([1.0 for i in self.getlist if j in i]))

        elif self.tfidf == "tf-idf":
            for i in self.getlist:
                for j in i:
                    countw += 1
                    c = instv.count(j)
                    vartf = c / len(instv)
                    varidf = math.log10(len(self.getlist)/sum([1.0 for i in self.getlist if j in i]))
                    klist[self.getlist.index(i)][countw -1] = vartf * varidf

        elif self.tfidf == "01":
            for i in self.getlist:
                for j in i:
                    countw += 1
                    klist[self.getlist.index(i)][countw - 1] = 1

        else self.tfidf == "custom":
            for i in self.getlist:
                for j in i:
                    countw += 1
                    klist[self.getlist.index(i)][countw - 1] = self.customlist[self.getlist.index(i)]
        return klist
