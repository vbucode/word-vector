import math

class WordVector:
    def __init__(self, getlist, lcustomlist = None, rcustomlist = None, tfidf = "01"):
        self.getlist = getlist
        self.lcustomlist = lcustomlist
        self.rcustomlist = rcustomlist
        self.tfidf = tfidf
    def load(self):
        klist = []
        instv = []
        c = 0
        countw = 0
        for i in self.getlist:
            for j in i:
                instv.append(j)

        if self.tfidf == "tf":
            for i in self.getlist:
                tlist = []
                tlist2 = []
                if countw != 0:
                    tlist.append([0] * countw)
                for j in i:
                    countw += 1
                    c = instv.count(j)
                    tlist.append(c / len(instv))
                tlist.append([0] * (len(instv) - countw))
                for i in tlist:
                    tlist2.extend(i)
                klist.append(tlist2)

        elif self.tfidf == "idf":
            for i in self.getlist:
                tlist = []
                tlist2 = []
                if countw != 0:
                    tlist.append([0] * countw)
                for j in i:
                    countw += 1
                    tlist.append(math.log10(len(self.getlist)/sum([1.0 for i in self.getlist if j in i])))
                tlist.append([0] * (len(instv) - countw))
                for i in tlist:
                    tlist2.extend(i)
                klist.append(tlist2)

        elif self.tfidf == "tf-idf":
            for i in self.getlist:
                tlist = []
                tlist2 = []
                if countw != 0:
                    tlist.append([0] * countw)
                for j in i:
                    countw += 1
                    c = instv.count(j)
                    vartf = c / len(instv)
                    varidf = math.log10(len(self.getlist)/sum([1.0 for i in self.getlist if j in i]))
                    klist.append(vartf * varidf)
                tlist.append([0] * (len(instv) - countw))
                for i in tlist:
                    tlist2.extend(i)
                klist.append(tlist2)

        elif self.tfidf == "01":
            for i in self.getlist:
                tlist = []
                tlist2 = []
                if countw != 0:
                    tlist.append([0] * countw)
                for j in i:
                    countw += 1
                    tlist.append([1])
                tlist.append([0] * (len(instv) - countw))
                for i in tlist:
                    tlist2.extend(i)
                klist.append(tlist2)


        elif self.tfidf == "custom":
            for i in self.getlist:
                tlist = []
                tlist2 = []
                if countw != 0:
                    tlist.append([0] * countw)
                for j in i:
                    countw += 1
                    c = 0
                    for k in self.lcustomlist:
                        c += 1
                        if k == j:
                            klist.append(self.rcustomlist[self.lcustomlist.index(k)])
                            break
                    if c == len(self.lcustomlist):
                        klist.append(1)
                tlist.append([0] * (len(instv) - countw))
                for i in tlist:
                    tlist2.extend(i)
                klist.append(tlist2)
            for i in self.getlist:
                for j in i:
                    countw += 1
                    c = 0
                    for k in self.lcustomlist:
                        c += 1
                        if k == j:
                            klist[self.getlist.index(i)][countw - 1] = self.rcustomlist[self.lcustomlist.index(k)]
                            break
                    if c == len(self.lcustomlist):
                        klist[self.getlist.index(i)][countw - 1] = 1
        
        return klist
