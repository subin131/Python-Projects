def initialDisplay():
    inital="""Welcome to the Sunway Student Tracking System (SSTS)"""
    print(inital)
    
def passwordValidation():
    initialDisplay()
    countDigit=0
    countUpper=0
    countLower=0
    countSpecial=0
    password=input("Enter a password: ")
    if len(password)< 6 or len(password) >16:
        print("Password must be between 6 to 16 characters")
    else:
        for i in password:
            if i.isdigit():
                countDigit=countDigit+1
            elif i.isupper():
                countUpper=countUpper+1
            elif i.islower():
                countLower=countLower+1
            else:
                countSpecial=countSpecial+1
        if countDigit==0 or countUpper==0 or countLower==0 or countSpecial==0:
            print("Password must contain at least one digit,one upper case letter,one lower case letter and one special character")
        else:
            print("Password is valid")
            
passwordValidation()