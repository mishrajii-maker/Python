#Dictionary mutable hoti hai isko change kr skte hai  

marks= {
    "Harry":100,
    "Shubham":56,
    "Rohan":23,
}

print(marks.items()) #key value ke pair ka ak list deta hai 

print(marks.keys()) #keys print krne k liye 
print(marks.values())#values print krne k liye

marks.update({"Harry":99,"Renuka":100})#marks update kr skte hai aur new value nd key add kr skte h kyuki dic ki value change ho skti h
print(marks)

print(marks.get("Harry2"))#Prints None
        #or
print(marks["Harry2"])#Returns an error

#=====================================================

d = {'a': 1, 'b': 2}

print(d.get('a'))           # Output: 1
print(d.get('c', 0))        # Output: 0
print(d.keys())             # Output: dict_keys(['a', 'b'])
print(d.values())           # Output: dict_values([1, 2])
print(d.items())            # Output: dict_items([('a', 1), ('b', 2)])

d.update({'c': 3})
print(d)                    # Output: {'a': 1, 'b': 2, 'c': 3}

d.pop('b')                  # Removes 'b'
print(d)                    # Output: {'a': 1, 'c': 3}

d2 = d.copy()
print(d2)                   # Output: {'a': 1, 'c': 3}
