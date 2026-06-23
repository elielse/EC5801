import queue
import logging
import threading
import time

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

    # Método para eliminar una cola        
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
        logging.debug("elemento agregado a la cola")

    # Método para recibir datos
    def receive(self, name:str):

        # Verificamos que la cola exista
        if not self.__queue_dict__.get(name):
            logging.error("queue name does not exists")
            return None
        
        # Verificamos que no está vacía
        if self.__queue_dict__[name].empty():
            logging.info("No hay elementos a recibir")
            return None
        
        # Finalmente, retornamos el valor y ejecutamos la función callback
        data = self.__queue_dict__[name].get()
        logging.debug("data recibida")
        
        if self.__callback_dict__.get(name):
            self.__callback_dict__[name](data)
        return data
    
    # Metodo de poll
    def poll(self):

        # Iteramos sobre las colas recibiendo datos y ejecutando los callbacks
        for cola in self.__queue_dict__.keys():
            self.receive(cola)
        

# Callback function, pasando el mensaje como argumento e imprimiendolo
def callback_function(data:str):
    print("Callback function, data: ", end = "")
    if data: print(data)

# Loop para el hilo1
def loop_1():

    # timeout para que la ejecucion termine sola
    timeout = 15
    while timeout:
        time.sleep(2)
        msg_man.poll()
        timeout -= 1

logging.basicConfig(level=logging.DEBUG, filename = "logging_info.log", filemode="w", format = "%(asctime)s - %(levelname)s - function: %(funcName)s - %(message)s")
msg_man = Messages_Manager()


hilo1 = threading.Thread(target = loop_1)


msg_man.create("cola", 5, function = callback_function)
hilo1.start()

msg_man.send("cola", "1")
msg_man.send("cola", "2")
msg_man.send("cola", "3")
msg_man.send("cola", "4")
msg_man.send("cola", "5")
msg_man.send("cola", "6")
msg_man.send("cola", "7")
msg_man.send("cola", "8")


# Especie de .join() pero imprimiendo "...""
while(hilo1.is_alive()):
    print("...")
    time.sleep(4)

msg_man.delete("cola")
