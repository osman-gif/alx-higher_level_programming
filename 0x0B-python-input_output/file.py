#!/usr/bin/python3

lis = ['first', 'middle', 'age']
dic = {'first': 'os', 'last':'dg', 'age': 25}

ndic = {}

for l in lis:
    if l in list(dic.keys()):
        ndic[l] = dic[l]
print(ndic)


