from Concierto import Concierto
from DAO import DAO

def registrar_concierto():
    print("---Vas a registrar---")
    codConciento = input("Ingrese codigo del concierto: ")
    nombre = input("ingrese nombre del conciento: ")
    horario = input("Ingrese horario del concierto: ")
    precio = float(input("Ingrese el precio del concierto: "))
    capacidad = int(input("Ingrese la capacidad de personas en el concierto: "))
    c = Concierto(nombre,horario,precio,capacidad,codConciento)
    d = DAO()
    d.registrar_concierto(c)

def buscar_concierto() -> Concierto:
    codigo = input("Ingrese el codigo del concierto: ")
    d = DAO
    c = d.buscar_concieto(codigo)
    print(c)
    return c

def eliminar_concierto():
    c = buscar_concierto()
    if c!=None:
        d = DAO()
        d.eliminar_concierto(c.get_codConcierto())
    else:
        print("El codigo no existe vuelva a intentar con un codigo valido")
    

def modificar_concierto():
    c= buscar_concierto()
    if c!=None:
        d = DAO()
        c.set_codConcierto(preguntar_cambio("codigo",c.get_codConcierto()))
        c.set_nombre(preguntar_cambio("nombre",c.get_nombre()))
        c.set_horario(preguntar_cambio("Horario",c.get_horario()))
        c.set_precio(float(preguntar_cambio("Precio",c.get_precio())))
        c.set_capacidad(int(preguntar_cambio("Capacidad",c.get_capacidad())))
        


    else:
        print("El Codigo no existe")
    
def preguntar_cambio(valor:str,atributo):
    opcion = input(f"Desea modificar el {valor}: s/n ")
    if opcion.lower() =="s":
        v = input(f"Ingrese el {valor}: ")
        return v
    else:
        return atributo




def mostrar_todo():
    pass

def menu():
    print("Bienvenido")
    print("----opciones-----")
    print("1.- Registrar Concierto ")
    print("2.- Buscar Concierto ")
    print("3.- Eliminar Concierto")
    print("4.- Modificar Concierto")
    print("5.- Mostrar Todo")
    print("6.- Salir ")
    opcion = input("Ingrese una opcion: ")
    if opcion =="1":
        registrar_concierto()
    elif opcion == "2":
        buscar_concierto()
    elif opcion == "3":
        eliminar_concierto()
    elif opcion == "4":
        modificar_concierto()
    elif opcion == "5":
        mostrar_todo()
    elif opcion =="6":
        print("Gracias por ultilizar el programa, vuelva pronto.")
        return True
    else:
        print("La opcion ingresada no es valida, intentelo nuevamente.")


while menu() !=True:
    pass
