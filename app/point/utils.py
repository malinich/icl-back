import xlrd
import functools


def save_points(file):
    work_book = xlrd.open_workbook(file)

    for sheet in work_book.sheets():
        for row in sheet.get_rows():
            yield tuple(float(cell.value) for cell in row)


def catch_error(*, errors: tuple, rise_up: type(Exception), message: dict):
    """
    catch error inside methods of the class for clean code
    """

    def wrap(fn):
        @functools.wraps(fn)
        def inside(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except errors as e:
                raise rise_up(message)
        return inside
    return wrap
