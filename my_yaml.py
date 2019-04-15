import yaml


def write_to_yaml():
    with open('write.yaml', 'w') as file:
        yaml.dump(a, file)

    with open('write.yaml') as file:
        print(file.read().encode('utf-8'))


a = {'первый': [1,2,3], 'второй': 3, 'третий': {'1': '€'}}
b = write_to_yaml()

