#taking inputs from the user
from hashlib import new


frd=[]
num=int(input("How many name you gonna add: "))
#adding the item in list 
for i in range(num):
    add=input("Enter the name of the friends: ")
    frd.append(add)
    
print(frd)
print(len(frd))
#reversing in the list
for i in reversed(frd):
    new_frd=[]
    new_frd.append(i)
    print(new_frd)