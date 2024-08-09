print("MENU")
print("1. C to F")
print("2. F to C")
choice = int(input("enter your choice : "))
if choice==1:
    c=float(input("Enter temp in C : "))
    f=((9*c)/5)+32
    print("Temp in F =",round(f,2))
elif choice==2:
    f=float(input("Enter temp in F : "))
    c=((f-32)*5)/9
    print("Temp in C =",round(c,2))
else:
    print("INVAlID CHOICE")
