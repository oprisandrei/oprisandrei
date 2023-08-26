x=int(input("primul"))
y=int(input("al doilea"))
z=int(input("al treilea"))

if x>= y >= z:
    print(x,y)
elif x>=z>=y:
    print(x,z)
elif(y>=x>=z):
    print(y,x)
elif(y>=z>=x):
    print(y,z)
elif(z>=x>=y):
    print(z,x)
elif(z>=y>=x):
    print(z,y)