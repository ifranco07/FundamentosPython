# Funciones
# def name_function(params):
#   code 

# Sin parámetros y sin retorno
def saluda():
    print("Hola a Todos!")
    
saluda()

# Con parámetros, sin retorno
def duplica(num):
    print(num * 2)

duplica(5)

def suma(num1, num2):
    print (f"La suma de los numeros es: { num1 + num2}")
    
suma(23, 45)

# Parámetros opcionales, sin retorno
def get_lista(al_1= "Jose", al_2= "Darlen"):
    return [al_1, al_2]

my_list = get_lista()
print(my_list)
my_list = get_lista("Peter")
print(my_list)
my_list = get_lista("Peter Parker", "Toy Stark")
print(my_list)
my_list = get_lista(al_2="Peter Parker", al_1="Toy Stark")
print(my_list)

