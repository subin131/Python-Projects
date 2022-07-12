print("**************************************")
print("   Department of Transport Management   ")
print("            Baneswor, kathmandu     ")
print("Welcome to DOTM Bike Renewal System")
print("            Fiscal Year=2020/21")


name=input("Enter your name:")
address=input("Enter your address:")
phone=input("Enter your phone number:")
def calculate_tax():
    
    bike_cc=int(input("Enter the bike cc:"))
    tax=0
    if(bike_cc>=125):
        tax=2800
    elif(bike_cc>125 and bike_cc<=160):
        tax=4500
    elif(bike_cc>161 and bike_cc<=250):
        tax=5500
    elif (bike_cc>251 and bike_cc<=400):
        tax=9000
    elif (bike_cc>401 and bike_cc<=650):
        tax=20000
    elif (bike_cc>651):
        tax=30000
    return bike_cc,tax

bike_cc,tax=calculate_tax()
print(f"Customer Name: {name}                   Address:{address}")
print(f"Customer Bike [cc]: {bike_cc}           Phone No:{phone}")
print(f"{name} with {bike_cc} cc have to pay Tax to [Rs.]={tax}")