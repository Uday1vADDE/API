l=[7,7,7,7,7,7]
d={}
o=0
for i in l:
    d[i]=d.get(i,0)+1
k=len(l)//2
l1=list(d.values())
l1.sort(reverse=True)
i=0
while(k>0):
    o+=1
    k-=l1[i]
    i+=1
print(o) #1338


