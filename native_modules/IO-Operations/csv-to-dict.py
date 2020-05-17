import csv
from typing import List


def csv_to_dict(path: str, _newline: str) -> List[dict]:
    """ Opens csv and reads rows one by one as dictionaries.
        Can be easily modified to perform pandas-like read."""
    with open(path, newline=_newline) as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]


# Example Read
for c, i in enumerate(csv_to_dict(path='data/example_data.csv', _newline='')):
    print(f'Index {c} with entry:\n{i}')


def csv_to_dict_w(path: str, _newline: str, d: List[dict], fnames: List[str], _type: str = 'w', header_: bool = True):
    """ Opens csv and writes rows one by one mapped by a list of dictionaries.
        Can be easily modified to perform pandas-like to_csv."""
    with open(path, _type, newline=_newline) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fnames)
        if header_ == True:
            writer.writeheader()
        for c, i in enumerate(d):
            _write_row(dictionary=i, w=writer)


def _write_row(dictionary, w):
    w.writerow(dictionary)


fieldnames = ['first_name', 'last_name']
dicts = [{'first_name': 'Bilbo', 'last_name': 'Baggings'},
         {'first_name': 'Bobba', 'last_name': 'Fett'}]

# Example Write
csv_to_dict_w(path='data/example_data1.csv', _newline='',
              d=dicts, fnames=fieldnames, _type='w', header_=True)
