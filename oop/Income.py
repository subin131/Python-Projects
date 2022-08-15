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
    



def setInput():
        name=input("Enter the name: ")
        address=input("Enter the address: ")
        pan=input("Enter the pan number: ")
        year=input("Enter the year: ")
        monthly_income=int(input("Enter the montly_income: "))
        choice=input("Enter the Y for married and N for unmarried: ")
        if choice=="Y":
            tax_amt=salary.calculationMarried(monthly_income)
        else:
            tax_amt=salary.calculationUnmarried(monthly_income)
            
        return tax_amt
    
def display():
    initailDisplay()
    tax=setInput()
    print(f"The tax amount {tax}")
    


            
        
    
        
            
        