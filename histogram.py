# create a histogram from an input
import sys
import string

words = open(input()).read().split()
d = dict()
for word in words:
    t = word.translate(str.maketrans('', '', string.punctuation)).upper()
    if (len(t) > 0):
        d[t] = d.get(t, 0) + 1

# create a list so we can sort it
l = list()
for key, value in d.items():
    l.append((value, key))
l = sorted(l, reverse=True)

for v, k in l:
    print("{:10}".format(k), end="")
    percent = v/len(words) * 100
    #print(v)
    stars = percent
    print("[", sep="", end="")
    while stars >= 0:
        print("*", end="")
        stars -= 5
    print("]", end=" ")
    print(f"{round(percent, 2)}%")

# get total number of words
#numWords = len(words)
#print(numWords)


