s1={1,45,6,78}
s2={7,8,1,78}

print(s1.union(s2))
print(s1.intersection(s2))

#===============================================================
a = {1, 2, 3}
b = {3, 4, 5}

a.add(6)
a.update([7, 8])
a.discard(10)  # No error
# a.remove(10) # Would raise KeyError

print(a.union(b))            # {1, 2, 3, 4, 5, 6, 7, 8}
print(a.intersection(b))     # {3}
print(a.difference(b))       # {1, 2, 6, 7, 8}
print(a.symmetric_difference(b)) # {1, 2, 4, 5, 6, 7, 8}
