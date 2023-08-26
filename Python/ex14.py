n=2

count=0

while count<10:
    prime=True
    for m in range(2,n):
        if n%m==0:
            prime=False
            break
    if prime:
        print(n)
        count+=1
    n+=1

