#initail function
def initailDisplay():
    initial="""
    Welcome to the System
    """
    print(initial)
    
#display function
def inputDisplay():
    employees={}
    number=int(input("Enter how many employee do you want to add ?"))
    for i in range(number):
        name=input("Enter the name: ")
        salary=int(input("Enter the salary: "))
        
        employees[i]={f"name: {name},salary:{salary}"}
        
    return employees


print(inputDisplay())
