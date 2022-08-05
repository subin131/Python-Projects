#sunway student tracking system SSTS
def initialDisplay():
    inital="""Welcome to the Sunway Student Tracking System (SSTS)"""
    print(inital)
    
#function to calculate the cube of each number
def cubesum():
    num=int(input("Enter a number: "))
    length=len(str(num))
    x=num
    sum=0
    while num>0:
        a=num%10
        sum+=a**length
        num//=10
    return x,sum
    
def Armstrong():
    initialDisplay()
    x,sum=cubesum()
    if x==sum:
        print(f"{x} is an Armstrong number")
    else:
        print(f"{x} is not an Armstrong number")
        

Armstrong()