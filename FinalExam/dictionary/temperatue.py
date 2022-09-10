#creating the class
class Temperature:
    def __init__(self):
        initial="Welecome to our services"
        print(initial)
        
        
    def setInput(self):
        temperatures={}
        num=int(input("Enter how many temperature should be added: "))
        for i in range(num):
            temp=int(input(f"Temperature day [{i+1}] = "))
            temperatures[i+1]=temp
        return temperatures
    
    def categoryCheck(self):
        data=self.setInput()
        countHot=0
        results={}
        countNormal=0
        countCold=0
        totalTemp=0
        average=0
        for day,temp in data.items():
            totalTemp=totalTemp+temp
            average=totalTemp/len(data)
            print(temp)
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
        return results, countHot,countNormal,countCold,average,data
        
        
    
    def Display(self):
        res,ch,cn,cc,avg,data=self.categoryCheck()
        print("\nDaily Temperature Reports")
        for i,v in data.items():
            print(f"Temperature Day [{i+1}] = {v} Celcius {res[i]}")
            
        print("\n")
        print(f"The average Temp for  days is {avg} Celcius")
        print(f"Number of hot days= {ch} day/s")
        print(f"Number of normal days= {cn} day/s")
        print(f"Number of cold days= {cc} day/s")
    
        
        
            
           
            
obj=Temperature()
obj.Display()