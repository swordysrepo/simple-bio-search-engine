#!/python3.8/bin
import os

s=set()
f = open("titles.txt")
for word in f.read().split():
    s.add(word)

for a in s:
    if len(a)>4:
        os.system('def ' + a)
