g=float(input("enter score : "))
if(g>=0.0 and g<=1.0):
    if g>=0.9:
        print("A")
    elif g>=0.8:
        print("B")
    elif g>=0.7:
        print("C")
    elif g>=0.6:
        print("D")
    else:
        print("F")
else:
    print("INVALID RANGE")
