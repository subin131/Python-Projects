def initailDisplay():
    initial=""" Welcome to income tax office"""
    

class Income:
    def __init__(self):
        self.name
        self.address
        self.pan
        self.year
        self.monthly_income
        self.choice
    
    def setInput(self):
        self.name=input("Enter the name: ")
        self.address=input("Enter the address: ")
        self.pan=input("Enter the pan number: ")
        self.year=input("Enter the year: ")
        self.monthly_income=int(input("Enter the montly_income: "))
        self.choice=input("Enter the Y for married and N for unmarried: ")
        
    # def calculation(self):
    #     if self.choice=="Y":
    #         self.calculationMarried(self.monthly_income)
    #     else:
    #         self.calculationUnmarried(self.monthly_income)
            
    def calculationMarried(mi):
        tax=0
        if mi>4500000:
            tax=mi*0.99
        elif mi>600000:
            tax=mi*0.90
        else:
            tax=mi*0.60
        return tax
    
    def calculationUnmarried(mi):
        tax=0
        if mi> 450000:
            tax=mi*0.95
        elif mi >600000:
            tax=mi*0.75
        else:
            tax=mi*0.60 
        return tax
    


salary=Income()
def display():
    initailDisplay()
    if salary.choice=="Y":
        tax_m=salary.calculationMarried()
        print(f"The tax paid by {salary.name} of amount {tax_m}")
    else:
        tax_u=salary.calculationUnmarried()
        print(f"The tax paid by {salary.name} of amount {tax_u}")
 


            
        
    
        
            
        