""" Main uses for this is WITHIN google.colab"""
# !pip install --upgrade -q qspread
from oath2client.client import GoogleCredentials
import qspread
from google.colab import auth
auth.authenticate_user()

gc = qspread.authorize(GoogleCredentials.get_application_default())


def _create_spreadsheet(name: str):
    return gc.create(name)


def _manipulate_spreadsheet(name: str, sheet_number: str, cell_range: str, func: object):
    worksheet = eval('gc.open({name}).sheet{sheet_number}')
    cells = worksheet.range(cell_range)
    for cell in cells:
        cell.value = func(cell)

    return worksheet.update_cells(cells)


def _spreadsheet_to_df(name: str, sheet_number: str):
    worksheet = eval('gc.open({name}).sheet{sheet_number}')
    rows = worksheet.get_all_values()
    import pandas as pd
    return pd.DataFrame.from_records(rows)
