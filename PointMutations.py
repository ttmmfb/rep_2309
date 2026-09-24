# from random import *

# bases='ATCG'
# l=randint(1,1000)
# s1=''.join(choice(bases) for _ in range(l))
# s2=''.join(choice(bases) for _ in range(l))
# print(s1)
# print(s2)

with open('CPM.txt','r') as file:
    s1=file.readline()
    s2=file.readline()

count=0
for i in range(len(s1)):
    if s1[i]!=s2[i]:
        count+=1
print(count)