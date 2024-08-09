
try:
    h=int(input("Enter hours : "))
    r=int(input("Enter hours : "))
    pay=h*r
    print("Pay = ",pay)
except ValueError:
    print("Error, please enter numeric input")
    
