#soy un comentario de linea´

'''

Soy un comentario de bloque

'''

#variables en python
nombreUsuario = 'Juan jose'
#salida en concola
print("Hola, buenas noches ",nombreUsuario)
#fprint de python (Otra forma de concatenar)
print(f'Su nombre es {nombreUsuario}')


#Variables datos primitivos
edadUsuario = 32
estaturaUsuario = 1.62
esHinchaDelMejor = True  #"En python , El True o False (booleano) empiezan con mayuscula porque es una clase"
nombre = 'Juan jose'

print(f'Su nombre es {nombre} y usted es hinncha del mejor? {esHinchaDelMejor}')


#Entrada de datos por consola
numero1 = int(input("Didite un numero entero"))
numero2 = int(input("Didite otro numero entero"))
result = numero1+numero2
print(f'El resultado fue {result}')

#las condiciones logicas (condicionales) - IF
#Es importante tabular para que python entienda
if(numero1>0):
    print("Soy un nunmero positivo")
else:
    print("Soy un numero negativo")