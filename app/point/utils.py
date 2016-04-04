import xlrd


def save_points(file):
    work_book = xlrd.open_workbook(file)

    for sheet in work_book.sheets():
        for row in sheet.get_rows():
            yield tuple(float(cell.value) for cell in row)
