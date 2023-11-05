import json
import yaml


def get_data(file_path: str):
    with open(file_path, 'r') as file:
        data = file.read()
        extension = '.' + file_path.split(".")[-1]
    return parse_data(data, extension)


def parse_data(data, extension):
    if extension in (".yml", ".yaml"):
        return yaml.safe_load(data)
    elif extension == ".json":
        return json.loads(data)
    else:
        raise ValueError('Тип файла не поддерживается.')
