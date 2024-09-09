print("Hola " + "Phyton " + 'Que tal?')
print("Hola" > "Phyton")

### Operadores Logicos


print(3 > 4 and "Hola" > "Phyton" )
print(3 > 4 or "Hola" > "Phyton" )
print(3 < 4 and "Hola" < "Phyton" )
print(3 < 4 or "Hola" > "Phyton" )
print(3 < 4 or "Hola" > "Phyton" and 4 == 4 )
print(not (3 > 4))

#print(3 > 4  "Hola" > "Phyton" )


#ejercicio Supongamos que estás construyendo una aplicación para una tienda en línea y necesitas verificar si un cliente cumple con ciertos criterios para aplicar un descuento. Aquí está el escenario:
##Criterios para aplicar un descuento:
##El cliente debe ser mayor de 18 años.
##El cliente debe haber realizado al menos 3 compras anteriore

edad = 18
compras = 8

cumple_edad = edad > 18
compras_realizadas = compras >= 3

if cumple_edad and compras_realizadas:
    print("Apto para el descuento: ")
else:
    print("No cumple con los requerimientos")

##Supongamos que estás desarrollando un sistema de autenticación para una aplicación web. Necesitas verificar si un usuario proporciona las credenciales correctas para iniciar sesión. Aquí están los criterios:
#El usuario debe ingresar un nombre de usuario válido (por ejemplo, no puede estar vacío).
#La contraseña debe tener al menos 8 caracteres

nombre_usurio = input("Ingresa tu Nombre de usuario")
contrasena = input("Ingrese Contrena")

nombre_valido = bool(nombre_usurio)
contrasena_valida = len(contrasena) >= 8

if nombre_valido and contrasena_valida:
    print("Credenciales Validas")
else:
    print("Error en las credenciales: " + "Contrasena debe contener 8 digitos!!")


numero = int(input("Ingrese un Numero Entero: "))

if numero % 2 == 0:
    print(f"{numero} es un numero Par: ")
else:
    print(f"{numero} no es un numero Impar: " )

