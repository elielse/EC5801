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

class YAMI_HANDLER(Generic[generic_t]):
    

    def __init__(self) -> None:
        ...
        

    def load_file(self, file_path: Path, mode = 'r'):
        if file_path.exists():
            with file_path.open(mode) as config:
                config_data = load(config, Loader=Loader)
                #print(config_data)
                return config_data

    def write_file(self, datos, file_path: Path, mode = 'w'):
        if file_path.exists():
            with file_path.open(mode) as config:
                dump(datos, config, default_flow_style=False)

# Data a escribir
datos = {
    'nombre': 'Usuario',
    'edad': 30,
    'habilidades': ['Python', 'YAML']
}

yami_handler = YAMI_HANDLER()

datos = {
    'nombre': 'Usuario',
    'edad': 30,
    'habilidades': ['Python', 'YAML']
}



load_file: dict = yami_handler.load_file(Path("config.yaml"))
yami_handler.write_file(datos, Path("config.txt"))
print(load_file)
#if file_path.exists(): print("Valid file")
#if Path("confg.txt").exists(): print("Valid file")
#else: print("invalid file")


