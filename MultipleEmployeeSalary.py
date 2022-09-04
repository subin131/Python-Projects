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
        choice=input("Enter Y for married and N for unmarried: ")
        
        employees[i]={f"name: {name},salary:{salary},choice:{choice}"}
        
    return employees

def conditionalChoice():
    data=inputDisplay()
    for i in range(data):
        choice=data[i+2]
        if choice=="Y":
            tax=marriedTax()
        else:
            tax=unmarriedTtax()
            
    return tax

def marriedTax():
    pass

def unmarriedTax():
    pass



print(inputDisplay())
