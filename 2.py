# From YAML
from yaml import load, dump
try:
        from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# Typing imports
from typing import Any, Generic, TypeVar, cast
     
from pathlib import Path

generic_t = TypeVar("generic_t")


# Class to manage files
class YAML_HANDLER(Generic[generic_t]):
    

    def __init__(self) -> None:
        ...
        
    # get dict from path
    def load_file(self, file_path: Path, mode = 'r') ->dict:

        # Check if it is a correct path
        if file_path.exists():

            # Open file and return data as a dict
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
        self.__dict__[name] = {'path': str(path_arg), 'data': self.load_file(path_arg)}
    
    # Getter given key name
    def get(self, name: str) -> dict:
        return self.__dict__[name]
    
    # Save dict in predefined Path for private .yaml file
    def save_dict(self) -> None:
        self.write_file(self.__dict__, self.__file_path__)

# Data a escribir
datos = {
    'nombre': 'Usuario',
    'edad': 30,
    'habilidades': ['Python', 'YAML']
}
datos['new'] = 'nuevo'

yaml_file_handler = YAML_FILE_HANDLER()


load_file: dict = yaml_file_handler.load_file(Path("config.yaml"))
#yami_handler.write_file(datos, Path("config.txt"))
#print(load_file)
#if file_path.exists(): print("Valid file")
#if Path("confg.txt").exists(): print("Valid file")
#else: print("invalid file")

yaml_file_handler.add_stream(Path("config.yaml"), "config.yaml")
yaml_file_handler.add_stream(Path("config.txt"), "config.txt")

print(yaml_file_handler.get("config.yaml"))

yaml_file_handler.save_dict()

