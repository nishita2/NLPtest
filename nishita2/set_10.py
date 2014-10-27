#coding: UTF-8

file = open('col2.txt','r')
txt = file.readlines()
token = set(txt)
dict = {}

for str in token:
    dict[str] = txt.count(str)
print dict
for k, v in sorted(dict.items(), key=lambda x:x[1]):
    print k
