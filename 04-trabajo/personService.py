from repository import Repository
from person import Person
class PersonService:

    def get_personList(self):
        print(Repository().person)

    def add_person(self, person):
        print("...Agregando persona...")
        lastKey = -1
        for key in Repository.person:
            lastKey = key
        lastKey = lastKey + 1
        Repository.person [lastKey] = person.__dict__
    
    def update_person(self ,key):
        while True:
            z = int(input("Elija una opcion: 1.Modificar Nombre. 2.Modificar Apellido. 3.Modificar edad, 4.Cancelar"))
            if z == 1:
                Repository.person[key]['_name'] = str(input("Ingrese nombre de la persona: ").upper())
            elif z==2:
                Repository.person[key]['_surname'] = str(input("Ingrese apellido de la persona: ").upper())
            elif z==3:
                Repository.person[key]['_age']= int(input("Ingrese apellido de la persona: "))
            elif z==4:
                break
            else:
                ValueError("El valor ingresado no esta contemplado")

    def delete_person(self ,key):
        print("...Eliminando...")
        del Repository.person[key]
       

