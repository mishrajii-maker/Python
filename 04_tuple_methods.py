#Give me some tuple method 

a= (1,45,342,3424, False,"Rohan","Shivam")   
print(a)

no = a.count(45) #45 ak bar aya hai whi bta rha 
print(no)

#Note: Tuple is immutable, so most of the list methods (like .append(), .remove(), etc.) don’t work on tuples.


i=a.index(3424)
print(i) #3rd index pr hai.

print(len(a)) #length bta rha

print(45 in a) #in keyword


t=[1,2,3,4]     #convert list to tuple 
l=tuple(t)
print(l)