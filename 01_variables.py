#  Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)


# Concatenacion de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)


# Funciones del sistemas
print(len(my_string_variable))

# Variables en una sola linea.  ! Cuidado con abusar de esto,
name, surname, alias, age = "Melvin", "Ramos", "MelRam", 24
print("Me llamo:", name, surname, ". Mi edad es:", age, "Y mi alias es:", alias)

""""# Inputs
first_name = input("What is your name: ")
age = input("How old are you? ")

print(first_name)
print(age)"""

# Cambiamos su tipo
name = 24
age = "Melvin"
print(name)
print(age)

# Forzamos el tipo?
address: str = "Mi direccion"
address = 32
print(type(address))