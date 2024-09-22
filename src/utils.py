from csv_reader import row

def get_all_values_from_column(rows:list[row], column_name:str) -> list[str]:
    result:list[str] = []

    for r in rows:
        result.append(r[column_name])

    # drop duplicates
    result = list(set(result))
    result = sorted(result)

    return result
