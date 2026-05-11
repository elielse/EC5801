import time

# Clase modelando el HD, con delays de lectura y escritura
# Para crear variable de esa clase de pasa como argumento un numero entero
# con el numero de bytes a usar
class HD:
    __read_delay: float = 0.1
    __write_delay: float = 0.15
    __mem: bytearray
    __mem_size: int
    # Inicializacion
    def __init__(self, N: int):
        self.__mem = bytearray(N)
        self.__mem_size = N

    # Getter, pasando como argumentos la ubicacion
    # el offset y la cantidad de bytes a leer
    def get(self, offset: int, size: int):

        # Delay
        time.sleep(self.__read_delay)

        result = bytearray(size)
        for i in range(0, size, 1):
            result[i] = self.__mem[i + offset]
        return result
    
    # Setter, los argumentos son: data a escribir, ubicacion y el tamaño
    def set(self, data: bytearray ,offset: int):
        time.sleep(self.__write_delay)
        if len(data) + offset > self.__mem_size:
            return False
        for i in range(0, len(data), 1):
            self.__mem[offset + i] = data[i]
        return True

# Clase para modelar la RAM, en el codigo funciona igual que el HD pero con
# distintos delays
class RAM:
    __read_delay: float = 0.01
    __write_delay: float = 0.015
    __mem: bytearray
    __mem_size: int
    # Inicializacion
    def __init__(self, N: int):
        self.__mem = bytearray(N)
        self.__mem_size = N

    # Getter, pasando como argumentos la ubicacion
    # el offset y la cantidad de bytes a leer
    def get(self, offset: int, size: int):

        # Delay
        time.sleep(self.__read_delay)

        result = bytearray(size)
        for i in range(0, size, 1):
            result[i] = self.__mem[i + offset]
        return result
    
    # Setter, los argumentos son: data a escribir, ubicacion y el tamaño
    def set(self, data: bytearray ,offset: int):
        time.sleep(self.__write_delay)
        if len(data) + offset > self.__mem_size:
            return False
        for i in range(0, len(data), 1):
            self.__mem[offset + i] = data[i]
        return True

# Funciona en codigo igual a la RAM y HD pero con otros delays
class SRAM:
    __read_delay: float = 0.001
    __write_delay: float = 0.0015
    __mem: bytearray
    __mem_size: int
    # Inicializacion
    def __init__(self, N: int):
        self.__mem = bytearray(N)
        self.__mem_size = N

    # Getter, pasando como argumentos la ubicacion
    # el offset y la cantidad de bytes a leer
    def get(self, offset: int, size: int):

        # Delay
        time.sleep(self.__read_delay)

        result = bytearray(size)
        for i in range(0, size, 1):
            result[i] = self.__mem[i + offset]
        return result
    
    # Setter, los argumentos son: data a escribir, ubicacion y el tamaño
    def set(self, data: bytearray ,offset: int):
        time.sleep(self.__write_delay)
        if len(data) + offset > self.__mem_size:
            return False
        for i in range(0, len(data), 1):
            self.__mem[offset + i] = data[i]
        return True

# Funcion de escritura para el polimorfismo
def write(x, data, offset):
    x.set(data, offset)

# Funcion de lectura para el polimorfismo
def read(x, offset, size):
    return x.get(offset, size)



hard_disk = HD(10)
data = bytearray(5)
data = [0x00, 0x01, 0x02, 0x03, 0x04]
if hard_disk.set(data, 0) == False : print("error al escribir")
if hard_disk.set([0xff, 0xff], 8) == False : print ("error al escribir")

print(hard_disk.get(0, 10))
print(read(hard_disk, 0, 10))
