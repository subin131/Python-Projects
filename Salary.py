#program to receive the salary of a employee depending on the tax rate

def total_salary():
    salary = int(input("Enter the salary per month: "))
    total_salary=salary*12
    #for taxation
    if total_salary<15000:
        new_salary=total_salary*0.85
        return new_salary
    elif total_salary>15000 and total_salary<30000:
        new_salary=total_salary*0.82
        return new_salary
    elif total_salary>30000 and total_salary<50000:
        new_salary=total_salary*0.80
        return new_salary
    elif total_salary>50000:
        new_salary=total_salary*0.65
        return new_salary

print(f"The total salary is per year is : {total_salary()}")


        
    