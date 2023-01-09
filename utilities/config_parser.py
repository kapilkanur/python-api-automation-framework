import yaml
from yaml.loader import SafeLoader

try:
    with open('../config.yaml') as f:
        try:
            cfg = yaml.load(f, Loader=SafeLoader)
            print(cfg)
        except yaml.YAMLError as exc:
            print(exc)
            print("Unable to load the YAML file")
except FileNotFoundError as exc:
    print(exc)
    print("The configuration yaml file does not exist")


def get_base_uri():
    print("The base URI is : " + cfg['base_uri'])
    return cfg['base_uri']
