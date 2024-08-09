
try:
    x= int(input("Enter a number :"))
except:
    x='n'
    print("Error")
#    raise a("happy")
if x is 'n':
    pass
elif x%2==0:
    print("Even")
else:
    print("odd")
