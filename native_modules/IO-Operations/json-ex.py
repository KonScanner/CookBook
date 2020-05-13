import json

my_dict: dict = {'a_0': 0, 'a_1': 1, 'a_2': 1, 'a_3': 2, 'a_4': 3}


def json_method(fname: str = 'workfile'+'.json', method: str = 'w', context: str = 'test'):
    """ json: 'dictionary-like' format."""
    with open(fname, method) as f:
        if method == 'w':
            return json.dump(context, f)
        elif method == 'rb':
            return json.load(f)


json_method(context=my_dict)
print(json_method(method='rb'))
