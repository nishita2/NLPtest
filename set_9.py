#coding: UTF-8

file = open('sample.txt','r')
txt = file.readlines()
second = []
dict = {}
for row in txt:
    a = row.split('\t')
    second.append(a[1])
    dict[a[1]] = a[0]
second.sort()
second.reverse()
for i in second:
    print dict[i]+'\t'+(i.strip('\n'))
