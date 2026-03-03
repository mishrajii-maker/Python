'''
def goodDay(name,ending):
    print("Good Day,"+name)
    print(ending)



#call 
goodDay("Harry","Thank you") #arguments harry pass kr rhe uper name receive kr k print kr dega .
goodDay("Rohan","Thank you") #Rohan name me chla jayega aur thank you ending wale parameter me .
goodDay("Divya","Thank you") 

'''
#======================================================

def goodDay(name,ending):
    print("Good Day,"+name)
    print(ending)
    return "ok" #yha ki return value a me asign ho jayegi agr return value nhi denge to a hmesa none value dega 



#call 
a= goodDay("Harry","Thank you")
print(a) 