def cifre_pare(n):
    nr=0
    n=abs(n)

    while n>0:
        m=n%10
        if m%2==0:
            nr+=1
        n=n//10
    return nr
print(cifre_pare(-246813))

