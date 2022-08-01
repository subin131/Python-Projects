#program to take multiple inputs in dictionary



def initialDisplay():
    print
    print("""      Welcome to the Exam Marks Program   """)
    

def calculation():
    marks={}
    grade=""
    print("Now taking subjects marks..")
    ca=int(input(f"Enter the computer architecture marks: "))
    db=int(input(f"Enter the database marks: "))
    marks["cd"]=ca
    marks["db"]=db
    total=ca+db;
    percent=total/2;
    if(percent>80):
        grade="A"
    elif(percent>70):
        grade="B"
    elif(percent>60):
        grade="C"
    else:
        grade="F"
    return grade
    
    

def inputStudent():
    initialDisplay()
    num=int(input("Enter the number of students: "))
    students={}
    for i in range(num):
        students[i]={}
        name=input(f"Enter the name of the {i+1} student: ")
        address=input(f"Enter the address of the {i+1} student: ")
        sem=int(input(f"Enter the semester of the {i+1} student: "))
        year=int(input(f"Enter the year of the {i+1} student: "))
        
        grade= calculation()
        print(f"""  Student Name: {name},
        Student Address: {address},
        Student Semester: {sem},
        Student Year: {year},
        Stucdent Grade: {grade}
              """)
        students[i]["name"]=name
        students[i]["address"]=address
        students[i]["sem"]=sem
        students[i]["year"]=year
        students[i]["Grade"]=grade
        
    return students

print(inputStudent())