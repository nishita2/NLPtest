#coding: UTF-8

file = open('sample.txt','r')
col1 = open('col1.txt','w')
col2 = open('col2.txt','w')
a = file.readlines()
for column in a:
    b = column.split('\t')
    col1.write(b[0]+'\n')
    col2.write(b[1])

