class Income:
    def __init__(self):
        initial=""" Welcome to tax service""" 
        print(initial)
        
    def setInput(self):
        employees={}
        employee=int(input("How many employee to calculate the tax? "))
        for i in range(employee):
            self.name=input(f"Enter the name of {i+1} employee: ")
            self.address=input(f"Enter the name of {i+1} address: ")
            self.pan=input(f"Enter the pan number of {i+1} employee: ")
            self.year=input(f"Enter the fiscal year of {i+1} employee: ")
            self.monthly_income=int(input(f"Enter the monthly income of {i+1} employee: "))
            self.choice=input(f"Enter Y for married and N for unmarried for {i+1} employee: ")
            employees[i+1]=self.name,self.address,self.pan,self.year,self.monthly_income,self.choice
            self.display()
        
        return employees
        
    #function for married
    def married(self):
        print("You are married!!")
        #annual income need to calculate
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
            # print(f"The tax excluded income is {tax} with the rate {tax_rate} for the income Rs.{t.monthly_income}")
            return tax,tax_rate
        else:
            tax,tax_rate=self.unmarried()
            # print(f"The tax excluded income is {tax} with the rate {tax_rate} for the income Rs.{t.monthly_income}")
            return tax,tax_rate
                    
                    
    def display(self):
        tax,tax_rate=self.category()
        print(f"Name: {self.name}                          Address: {self.address}")
        print(f"Year: {self.year}                          Pan: {self.pan}")
        print(f"The tax excluded income is {tax} with the rate {tax_rate} for the income Rs.{self.monthly_income*12}")
        
t=Income()
result=t.setInput()
print(result)