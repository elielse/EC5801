import logging

# Testing logging library

logging.basicConfig(level=logging.INFO, filemode="w", format = "%(asctime)s - %(levelname)s - function: %(funcName)s - %(message)s")

def division(a:float,b:float):
    try:
        result = a/b
        logging.info("result = " + str(result))
        return result
    except: logging.critical("division by 0")


division(1,0)
division(1,1)

# Se puede hacer lo mismo con otras funciones

# Ahora probamos a guardar los loggers en un archivo
my_logger = logging.getLogger("Logger personalizado")
my_loggerHandler = logging.FileHandler(filename = 'log_info.log', mode = "w")

format = logging.Formatter("%(asctime)s - %(levelname)s - function: %(funcName)s logger name: %(name)s - %(message)s")
my_loggerHandler.setFormatter(format)
my_logger.addHandler(my_loggerHandler)

my_logger.error("testing my logger")