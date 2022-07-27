

def initialDisplay():
    print("----------------------------------------------------")
    print("      Welcome to the Exam Marks Program")
    
    

initialDisplay()
    
    

def calculation(m):
   
    grade=""
    percent=m/100*100
    print(percent)
    if percent>80:
        grade="A"
    elif percent>70:
        grade="B"
    elif percent>60:
        grade="C"
    elif percent>50:
        grade="D"
    else:
        grade="F"
        
    return grade

def finalDisplay():
    print("----------------------------------------------------")
    num=int(input("Enter the number of students: "))
    for i in range(num):
        name=input(f"Enter the name of the {i+1} student: ")
        mark=int(input(f"Enter the marks of the {i+1} student: "))
        grade=calculation(mark)
        print("Student Name: ",name)
        print("Student Grade: ",grade)
    

finalDisplay()
    


    
    