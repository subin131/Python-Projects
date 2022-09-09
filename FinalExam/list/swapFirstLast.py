#lets consider the list with the elements 
fruits=["apple","orange","mango","kiwi"]

# print(fruits[0])

a=fruits[0]
b=fruits[-1]
print(f"Before {a} and {b}")
temp=a
a=b
b=temp
print(f"After {a} and {b}")

