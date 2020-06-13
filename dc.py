from itertools import chain
def fun(i,j):
    if(all([k[i+1][j-1],k[i][j+1]])):
        return k[i+1][j-1]+k[i][j+1]-k[i+1][j]+1
    elif(any([k[i+1][j-1],k[i][j+1]])):
        if(k[i+1][j-1]==0):
            return max(k[i+1][j],k[i][j+1],k[i+1][j+1])+1
        else:
            if(k[i+1][j]==0):
                if(k[i+1][j+1]==0):
                    return k[i+1][j-1]+1
                if(k[i+1][j+1]==k[i+1][j-1]):
                    if(k[i+2][j]):
                        return k[i+1][j-1]+k[i+1][j+1]+2-k[i+2][j]
                    return k[i+1][j-1]+k[i+1][j+1]+1
                return k[i+1][j-1]+k[i+1][j+1]+1-k[i+2][j]
            else:
                return max(k[i+1][j-1],k[i+1][j],k[i+1][j+1])+1
    else:
        return max(k[i+1][j-1],k[i+1][j-1],k[i+1][j-1],k[i+1][j+1])+1


k=[]
for _ in range(int(input())):
    n,m=map(int,input().split())
    li=[]
    for i in range(n):
        li.append(list(map(int,input().split())))
    def f(l,n,m):
        if(n>m):
            for i in range(n):
                l[i]+=[0]*(n-m)
        elif(m>n):
            for i in range(m-n):
                l.append([0]*m)
        n=max(n,m)
        global k
        k=[]
        for i in range((max(n,m)+2)):
            k.append([0]*(max(n,m)+2))
        for i in range(n-1,-1,-1):
            for j in range(n-i):
                #print(n-j-1,i+j)
                if(l[n-j-1][i+j]):
                    k[n-j-1][i+j]=fun(n-j-1,i+j)
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                #print(i-j,j)
                if(l[i-j][j]):
                    k[i-j][j]=fun(i-j,j)
        for i in k:
            print(i)
        print()
        return max(chain.from_iterable(k))
    x=[[li[j][i] for j in range(len(li))] for i in range(len(li[0]))] 
    print(max(f(x[:],m,n),f(li[:],n,m)))
