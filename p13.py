import sys
try:
    h=int(input("Enter hours : "))
    r=int(input("Enter hours : "))
except ValueError:
    print("Error, please enter numeric input")
    sys.exit()
pay=h*r
print("Pay = ",pay)
