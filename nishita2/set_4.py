#coding: UTF-8

col1 = open('col1.txt','r')
col2 = open('col2.txt','r')
a = col1.readlines()
b = col2.readlines()
n = len(a)
for i in range(0,n):
    print (a[i].strip('\n'))+'\t'+(b[i].strip('\n'))

