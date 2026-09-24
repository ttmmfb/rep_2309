def GC(l):
    c=l.count('C')+l.count('G')
    return c/len(l)*100

m=0
with open('fasta1.txt', 'r') as file:
    for line in file:
        line=line.strip()
        if line[0]=='>':
            name=line
            continue
        else:
            GC_count=GC(line)
            if GC_count>m:
                m=GC_count
                max_name=name
print(max_name[1:], m)