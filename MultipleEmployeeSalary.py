def initailDisplay():
    initial="""
    Welcome to the System
    """
    print(initial)
    
#display function
def inputDisplay():
    employees={}
    number=int(input("Enter how many employee do you want to add: "))
    for i in range(number):
        name=input(f"Enter the name of {i+1} employee: ")
        year=input(f"Enter the fiscal year of {i+1} employee:  ")
        salary=int(input(f"Enter the salary {i+1} employee: "))
        choice=input(f"Enter Y for married and N for unmarried of {i+1} employee: ")
        employees[i+1]={f'name': name, 'year':year, 'salary':salary,'choice':choice}
        
    return employees

def conditionalChoice():
    data=inputDisplay()
    #loop to get all nested dictionary with key and value
    for i in data:
        name=data[i]['name']
        year=data[i]['year']
        # print(data[i]['name'])
        if data[i]['choice']=="Y":
            tax,tax_rate,tax_amt=tax_married(data[i]['salary'])
            display(name,year,tax,tax_rate,tax_amt)
            
        else:
            tax,tax_rate,tax_amt=tax_unmarried(data[i]['salary'])
            display(name,year,tax,tax_rate,tax_amt)
        
    

def tax_married(s):
    tax=0
    tax_amt=0
    tax_rate=""
    income=s*12
    if(income<=450000):
        tax_amt=income*0.99
        tax=income-tax_amt
        tax_rate="1%"
    elif(income<=550000):
        tax_amt=income*0.90
        tax=income-tax_amt
        tax_rate="10%"
    elif(income<=1700000):
        tax_amt=income*0.80
        tax=income-tax_amt
        tax_rate="20%"
    elif(income<2450000):
        tax_amt=income*0.64
        tax=income-tax_amt
        tax_rate="36%"
    return tax,tax_rate,tax_amt
    

def tax_unmarried(s):
    tax=0
    tax_rate=""
    tax_amt=""
    income=s*12
    if(income<=400000):
        tax_amt=income*0.99
        tax=income-tax_amt
        tax_rate="1%"
    elif(income<=500000):
        tax_amt=income*0.90
        tax=income-tax_amt
        tax_rate="10%"
    elif(income<=1700000):
        tax_amt=income*0.80
        tax=income-tax_amt
        tax_rate="20%"
    elif(income>2400000):
        tax_amt=income*0.64
        tax=income-tax_amt
        tax_rate="36%"
    return tax,tax_rate,tax_amt

def display(n,y,t,tr,ta):
   
    print(f"Employee Name: {n}                Year: {y}")
    print(f"The tax of the employee {n} is {t} with the rate of {tr}")


conditionalChoice()
