try:
    n=int(input("Enter a number : "))
except ValueError:
    print("only int accepted")
else:
    if n%2==0:
        print("Even")
    else:
        print("ODD")
