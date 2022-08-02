def initialDisplay():
    inital="""Welcome to the Sunway Student Tracking System (SSTS)"""
    print(inital)

def countChar():
    initialDisplay()
    countupper=0
    countlower=0
    countNum=0
    countSpecial=0
    #taking inputs from users
    info=input("Enter a string containing letters,digits and numbers: ")
    for i in info:
        if i.isupper():
            print(f"{i} is a upper case letter")
            countupper=countupper+1
        elif i.islower():
            print(f"{i} is a lower case letter")
            countlower=countlower+1
        elif i.isdigit():
            print(f"{i} is a digit")
            countNum=countNum+1
        else:
            print(f"{i} is a special character")
            countSpecial=countSpecial+1
    return countupper,countlower, countNum,countSpecial,info
    
upper,lower,number,special,data=countChar()
print(f"There are  {upper} letters ,{lower} letters ,{number} digits with {special} special character in the string {data}")
