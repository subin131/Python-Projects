terms=int(input("enter the range: "))
fib1=0
fib2=1
print(fib1)
for i in range(terms):

    fib=fib1+fib2
    fib1=fib2
    fib2=fib
    print(fib)
