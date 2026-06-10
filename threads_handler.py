import logging

import threading

import time

from typing import Callable, Any, Dict, Optional

# Archivo correspondiente a la parte 2 y 3 de la tarea 3

# Clase para el manejador de hilos
class THREAD_HANDLER():


    __max_threads__:int
    __threads_register:dict

    # Inicializamos la clase
    def __init__(self, max_threads: int)->None:
        self.__max_threads__ = max_threads
        self.__threads_register = {}
    
    # Allojamos la informacion del hilo pero no lo iniciamos aun
    def Thread_Allocate(self, name:str, function: Callable, **kwargs):
        
        if self.__threads_register.get(name) == None:
            
            self.__threads_register[name] = {"function": function, "kwargs":kwargs['kwargs'], "thread":None}

            return True
        logging.warning("El nombre del hilo ya existe")
        return False
    
    # Ahora si iniciamos el hilo siempre y cuando no se supere el limite de hilos
    def Thread_Start(self, name:str):

        if threading.active_count() < self.__max_threads__:

            # Creamos el hilo
            self.__threads_register[name]["thread"] = threading.Thread(target = self.__threads_register[name]["function"], kwargs = self.__threads_register[name]["kwargs"])

            # Creamos el evento asociado al hilo
            self.__threads_register[name]["event"] = threading.Event()
            
            print(self.__threads_register[name]["thread"])

            # Intentamos ejecutar la callback start function, si es que existe
            try:
                self.__threads_register[name]["Callback_Start"]()
            except: logging.info("No hay callback start function")
            
            # Iniciamos el hilo
            self.__threads_register[name]["thread"].start()

        else:
            logging.info("No hay hilos disponibles")
        
        
            
    # Registramos las funciones callback en el diccionario
    def Thread_Callback_Register(self, name:str, callback_function_start: Callable = None, callback_function_end: Callable = None):

        

        if self.__threads_register.get(name):
            
            self.__threads_register[name]["Callback_End"] = callback_function_end
            self.__threads_register[name]["Callback_Start"] = callback_function_start
        else:
            logging.error("No existe el hilo a relacionar las callback functions")

    
    def Thread_End(self, name:str):

        # Setteamos el evento, llamamos la callback end function, y quitamos la clave name del diccionario
        self.__threads_register[name]["event"].set()
        self.__threads_register[name]["Callback_End"]()
        self.__threads_register.pop(name)

        

    def Thread_Sync(self, name:str):

        # Sincronizamos esperando a que finalice el hilo
        try:
            self.__threads_register[name]["thread"].join()
        except:
            logging.error("No se pudo sincronizar con el hilo")
    
    
    

# Funcion de prueba para el callback start
def Callback_Start_fc() -> None:
    print("Callback Start function")

# funcion de prueba para el callback end
def Callback_End_fc() -> None:
    print("Callback End function")
        
# Funcion a ejecutar en el hilo de prueba
def hilo_1(text:str, timeout: int) -> None:
    print("Ejecutando funcion del hilo, con tiempo de ejecucion de:",timeout, "segundos")
    
    time.sleep(timeout)
    print(text)

# Testeando el thread handler

text = "texto de prueba"
thread_handler = THREAD_HANDLER(5)

logging.basicConfig(level=logging.INFO,)

thread_handler.Thread_Allocate("hilo 1", hilo_1, kwargs = {"text":text, "timeout":10} )
thread_handler.Thread_Callback_Register("hilo 1", 
                                        callback_function_start=Callback_Start_fc, 
                                        callback_function_end=Callback_End_fc)
thread_handler.Thread_Start("hilo 1")

thread_handler.Thread_Sync("hilo 1")

thread_handler.Thread_End("hilo 1")
