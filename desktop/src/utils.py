from csv_reader import row
import sys
from os import path

def get_resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = path.dirname(__file__)

    return path.join(base_path, relative_path)

def get_all_values_from_column(rows:list[row], column_name:str) -> list[str]:
    result:list[str] = []

    for r in rows:
        result.append(r[column_name])

    # drop duplicates
    result = list(set(result))
    result = sorted(result)

    return result
