from Concierto import  Concierto
import credencial
import mysql.connector


class DAO:
    def __init__(self):
        pass

    def __conectar(self):
        self.__conexion = mysql.connector.connect(**credencial.get_credenciales())
        self.__cursor = self.__conexion.cursor()

    def __cerrar(self):
        self.__conexion.commit()
        self.__conexion.close()


    def registrar_concierto(self,c:Concierto):
        #hacer algo que lo lleve a la bd
        self.__conectar()
        sql = "INSERT INTO conciento (nombre,horario,precio,capacidad,codconcierto) VALUES(%s,%s,%s,%s,%s)" 
        values = (c.get_nombre(),c.get_horario(),c.get_precio(),c.get_capacidad(),c.get_codConcierto())
        self.__cursor.execute(sql,values)
        self.__cerrar()
        

    def buscar_concierto(self,codigo:str):
        #Hacer algo que recupere de la bd y retorne.
        pass

    def eliminar_cocierto(self,codigo:str):
        #hacer algo que elimine la bd
        pass

    def modificar_concierto(self,c:Concierto):
        #Hacer algo que modifique el concierto en la bd

        pass

    def mostrar_todo(self):
        #Hacer Algo que traiga todo de la bd y retorne
        pass
