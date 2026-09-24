with open('rosalind_mer.txt', 'r') as file:
    n=int(file.readline().strip())
    a=list(map(int, file.readline().split()))
    m=int(file.readline().strip())
    b=list(map(int, file.readline().split()))

c=[]
while a and b:
    if a[0]<=b[0]:
        c.append(a.pop(0))
    else:
        c.append(b.pop(0))
c+=a
c+=b
print(*c)