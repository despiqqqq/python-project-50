import io
import json
import yaml


def get_data(data: str, extension: str):
    with io.StringIO(data) as file:
        return parse_data(file, extension)


def parse_data(file, extension):
    if extension in (".yml", ".yaml"):
        return yaml.safe_load(file)
    elif extension == ".json":
        return json.load(file)
    else:
        raise ValueError('Filetype is not supported.')
