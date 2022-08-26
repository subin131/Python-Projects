#taking input from the user
name=input("Enter the name of the student: ")
roll=input("Enter the roll number: ")

a=f"The name of the student is {name} and roll number is {roll}"

f=open("test.txt","a")
f.write(a)
f.close