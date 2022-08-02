#sunway student tracking system SSTS
def initialDisplay():
    inital="""Welcome to the Sunway Student Tracking System (SSTS)"""
    print(inital)
    
def cubesum():
    num=int(input("Enter a number: "))
    x=num
    a=num%10
    num=int(num/10)
    b=num%10
    c=int(num/10)
    sum=a**3+b**3+c**3
    return x,sum
    
def Armstrong():
    initialDisplay()
    x,sum=cubesum()
    if x==sum:
        print(f"{x} is an Armstrong number")
    else:
        print(f"{x} is not an Armstrong number")
        

Armstrong()