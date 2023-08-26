def sum_args(*args):
    sum=0
    for nr in args:
        sum=sum+nr
    return sum
print(sum_args(1,5,6,7,8,4,54,6644,3))