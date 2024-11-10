import yaml


def read_config():
    with open('resources/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config