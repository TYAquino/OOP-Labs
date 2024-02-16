j = 99   #global
#variable length positional arguments
def add(*args):
    i = 20    #local variable and accessed inside the function only
    print(j)
    print(i)
    print(args)
    print(type(args))
    list1 = [*args]
    list2 = list(args)
    print(list2)
    print(list1)
    total = 0
    for val in args:
        total += val
    return total
        
# A dictionary is passed in
def printPrices(**kwargs):
    #print(i)
    print(j)
    print(kwargs)
    for productName, price in kwargs.items():
        print(f"The price of {productName} is {price:.2f}")

printPrices(ABC=11.95, widget=23.50)
   
#add()
#add(1)
#add(2,3)
print(add(2,3,4))
print(j)