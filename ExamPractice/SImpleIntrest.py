#calculating the simple intrest
amount=int(input("Enter the amount: "))
time=int(input("Enter the time: "))
rate=int(input("Enter the rate: "))

def Intrest(amount,time,rate):
    
    intrest=(amount*time*rate)/100;
    print(f"The intrest for amount {amount} with the time {time} years of rate {rate} is {intrest}")
    
Intrest(amount,time,rate)