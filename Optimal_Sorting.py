n=int(input())
for i in range(n):
    m=int(input())
    i=list(map(int,input().split()))
    s=sorted(i)
    if i==s:
        print("0")
    else:
        print(max(i)-min(i))
        