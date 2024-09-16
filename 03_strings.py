## strigs

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string ))

print(my_string + " y " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_new_tap_string = "\tEste es un string con tabulacion"
print(my_new_tap_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# formateo de formato

name, surname, age = "Melvin", "Esteban", 24

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
#print("Mi nombre es %s %s y mi edad es $d" %(name, surname, age)) no funciona por alguna razon
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) #cuesta leer mas esto al programa
print("Mi nombre es {} {} y mi edad es {} anyos".format(surname, name , age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # mejor forma de defenir el formato

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# Division
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# reverse

reversed_language = language [ ::-1]
print(reversed_language)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.lower().isupper())
print(language.startswith("py"))

