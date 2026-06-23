import queue
import logging
import threading

class Messages_Manager():

    __queue_dict__:dict
    __callback_dict__:dict

    # Inicialización
    def __init__(self):

        # Diccionario para las colas, y otro para las funciones callback
        self.__queue_dict__ = {}
        self.__callback_dict__ = {}
        
    # Método para crear una cola
    def create(self, name:str, max_queue_items:int, function = None):

        # Si el nombre de la cola no existe previamente en el diccionario cremos la cola
        if not self.__queue_dict__.get(name):
            self.__queue_dict__[name] = queue.Queue(max_queue_items)
            logging.debug("Nueva cola")
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

# Función de callback para testear
def callback_function():
    print("Callback function")

msg_man = Messages_Manager()

msg_man.create("cola", 5, function = callback_function)

msg_man.delete("cola")