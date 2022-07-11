print("*********************************")
print("        Inland Revenue Department        ")
print("          Lazimpat, kathmandu     ")
print("                Welcome to           ")
print("          Integrated Tax System (ITS)    ")
print("*********************************")
name=input("Enter your name: ")
address=input("Enter your address: ")
pan=input("Enter your PAN number: ")
year=(input("Enter the year: "))

def tax_calculation():
    tax=0
    choice=input("Enter Y for Married and N for Unmarried:  ")
    if(choice=="Y"):
        print("You are married")
        income=int(input("Enter your income: "))
        if(income>=450000):
            tax=income*0.99
        elif(income>=550000):
            tax=450000*0.99 + (income-450000)*0.90
        elif(income>=1700000):
            tax=450000*0.99 + (income-450000)*0.70 
        elif(income>2450000):
            tax=450000*0.99 + (income-450000)*0.64
            
    elif(choice=="N"):
        print("You are unmarried")
        income=int(input("Enter your income: "))
        if(income>=400000):
            tax=income*0.99
        elif(income>=500000):
            tax=400000*0.99 + (income-400000)*0.90
        elif(income>=1700000):
            tax=450000*0.99 + (income-400000)*0.70 
        elif(income>2450000):
            tax=450000*0.99 + (income-400000)*0.64
    return tax,choice


tax,choice=tax_calculation()
print(f"Tax Payee: {name}                             Adress: {address}")
print(f"PAN No: {pan}            FY:{year}            Married Status:{choice} ")
print(f"Tax Payee {name} with {pan} fall under Tax slab. ")
print(f"{name} ({pan}) to pay tax to government is [Rs.]={tax}")

       

        
    
    
            
            
            
            
        
            
    