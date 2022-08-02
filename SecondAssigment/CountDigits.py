def initialDisplay():
    inital="""Welcome to the Sunway Student Tracking System (SSTS)"""
    print(inital)
    
def countChar():
    initialDisplay()
    countLetter=0
    countNum=0
    countSpecial=0
    #taking inputs from users
    info=input("Enter a string containing letters,digits and numbers: ")
    for i in info:
        if i.isalpha():
            print(f"{i} is a letter")
            countLetter=countLetter+1
        elif i.isdigit():
            print(f"{i} is a digit")
            countNum=countNum+1
        else:
            print(f"{i} is a special character")
            countSpecial=countSpecial+1
    return countLetter,countNum,countSpecial,info
    
letter,number,special,data=countChar()
print(f"There are  {letter} letters and {number} digits with {special} special character in the string {data}")

            

    