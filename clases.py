# Definimos la clase MATRIZ
class MATRIZ:
    # Variable de clase para almacenar la matriz
    _x: list = []

    # Inicializacion
    def __init__(self, x):
        self._x = x;
    
    # Metodo getter
    def __get__(self):
        return self._x
    
    # Operacion suma
    def __add__(self, other):
        __result:list = []
        for element in range(len(self._x)):
            fila_result = []
            for col in range(len(self._x[element])):
                fila_result.append(self._x[element][col] + other._x[element][col])
            __result.append(fila_result)
        return __result
    
    # Operacion resta
    def __sub__(self, other):
        __result:list = []
        for element in range(len(self._x)):
            fila_result = []
            for col in range(len(self._x[element])):
                fila_result.append(self._x[element][col] - other._x[element][col])
            __result.append(fila_result)
        return __result
    
    # Operacion multiplicacion
    def __mul__(self, other):
        __result:list = []
        if len(self._x[0]) != len(other._x):
            raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")
        for element in range(len(self._x)):
            fila_result = []
            for col in range(len(other._x[element])):
                sum = 0
                for k in range(len(self._x[element])):
                    sum += self._x[element][k] * other._x[k][col]
                fila_result.append(sum)
            __result.append(fila_result)
        return __result
    
    # Operacion division
    def __truediv__(self, other):
        print("La división de matrices no está definida.")
        return None
    
# Matriz de prueba
matriz : list = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 [10,11,12]]

m1 = MATRIZ(matriz)
m2 = MATRIZ(matriz)
m3 = MATRIZ(m1 / m2)

# Imprimimos si no hay division
if m3.__get__() is not None:
    print(*(m3.__get__()), sep = '\n')