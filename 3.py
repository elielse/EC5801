# From YAML
from yaml import load, dump
try:
        from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# Typing imports
from typing import Any, Generic, TypeVar, cast
     
from pathlib import Path

# Import schema validator function
from schema_validator import schema_validator

generic_t = TypeVar("generic_t")


# Class to manage files
class YAML_HANDLER(Generic[generic_t]):
    

    def __init__(self) -> None:
        ...
        
    # get dict from path
    def load_file(self, file_path: Path, mode = 'r') ->dict:

        # Check if it is a correct path
        if file_path.exists():

            with file_path.open(mode) as config:
                config_data = load(config, Loader=Loader)
                return config_data
        else: raise ValueError("Ruta no valida")

    # write a dict in a file, given the path
    def write_file(self, datos, file_path: Path, mode = 'w'):

        # if the path is correct
        if file_path.exists():
            
            # open file and write the data
            with file_path.open(mode) as config:
                dump(datos, config, default_flow_style=False)
        else: raise ValueError("Error al abrir el archivo")

# class hereditary from YAML_HANDLER
class YAML_FILE_HANDLER(YAML_HANDLER):

    # Path for private dict
    __file_path__: Path = Path("data.yaml")
    # Private dict
    __dict__:dict

    # Init
    def __init__(self) -> None:
        super().__init__()
    
    # Add data from a file to __dict__, with key = 'name', value = {'path': ...,'data': ...}
    def add_stream(self, path_arg: Path, name: str) -> None:

        # If data format is like required_schema add it to __dict__ and return whether is it ok or not
        if process_data(self.load_file(path_arg)) != None:
            self.__dict__[name] = {'path': str(path_arg), 'data': self.load_file(path_arg)}
            return True
        return False
    
    # Getter given key name
    def get(self, name: str) -> dict:
        
        try: 
            return self.__dict__[name]
        except: return None
    
    # Save dict in predefined Path for private .yaml file
    def save_dict(self) -> None:
        self.write_file(self.__dict__, self.__file_path__)

required_schema = {'Nombre':str, 'Altura':int, 'Peso':int, 'Edad':int, 'Lista de habilidades':str, 'Descripcion':str}

# Fabric
@schema_validator(required_schema)
# Decorated function to process data
def process_data(data):
    return data

# Data a escribir que no teine los requerimientos
datos = {
    'nombre': 'Usuario',
    'edad': 30,
    'habilidades': ['Python', 'YAML']
}

yaml_file_handler = YAML_FILE_HANDLER()

#  Add config.yaml data to the private dictionary
if yaml_file_handler.add_stream(Path("config.yaml"), "Eliel"):

    # Prints if it could be added
    print("stream config.yaml was added ")
else: print("stream config.yaml could not be added ")

#  Add config.yaml data to the private dictionary
if yaml_file_handler.add_stream(Path("config.txt"), "config.txt"):

    # Prints if it could be added
    print("stream config.txt was added ")
else: print("stream config.txt could not be added ")

# Testing getter, and proving config.yaml has been added
print(yaml_file_handler.get("Eliel"))

# Saving private dictionary data into data.yaml
yaml_file_handler.save_dict()


# Also testing more schema validator function
data_to_validate  = yaml_file_handler.get("Eliel")['data']

print(data_to_validate)

if process_data(data_to_validate) != None :print("All right")

if yaml_file_handler.get("config.txt")!= None:
    print("config.txt saved in the private file")
else: print("config.txt wasn't saved")