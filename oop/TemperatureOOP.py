#class temperature
class Temperature:
    def __init__(self):
         self.temp=0
         
    
    def set_temp(self):
        self.temp=int(input("Enter the temperature: "))
        
    def get_temp(self):
        return self.temp
    
        
tempObj=Temperature()
def calculation(temp):
    result=""
    if temp>=100:
        result=" hot day"
        
    elif temp>=80:
        result=" mid hotty day"
        
    elif temp>=60:
        result="normal day"
        
    elif temp>=40:
        result=" mid cool day"
        
    else:
        result=" cold day"
        
    return result
            
           
def display():
    tempObj.set_temp()
    final=calculation(tempObj.temp)
    print(f"The temperature is: {tempObj.temp} and the result will be {final}.")   
            
    
display() 