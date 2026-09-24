from random import *

bases='ATCG'
l=randint(1,1000)
s1=''.join(choice(bases) for _ in range(l))
s2=''.join(choice(bases) for _ in range(l))
print(s1)
print(s2)

count=0
for i in range(l):
    if s1[i]!=s2[i]:
        count+=1
print(count)