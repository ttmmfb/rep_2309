with open('rosalind_maj.txt', 'r') as file:
    k,n=map(int, file.readline().split())

    ans=[]
    
    for _ in range(k):
        posl=list(map(int, file.readline().split()))
        found=-1
        for x in set(posl):
            if posl.count(x)>n/2:
                found=x
                break
        ans.append(found)

print(*ans)