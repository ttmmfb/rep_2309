from math import *

k,m,n=map(int, input().split())
ppl=k+m+n

#k - AA
#m - Aa
#n - aa

def C(x,y): #сочетания по x из y
    return factorial(y)/(factorial(y-x)*factorial(x))

m_n=1/2*C(1,m)*C(1,n)/C(2,ppl)
m_m=1/4*C(2,m)/C(2,ppl)
n_n=C(2,n)/C(2,ppl)

P=1-(m_n+m_m+n_n)
print(P)