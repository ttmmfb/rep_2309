with open('kodon.txt','r') as file:
    kodon=[]
    let=[]
    for line in file:
        a=line.split()
        kodon.append(a[0])
        let.append(a[1])

with open('string6.txt', 'r') as file:
    ans=''
    s=file.readline().strip()
    for i in range(0,len(s)-2,3):
        kod=s[i]+s[i+1]+s[i+2]
        l=let[kodon.index(kod)]
        if l=='Stop':
            break
        ans+=l
print(ans)