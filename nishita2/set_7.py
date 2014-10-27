#coding: UTF-8

file = open('sample.txt','r')
txt = file.readlines()
first = []
for row in txt:
    a = row.split('\t')
    first.append(a[0])
print len(set(first))
