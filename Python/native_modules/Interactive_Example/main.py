import os
import sys
import calendar
import re

months = [i.lower() for i in calendar.month_abbr][1:]


def name_changer(directory_name: str = dir_name):
    """Filename is expected to be in the form 'data-DD-MMM-YY.txt'."""
    regex = r"([A-Za-z0-9]+)\w+"  # to match file details
    for filename in os.listdir(dir_name):
        if [match.group(0) for matchNum, match in enumerate(
                re.finditer(r"(.txt)", filename, re.MULTILINE), start=1)][0] in filename:

            match = [match.group(0) for matchNum, match in enumerate(
                re.finditer(regex, filename, re.MULTILINE), start=1)]

            d, month, y = int(match[1]), match[2], int(match[3])
            m = months.index(month.lower()) + 1

            newname = '{}-20{:02d}-{:02d}-{:02d}.txt'.format(match[0], y, m, d)

            newpath = os.path.join(dir_name, newname)
            oldpath = os.path.join(dir_name, filename)

            print(f'{oldpath}->{newpath}')
            os.rename(oldpath, newpath)


if __name__ == "__main__":
    dir_name = str(sys.argv[1])
    if dir_name is None:
        print('Assumed dir_name == \'data\':')
        name_changer(directory_name=str(os.getcwd()) + r'\data')
    else:
        print(f'Using directory path {dir_name}')
        name_changer(directory_name=dir_name)
