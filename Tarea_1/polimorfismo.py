import asyncio

# Funcion para modelar el delay
async def delay(t:float):
    await asyncio.sleep(t)
    print(t)
class HD:
    __read_delay: float = 0.1
    __write_delay: float = 0.15
    __mem: bytearray
    def __init__(self, N: int):
        self.__mem = bytearray(N)

    def get(self, offset: int, size: int):
        asyncio.run(delay(self.__read_delay))
        result = bytearray(size)
        for i in range(0, size, 1):
            result[i] = self.__mem[i + offset]
        return result
    
    def set(self, data: bytearray ,offset: int, size: int):
        asyncio.run(delay(self.__write_delay))
        for i in range(0, size, 1):
            self.__mem[offset + i] = data[i]
    
class RAM:
    __read_delay: float = 0.01
    __write_delay: float = 0.015
    __mem: bytearray
    def __init__(self, N: int):
        self.__mem = bytearray(N)

    def get(self, offset: int, size: int):
        asyncio.run(delay(self.__read_delay))
        result = bytearray(size)
        for i in range(0, size, 1):
            result[i] = self.__mem[i + offset]
        return result
    
    def set(self, data: bytearray ,offset: int, size: int):
        asyncio.run(delay(self.__write_delay))
        for i in range(0, size, 1):
            self.__mem[offset + i] = data[i]
    
class SRAM:
    __read_delay: float = 0.001
    __write_delay: float = 0.0015
    __mem: bytearray
    def __init__(self, N: int):
        self.__mem = bytearray(N)

    def get(self, offset: int, size: int):
        asyncio.run(delay(self.__read_delay))
        result = bytearray(size)
        for i in range(0, size, 1):
            result[i] = self.__mem[i + offset]
        return result
    
    def set(self, data: bytearray ,offset: int, size: int):
        asyncio.run(delay(self.__write_delay))
        for i in range(0, size, 1):
            self.__mem[offset + i] = data[i]

def write(x, data, offset, size):
    x.set(data, offset, size)
def read(x, offset, size):
    return x.get(offset, size)



hard_disk = HD(10)
data = bytearray(5)
data = [0x00, 0x01, 0x02, 0x03, 0x04]
hard_disk.set(data, 0, 5)
hard_disk.set([0xff, 0xff], 5, 2)

print(hard_disk.get(0, 10))
print(read(hard_disk, 0, 10))
