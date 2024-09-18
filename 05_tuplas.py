## Tuples ##

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (24 , 1.75, "Melvin", "Ramos", "Melvin")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) indexError
#print(my_tuple[-6]) indexError

print(my_tuple.count("Melvin"))
print(my_tuple.index("Ramos"))
print(my_tuple.index("Melvin"))

#my_tuple[1] = 1.80 'tuple' object does not support item assignment

my_sum_tuplas = my_tuple + my_other_tuple
print(my_sum_tuplas)
