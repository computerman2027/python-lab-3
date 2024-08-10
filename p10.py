try:
    x= int(input("Enter a number : "))
except:
    x='n'
    print("Error")
if x == 'n':
    pass
elif x%2==0:
    print("EVEN")
else:
    print("ODD")