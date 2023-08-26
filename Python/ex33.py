def process_data(func,*args,**kwargs):
    def func(*args,**kwargs):
        sum=0
        for nr in args:
            sum=sum+nr
        for key,value in kwargs.items():
            print(key,value)
process_data(func,123,matei="oipwe")