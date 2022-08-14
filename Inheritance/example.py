class Person:  
    def run(self):  
        print("People can run")  
        
        
#child class Dog inherits the base class Animal  
class Student(Person):  
    def eat(self):  
        print("students can eat")  
d = Student()  
d.eat()  
d.run()  