#comentario if and else
num = int (input ("Ingresar el numero:"))
if num % 2 == 0 :
    print ("par")
else :
    print ("impar")    

    for i in range (10) :
        print ("Es la tabla de :", i + 1)
        for ii in range (10) :
            print ("", i +1, 'x', ii + 1, "=", (i+1) *(ii+1))

#comment for and while
personas =['Armando', 'Jose', 'Pedro']
for i in personas :
    print (i)            


n = 5
while n>0 :
    print (n)
    n -=1

    #comentario  next while true
while True :
    parar = input ("Desea parar s/n:")
    if parar == 's' :
        print ("fin,")
        break
    else :
        print ("_________")



#comentario try and except 

try :
    fh = open("archivos.txt","a")
    fh.write ("Nombre: Melvin Ramos\n")
    fh.write ("Direccion: Guatemala\n") 
    fh.write ("Telefono: 4444\n")
    fh.close ()
    #leer
    fr = open ("archivo.txt","r")
    for linea in fr :
        print (linea.strip())

except :
    print ('error en el archivo.')
    exit()    