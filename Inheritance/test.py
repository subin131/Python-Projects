class Vehicle:  
    def horn(self):  
        print("Cute horn")  
        
        
#child class Dog inherits the base class Animal  
class Car(Vehicle):  
    def brake(self):  
        print("car braking")  
d = Car()  
d.brake()  
d.horn()  