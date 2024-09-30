from csv_reader import row

def filter_rows_value_equal(rows:list[row], field_name:str, value:str) -> list[row]:
    result:list[row] = []

    for current in rows:
        if current[field_name] == value:
            result.append(current)

    return result

def filter_rows_value_contains(rows:list[row], field_name:str, value:str) -> list[row]:
    result:list[row] = []

    for current in rows:
        if value in current[field_name]:
            result.append(current)

    return result

def filter_rows_value_greater_than(rows:list[row], field_name:str, value:str):
    result:list[row] = []

    for current in rows:
        if current[field_name] > value:
            result.append(current)

    return result

def filter_rows_value_lower_than(rows:list[row], field_name:str, value:str):
    result:list[row] = []

    for current in rows:
        if current[field_name] < value:
            result.append(current)

    return result

def filter_rows_value_greater_equal_than(rows:list[row], field_name:str, value:str):
    result:list[row] = []

    for current in rows:
        if current[field_name] >= value:
            result.append(current)

    return result

def filter_rows_value_lower_equal_than(rows:list[row], field_name:str, value:str):
    result:list[row] = []

    for current in rows:
        if current[field_name] <= value:
            result.append(current)

    return result