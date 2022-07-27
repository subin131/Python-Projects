#taking input from user and storing in a dictionary

def initialDisplay():
    print("----------------------------------------------------")
    print("      Welcome to the Exam Marks Program")
    
    
    
    
def subjectMark():
    sub1=int(input("Enter the marks of the first subject: "))
    sub2=int(input("Enter the marks of the second subject: "))
    sub3=int(input("Enter the marks of the third subject: "))
    return sub1,sub2,sub3


def calculation():
    s1,s2,s3=subjectMark()
    totalMark=s1+s2+s3
    percent=totalMark/300*100
    if percent>80:
        grade="A"
    elif percent>70:
        grade="B"
    elif percent>60:
        grade="C"
    else:
        grade="F"
    return grade
    
    
def displayStudent():
    initialDisplay()
    student={}
    num=int(input("Enter the number of students: "))
    for i in range(num):
        name=input(f"Enter the name of the {i+1} student: ")
        grade=calculation()
        student[i+1]=grade ,name
        print(student[i+1])
    return student

    

print(displayStudent())


