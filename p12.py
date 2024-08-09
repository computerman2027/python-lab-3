try:
    a=float(input("enter number a: "))
    b=float(input("enter number b: "))
    c=float(input("enter number c: "))
except ValueError:
    print("only float and integer accepted")
else:
    print("max = ",max(a,b,c))
    print("min = ",min(a,b,c))
