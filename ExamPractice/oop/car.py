#class of the car
class Vehicle:
    def __init__(self,color,value):
        self.color = color
        self.value = value
        
    def get_car1(self):
        print(self.color,self.value)
        

print("-----------------------------")
for i in range(2):
    color=input(f"Enter the color of {i+1} the car: ")
    worth=int(input(f"Enter the worth of {i+1} the car: "))    
    car1=Vehicle(color,worth)
    car2=Vehicle(color,worth)
    print(car1.get_car1())
    