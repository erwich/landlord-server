import yaml

with open("config.yml", 'r') as stream:
    try:
        config = (yaml.load(stream))
    except yaml.YAMLError as exc:
        print(exc)