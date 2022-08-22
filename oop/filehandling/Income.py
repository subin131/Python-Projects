import json


class Income:
    def __init__(self):
       
    
        self.initial="""
        Welcome to tax service
        Inland Revenue Department 
           Lazimpat, kathmandu
                          
        """ 
        print(self.initial)
        
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
            with open('convert.txt', 'w') as file:
                file.write(json.dumps(employees))
        
        return employees
        
    #function for married
    def married(self):
        print("You are married!!")
        tax=0
        exclude_tax=0
        tax_rate=""
        annual_income=self.monthly_income*12
        if annual_income<400000:
            exclude_tax=annual_income*0.99
            tax=annual_income-exclude_tax
            tax_rate="1%"      
        elif annual_income<=500000:
            exclude_tax=annual_income*0.90
            tax=annual_income-exclude_tax
            tax_rate="10%"
        elif annual_income<=1700000:
            exclude_tax=annual_income*0.80
            tax=annual_income-exclude_tax
            tax_rate="30%"
        elif annual_income<=2450000:
            exclude_tax=annual_income*0.80
            tax=annual_income-exclude_tax
            tax_rate="36%"
        return tax,exclude_tax,tax_rate
    
    def unmarried(self):
        print("You are unmarried!!")
        tax=0
        exclude_tax=0
        tax_rate=""
        annual_income=self.monthly_income*12
        if annual_income<450000:
            exclude_tax=annual_income*0.99
            tax=annual_income-exclude_tax
            tax_rate="1%"      
        elif annual_income<=550000:
            exclude_tax=annual_income*0.90
            tax=annual_income-exclude_tax
            tax_rate="10%"
        elif annual_income<=1750000:
            exclude_tax=annual_income*0.80
            tax=annual_income-exclude_tax
            tax_rate="30%"
        elif annual_income<=2450000:
            exclude_tax=annual_income*0.80
            tax=annual_income-exclude_tax
            tax_rate="36%"
        return tax,exclude_tax,tax_rate
    
    def category(self):
        
        if self.choice=="Y":
            tax,exclude_tax,tax_rate=self.married()
            return tax,exclude_tax,tax_rate
        else:
            tax,exclude_tax,tax_rate=self.unmarried()
            return tax,exclude_tax,tax_rate
                    
                    
    def display(self):
        print(self.initial)
        tax,exclude_tax,tax_rate=self.category()
        print(f"Name: {self.name}                          Address: {self.address}")
        print(f"Year: {self.year}                          Pan: {self.pan}")
        print(f"The tax amount is {tax} and tax excluded income is {exclude_tax} with the rate {tax_rate} for the income Rs.{self.monthly_income*12}")
        print("******************************************************")
        
t=Income()
result=t.setInput()
print(result)