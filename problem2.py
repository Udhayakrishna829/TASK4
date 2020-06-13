for _ in range(int(input())):
    n=int(input())
    z=list(map(int,input().split()))
    l=list(map(int,input().split()))
    d={}
    k=[]
    for i in range(n):
        d[i+1]=[]
        k.append(i+1)
    m=int(input())
    if(m):
        i=0
        for j in l:
            l[i]=[z[i],-j]
            i+=1
        p=sorted(l)
        for i in range(m):
            x,y=map(int,input().split())
            k.remove(y)
            d[x].append(y)
        sum=0
        while(p!=[]):
            for i in p:
                if(l.index(i)+1 in k):
                    a=l.index(i)
                    sum+=(i[0]*-i[1])
                    p.remove(i)
                    k+=d[a+1]
                    for j in range(len(p)):
                        p[j][0]+=z[a]
                    break
    else:
        sum=0
        i=0
        for j in l:
            l[i]=[j,z[i]]
            i+=1
        k=0
        for i in sorted(l,reverse=True):
            sum+=((k+i[1])*i[0])
            k+=i[1]
    print(sum)
    
