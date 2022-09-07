import json


class Income:
    def __init__ (self):
        print("Welcome to System..")
        
    def inputDetails(self):
        employee={}
        num=int(input("Enter how many employee: "))
        for i in range(num):
            name=input(f"Enter the {i+1} employee name: ")
            year=input(f"Enter the {i+1} employee fiscal year: ")
            salary=int(input(f"Enter the {i+1} employee salary: "))
            choice=input(f"Enter the choice of {i+1} employee Y for married and N for unmarried: ")
            employee[i+1]={'name': name,  'year':year,'salary':salary,'choice':choice}
            with open('file.txt', 'w') as file:
                file.write(json.dumps(employee))
        return employee
    
    def checkCondition(self):
        data=self.inputDetails()
        for i in data:
            name=data[i]['name']
            year=data[i]['year']
            # print(data[i]['name'])
            if data[i]['choice']=="Y":
                tax,tax_rate,tax_amt=self.tax_married(data[i]['salary'])
                # print(f"The tax is {tax} of tax excluded amount {tax_amt} with the rate {tax_rate}")
                self.display(name,year,tax,tax_rate,tax_amt)
            else:
                tax,tax_rate,tax_amt=self.tax_unmarried(data[i]['salary'])
                # print(f"The tax is {tax} of tax excluded amount {tax_amt} with the rate {tax_rate}")
                self.display(name,year,tax,tax_rate,tax_amt)
                
    def tax_married(self,s):
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
    
    def tax_unmarried(self,s):
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
    
    def display(self,n,y,t,tr,ta):
        print(f"Employee Name: {n}                Year: {y}")
        print(f"The tax of the employee {n} is {t} with the rate of {tr}")
        

   
take=Income()
take.checkCondition()
        