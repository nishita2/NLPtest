#coding: UTF-8
import sys

file = open('sample.txt','r')
txt = file.readlines()
argv = sys.argv
n = int(argv[1])
for i in range(0,n):
    print txt[i].strip('\n')
