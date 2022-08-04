#initial display information
def initialDisplay():
    initial="""
    Sunway Temperature Record Management System
                    Kathmandu Nepal
                    11 August 2022
    ------------------------------------------------
    """
    print(initial)
    
    
def inputInformation():
    temperatures={}
    days=int(input("How many days to record temperature? "))
    for i in range(days):
        temp=int(input(f"Temperature day [{i+1}] = "))
        temperatures[i+1]=temp
    return temperatures


def categoryCheck(temperature):
    results={}
    countHot=0
    countNormal=0
    countCold=0
    for day,temp in temperature.items():
        if temp>85:
            result="very hot"
            countHot=countHot+1
        elif temp>60 and temp<=85:
            result="pleasant day"
            countNormal=countNormal+1
        else:
            result= "very cold"
            countCold=countCold+1
        results[day]=result
    return results,countHot,countNormal,countCold
    
def calculationTemperature(temperature):
    total=0
    days=len(temperature)
    for temp in temperature.values():
        total+=temp
    average=total/days
    return average,days
      

def finalDisplay(temperature):
   
    daytype,ch,cn,cc=categoryCheck(temperature)
    avg,countDays=calculationTemperature(temperature)
    print("\nDaily Temperature Reports")
    for day,temp in temperature.items():
        print(f"Temperature Day [{day}] = {temp} Celcius {daytype[day]}")
    print("\n")
    print(f"The average Temp for {countDays} days is {avg} Celcius")
    print(f"Number of hot days= {ch} day/s")
    print(f"Number of normal days= {cn} day/s")
    print(f"Number of cold days= {cc} day/s")
    
initialDisplay()   
temperature=inputInformation()
finalDisplay(temperature)


