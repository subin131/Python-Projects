#adding the five numbers in list where inputs are given from the user
numbers=[]
for i in range(5):
    num=int(input(f"Enter the {i+1} number: "))
    numbers.append(num)
 
    
print(numbers)
# to write into the file
f=open("listNumber.txt","w")
f.write(str(numbers))
f.close()


#to read the file
file=open("listNumber.txt","r")
print("the file have")
print(file.read())
file.close()