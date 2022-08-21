class Income:
    def __init__(self):
        initial=""" Welcome to tax service""" 
        print(initial)
        
    def setInput(self):
        self.name=input("Enter the name of the employee: ")
        self.address=input("Enter the name of the address: ")
        self.pan=input("Enter the pan number: ")
        self.year=input("Enter the fiscal yaer: ")
        self.monthly_income=int(input("Enter the monthly income: "))
        self.choice=input("Enter Y for married and N for unmarried: ")
    #function for married
    def married(self):
        print("You are married!!")
        tax=0
        tax_rate=""
        if self.monthly_income<400000:
            tax=self.monthly_income*0.9 
            tax_rate="10%"      
        elif self.monthly_income<1000000:
            tax=self.monthly_income*0.8 
            tax_rate="20%"
        else:
            tax=self.monthly_income*0.7
            tax_rate="30%"
        return tax,tax_rate
    
    def unmarried(self):
        print("You are unmarried!!")
        tax=0
        if self.monthly_income<450000:
            tax=self.monthly_income*0.9  
            tax_rate="10%"      
        elif self.monthly_income<1100000:
            tax=self.monthly_income*0.8 
            tax_rate="20%"           
        else:
            tax=self.monthly_income*0.7
            tax_rate="30%"
        return tax,tax_rate
    
    def category(self):
        
        if self.choice=="Y":
            tax,tax_rate=self.married()
            print(f"The tax excluded income is {tax} with the rate {tax_rate} for the income Rs.{t.monthly_income}")
        else:
            tax,tax_rate=self.unmarried()
            print(f"The tax excluded income is {tax} with the rate {tax_rate} for the income Rs.{t.monthly_income}")
                    
t=Income()
t.setInput()
print(f"Name: {t.name}                          Address: {t.address}")
print(f"Year: {t.year}                          Pan: {t.pan}")
t.category()
