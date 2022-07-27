def example():
    students={}
    num=int(input("Enter the number of students: "))
    for i in range(num):
        students[i]={}
        name=input(f"Enter the name of the {i+1} student: ")
        address=input(f"Enter the address of the {i+1} student: ")
        age=int(input(f"Enter the age of the {i+1} student: "))
        
        students[i]["name"]=name
        students[i]["address"]=address
        students[i]["age"]=age
        
    return students

print(example())