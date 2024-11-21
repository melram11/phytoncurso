### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Melvin","Ramos", 24}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("MelvinDev")

print(my_other_set) # No se garantiza el orden

my_other_set.add("MelvinDev") # No se puede agregar elementos duplicados

print(my_other_set)

print("Melvin" in my_other_set)
print("Melven" in my_other_set)

my_other_set.remove("Melvin")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set) NameError porque ya no existe

my_set = {"Melvin", "Ramos", 24}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#",}))

print(my_new_set.difference(my_set))