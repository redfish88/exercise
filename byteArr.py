#coding:utf-8
a = 127
s = bin(a)[2:][::-1]
print [2**x for x in range(len(s)) if s[x] == '1']
print max(3,2,1)

