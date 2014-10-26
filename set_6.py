#coding: UTF-8
import sys

file = open('sample.txt','r')
txt = file.readlines()
length = len(txt)
argv = sys.argv
n = int(argv[1])
for i in range(length-n,length):
    print txt[i].strip('\n')
