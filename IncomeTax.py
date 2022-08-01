print("*********************************")
print("        Inland Revenue Department        ")
print("          Lazimpat, kathmandu     ")
print("                Welcome to           ")
print("          Integrated Tax System (ITS)    ")
print("*********************************")



#function for married tax system
def married_tax():
    tax=0
    print("You are married")
    income=int(input("Enter your income: "))
    if(income>=450000):
        tax=income*0.99
        tax_rate="1%"
    elif(income>=550000):
        tax=450000*0.99 + (income-450000)*0.90
        tax_rate="10%"
    elif(income>=1700000):
        tax=450000*0.99 + (income-450000)*0.70
        tax_rate="30%"
    elif(income>2450000):
        tax=450000*0.99 + (income-450000)*0.64
        tax_rate="36%"
    return tax,tax_rate
    
#function for unmarried tax system
def unmarried_tax():
    tax=0
    print("You are unmarried")
    income=int(input("Enter your income: "))
    if(income>=400000):
        tax=income*0.99
        tax_rate="1%"
    elif(income>=500000):
        tax=400000*0.99 + (income-400000)*0.90
        tax_rate="10%"
    elif(income>=1700000):
        tax=450000*0.99 + (income-400000)*0.70 
        tax_rate="30%"
    elif(income>2450000):
        tax=450000*0.99 + (income-400000)*0.64
        tax_rate="36%"
    return tax,tax_rate


def tax_calculation():
    numOfCustomer=int(input("Enter the number of customer: "))
    for i in range(numOfCustomer):
        choice=input(f"Enter {i+1} choice where Y for Married and N for Unmarried:  ")
        name=input("Enter your name: ")
        address=input("Enter your address: ")
        pan=input("Enter your PAN number: ")
        year=(input("Enter the year: "))
        if(choice=="Y"):
            tax_m,tax_rate=married_tax()
            print("******************************")
            print(f"Tax Payee: {name}                                     Adress: {address}")
            print(f"PAN No: {pan}                 FY:{year}               Married Status:{choice} ")
            print(f"Tax Payee {name} with {pan} fall under {tax_rate} Tax slab. ")
            print(f"{name} ({pan}) to pay tax to government is [Rs.]={tax_m}")
            print("******************************")

        elif(choice=="N"):
            tax_u,tax_rate=unmarried_tax()
            print("******************************")
            print(f"Tax Payee: {name}                                     Adress: {address}")
            print(f"PAN No: {pan}                 FY:{year}               Married Status:{choice} ")
            print(f"Tax Payee {name} with {pan} fall under {tax_rate} Tax slab. ")
            print(f"{name} ({pan}) to pay tax to government is [Rs.]={tax_u}")
            print("******************************")


tax_calculation()


       

        
    
    
            
            
            
            
        
            
    