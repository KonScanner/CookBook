from xml.etree import ElementTree as ET
import csv
import os


def _add_elem(parent, tag, text='\n', **kwargs):
    elem = ET.Element(tag, **kwargs)
    elem.text, elem.tail = text, text
    if parent is not None:
        parent.append(elem)
    return elem


root = ET.Element('contact_list', status='Private', company='Example, Inc')
root.text, root.tail = '\n', '\n'


with open(os.getcwd()+r'\data\example_data.csv') as f:
    for lname, fname, title, employment_type, email, phone in csv.reader(f):
        employee = _add_elem(root, 'employee')
        _add_elem(employee, 'full_name', f'{fname} {lname}')
        _add_elem(employee, 'job_title', title)
        _add_elem(employee, 'job_type', employment_type)
        _add_elem(employee, 'work_email', email)
        _add_elem(employee, 'work_phone', phone)

ET.dump(root)
