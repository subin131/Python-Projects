
try:
    with open ("abc.txt",'r') as f:
        
    # print(f.read())
        for i in f:    
            print(i," " )
        
finally:
    print("Finally")