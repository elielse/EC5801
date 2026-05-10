
# Definimos la clase punto
class point:

    # Coordenadas xyz
    __xpos:int
    __ypos:int
    __zpos:int

    # Inicializamos las coordenadas, siempre y cuando la entrada tenga 3 componentes
    def __init__(self, x):
        if len(x) != 3:
            raise ValueError("Se requieren 3 componentes para definir el punto")
        self.__xpos = x[0]
        self.__ypos = x[1]
        self.__zpos = x[2]

    # Getters
    def get_x(self):
        return self.__xpos
    def get_y(self):
        return self.__ypos
    def get_z(self):
        return self.__zpos
    
    # Suma
    def __add__(self, other):
        return [self.__xpos + other.__xpos, self.__ypos + other.__ypos, self.__zpos + other.__zpos]
    
    # Multiplicacion por escalar, especificar ejes a usar
    # ex. point.mul(esc, "xyz")
    def mul(self, esc:int , which_axis:str):
        v_esc : int = [1,1,1]

        for i in range(0, len(which_axis), 1):
            if which_axis[i] == "x": v_esc[0] = esc
            elif which_axis[i] == "y": v_esc[1] = esc
            elif which_axis[i] == "z": v_esc[2] = esc
            else: raise ValueError("Invalid Axis")
        
        return [self.__xpos * v_esc[0], self.__ypos * v_esc[1], self.__zpos * v_esc[2]]

class padre_point(point):
    def __init__(self, x):
        super().__init__(x)
    def magnitud(self):
        return self.get_x()**2 + self.get_y()**2 + self.get_z()**2

punto_1 = point([1,2,3])
punto_2 = point([4,5,6])

print(punto_1 + punto_2)
print(punto_1.mul(10, "xz"))
