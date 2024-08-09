
erro=0
try:
    h=int(input("Enter hours : "))
    r=int(input("Enter hours : "))
except ValueError:
    print("Error, please enter numeric input")
    erro=1
if erro==0:
    pay=h*r
    print("Pay = ",pay)
