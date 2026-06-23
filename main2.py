import queue
import logging
import threading

class Messages_Manager():

    __queue_dict__:dict
    __callback_dict__:dict
    __lockers__:dict

    # Inicializamos los diccionarios internos utilizados
    def __init__(self):
        self.__queue_dict__ = {}
        self.__callback_dict__ = {}
        self.__lockers__ = {}
    
    # Método para crear una cola
    def create(self, name:str, max_queue_items:int, function = None):
        
        # Si el nombre de la cola no existe previamente en el diccionario cremos la cola
        if not self.__queue_dict__.get(name):
            self.__queue_dict__[name] = queue.Queue(max_queue_items)
            self.__lockers__[name] = threading.Lock()
        else:
            logging.error("Ya existe una cola con ese nombre")
        
        # Si hay función callback se guarda
        if function:
            self.__callback_dict__[name] = function
            
    # Método para eliminar la cola
    def delete(self, name:str):

        if self.__queue_dict__.get(name):
            self.__queue_dict__[name].shutdown()
            self.__queue_dict__.pop(name)

        if self.__callback_dict__.get(name):
            self.__callback_dict__.pop(name)
    
    # Método para enviar datos
    def send(self, name:str, data: str):

        # Si no existe el nombre de la cola arroja un error
        if not self.__callback_dict__.get(name):
            logging.error("queue name does not exists")
            return
        
        # Si está full espera a que haya chance
        if self.__queue_dict__[name].full():
            try:
                self.__lockers__[name].acquire()
                self.__queue_dict__[name].put(data)
                self.__lockers__[name].release()
            except:
                logging.error("Error al intentar el send")
        else:    
            self.__queue_dict__[name].put(data)
    
    # Método para recibir datos
    def receive(self, name:str):

        # Verificamos que la cola exista
        if not self.__queue_dict__.get(name):
            logging.error("queue name does not exists")
            return None
        
        # Verificamos que no está vacía
        if self.__queue_dict__[name].empty():
            logging.error("No hay elementos a recibir")
            return None
        
        # Finalmente, retornamos el valor y ejecutamos la función callback
        data = self.__queue_dict__[name].get()
        
        if self.__callback_dict__.get(name):
            self.__callback_dict__[name](data)
        return data

# Callback function, pasando el mensaje como argumento
def callback_function(data:str):
    print("Callback function, data: ", end = "")
    if data: print(data)
msg_man = Messages_Manager()

# Probamos creando una cola, agregando elementos y recibiendo para probar los distintos casos
#

msg_man.create("cola", 5, function = callback_function)
msg_man.send("cola", "123456789")

msg_man.receive("cola")
msg_man.receive("cola")
msg_man.delete("cola")


