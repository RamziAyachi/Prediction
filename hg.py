
n,m=map(int,input().splite())
lisn=list(map(int,input().split()))
lism=list(map(int,input().split()))
print (lisn[n-1])

result=0
for i in range (0,n):
    s=0
    for j in range (i,n):
        s+=ln[j]
        for u in range (0,m):
            t=0
            p=u
            while((t<s)&(p<m)):
                t+=lm[p]
                p+=1
            if (t==s):
                result+=1

print (result)
        


