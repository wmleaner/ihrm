N=int(input("N:"))
fib=[0 for x in range(N+1) ]
fib[0]=0
fib[1]=1
for i in range(2,N+1):
    fib[i]=fib[i-1]+fib[i-2]
print(fib[N])
