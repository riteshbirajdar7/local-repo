try:
    print(x) #x is not defined , so it can raise an error
except:
    print("error occured") # this is gonna print
else:
    print("All correct") # it is going to occur either error is there or not


#ANother example with no errors
try:
    print("Hi") #it will print HI
except:
    print("error occured") #it is not going to print as error is not there
else:
    print("All correct") # it is going to occur either there is error or not
