#coding: UTF-8

file = open('sample.txt')
txt = file.read()
a = txt.split("\t")
print ' '.join(a)
