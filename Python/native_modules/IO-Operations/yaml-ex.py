import yaml


my_dict: dict = {'a_0': 0, 'a_1': 1, 'a_2': 1, 'a_3': 2, 'a_4': 3}


def yaml_method(fname: str = 'workfile'+'.yaml', method: str = 'w', context: str = 'test'):
    """ yaml: sort of operates like json, but is more humanly readable."""
    with open(fname, method) as f:
        if method == 'w':
            return yaml.safe_dump(context, f, default_flow_style=False)
        elif method == 'rb':
            return yaml.safe_load(f)


yaml_method(context=my_dict)
print(yaml_method(method='rb'))
