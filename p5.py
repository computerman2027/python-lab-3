#try:
#    print(x)
#except:
#    print("An exception occurred")
#print(x)



try:
    print(x)
except NameError:
    print("Variable x not defined")
except:
    print("Somethings else went wrong")
