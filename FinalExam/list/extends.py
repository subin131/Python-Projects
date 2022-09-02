#extends is to used to add all the item of one ;list to another
numbers=[1,2,4,5,7,8]
copy_num=[]
copy_num.extend(numbers)
print(f"The copy of {copy_num}")


numbers.extend([1,43])
print(numbers)