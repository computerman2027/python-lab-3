try:
    n=int(input("Enter a number : "))
    if n>=0:
        print("POSITIVE")
    else:
        print("NEGATIVE")
except ValueError:
    print("only int accepted")