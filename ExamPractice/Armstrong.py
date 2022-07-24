# number 
num=int(input("Enter a number: "))
x=num
c=num%10
c_result=c**3
num=int(num/10)
b=num%10
b_result=b**3
num=int(num/10)
a_result=num**3
result=a_result+b_result+c_result


if x==result:
    print(f"{x} is Armstrong number")
else:
    print(f"{x} is not an Armstrong number")
