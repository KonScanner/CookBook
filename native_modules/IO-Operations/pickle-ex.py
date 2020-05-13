import pickle

my_dict: dict = {'a_0': 0, 'a_1': 1, 'a_2': 1, 'a_3': 2, 'a_4': 3}


def pickle_method(fname: str = 'workfile.pickle', method: str = 'wb', context: str = 'test'):
    """ pickle: mainly used for temporary files, after running long operations, binary store"""
    if method == 'wb':
        return pickle.dump(context, open(fname, method))
    elif method == 'rb':
        return pickle.load(open(fname, method))


pickle_method(context=my_dict)
print(pickle_method(method='rb'))
