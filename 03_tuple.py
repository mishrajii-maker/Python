a= (1,2,4,7,9)
print(type(a))


a= ()   #empty tuple
print(type(a))


a= (1,)   # sirf 1 rkhunga to int ayega aur comma lg jayega to tuple kehlayega 
print(type(a))


a= (1,45,342,3424, False,"Rohan","Shivam")   

a[0]=453 #ham tuble ko change nhi kr skte hai.
print(type(a))