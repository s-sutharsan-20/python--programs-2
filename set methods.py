set_a={1,2,9,6,'r','s',5,1,5,'d'}
set_b={2,0,4,5,'t',3,'f','m','s','t'}
print(set_a)
print(set_b)
c=set_a.copy()
print(c)
print(c.clear())
print(c)
print(set_a.difference(set_b))
print(set_a-set_b)
print(set_b.difference(set_a))
print(set_b-set_a)
print(set_a.union(set_b))
print(set_a|set_b)
print(set_a.intersection(set_b))
print(set_a&set_b)
print(set_a.symmetric_difference(set_b))
print(set_a^set_b)
