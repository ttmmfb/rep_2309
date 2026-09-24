with open('graf.txt','r') as file:
    n,r=map(int, file.readline().split())
    sosed=[[] for _ in range(n+1)]
    for i in range(r):
        x1,x2=map(int, file.readline().split())
        sosed[x1].append(x2)
        sosed[x2].append(x1)
    stepeni=[len(sosed[i]) for i in range(n+1)]
    s_s=[]
    for i in range(n+1):
        s_s.append(sum(stepeni[k] for k in sosed[i]))
    s_s=s_s[1:]

print(*s_s)