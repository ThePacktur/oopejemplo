class Concierto:
    def __init__(self,nombre:str,horario:str,precio:float,capacidad:int,codConcierto:str,idConcierto: int=0):
        
        self.__nombre = nombre
        self.__horario = horario
        self.__precio = precio
        self.__capacidad = capacidad
        self.__codConcierto = codConcierto
        self.__idConcierto = idConcierto

    def get_nombre(self):
        return self.__nombre
    
    def get_horario(self):
        return self.__horario    
    def get_precio(self):
        return self.__precio
    
    def get_capacidad(self):
        return self.__capacidad
    
    def get_codConcierto(self):
        return self.__codConcierto
    
    def get_idConcierto(self):
        return self.__idConcierto
    
    def set_nombre(self,nombre):
        self.__nombre =  nombre       

    def set_horario(self,horario):
        self.__horario =horario        

    def set_precio(self,precio):
        self.__precio =  precio       

    def set_capacidad(self,capacidad):
        self.__capacidad =  capacidad       

    def set_codConcierto(self,codConcierto):
        self.__codConcierto = codConcierto         

    def set_idConcierto(self,idConcierto):
        self.__idConcierto = idConcierto         
