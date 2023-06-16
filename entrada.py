#function input -> retorna string
name=input('Como te llamas? \n')
age= int (input('>Cuantos años tienes? \n'))
future=int (input('cuantos años más? \n'))

print("Hola "+ name)
print("En "+ str(future)+ "años tendras"+ str(age + future))

#Formant Strings
"""
       Hola Ignacio, en 3 años tendras 24 años
"""
text_complete="Hola {}, en {} años tendras {} años"
print(text_complete.format(name, future, age+ future))

print(f"Hola {name}, en {future} años tendras {age + future} años")