try:
    f=open("abc.txt",'r')
    print(f.read())
    for i in f:
        print(i)
    
finally:
    f.close()
    print("Thank You")