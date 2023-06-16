students =[]

def show_students():
    for students in students:
        print("Alumno ->",students)

def  add_student(student):
    students.append(student)
def remove_student(student):
    try:
        students.remove(student)
    except Exception:
        print("No existe")
    
choice_text='''
Elige una opción:
    1- Insertar
    2- Mostrar
    3- Salir
'''
while True:
    choice=int(input(choice_text))
    if choice == 1:
        student = input("Ingresa student: ")
        add_student(student)
    elif choice == 2:
        show_students()
    elif choice == 3:
        student = input("Ingresa student a Eliminar: ")
    elif choice == 4:
        break
    else:
        print('Incorrect Option!')  