import json
import math

# load json
d = json.load(open("data.json"))

vect2 = d["vector"]
vectbow2 = d["bow"]
vectsent2 = d["sentok"]

# search tf-idf of word
def main():
    inp = input("word: ")
    countw = 0
    flag = 0
    for i in vectsent2:
        if flag == 0:
            for j in i:
                countw += 1
                if j == inp:
                    print("{}:{} all:{}".format(j, vect2[vectsent2.index(i)][countw -1], vectbow2.count(j)))
                    flag = 1
                    break
        if countw == len(vectbow2):
            print("the word does not exist in the documents")

while True:
    main()
