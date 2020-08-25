from personService import PersonService
from person import Person

class Opciones:

    def inicio(self):
        personService = PersonService()
        print("\n Bienvenido, a continuacion seleccione una de las siguientes opciones: ")
        while True:
            print("\n1. Agregar personas")
            print("\n2. Modificar datos de la persona")
            print("\n3. Eliminar persona")
            print("\n4. Listar personas")
            print("\n5. Salir")
            x = int(input("\nElija una opción: "))
            if x == 1:
                    # Agregar personas
                    p1 = Person()
                    p1.name = str(input("Ingrese un nombre: "))
                    p1.surname = str(input("Ingrese un Apellido: "))
                    p1.age = int(input("Ingrese una edad: "))
                    personService.add_person(p1)
            elif x==2:
                key = int(input("Ingrese clave que desea modificar: "))
                personService.update_person(key)
            elif x==3:
                key = int(input("Ingrese clave que desea eliminar: "))
                personService.delete_person(key)
            elif x==4:
                personService.get_personList()
            elif x==5:
                print("...Saliendo...")
                break
            else:
                print(ValueError("Opcion no contemplada"))