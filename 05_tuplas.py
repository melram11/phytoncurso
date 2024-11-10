## Tuples ##

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (24 , 1.75, "Melvin", "Ramos", "Melvin")
my_other_tuple = (35, 60, 30)

my_new_tuple = tuple()
my_new_tuple = (25, 1.85, "Joaquin", "Marquez", "Joaquin") 
print(my_new_tuple)

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

print(my_sum_tuplas[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Melramdev"
my_tuple.insert(1, "Azul")
print = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#del my_tuple[2]

del my_tuple

#print(my_tuple)
print(my_other_tuple)

