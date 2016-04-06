import xlrd
import functools
from itertools import chain


def get_rows(sheet):
    yield from sheet.get_rows()


def get_sheets(work):
    yield from work.sheets()


def save_points(file):
    work_book = xlrd.open_workbook(file)

    sheets = get_sheets(work_book)
    rows = (get_rows(sheet) for sheet in sheets)
    row = chain(*rows)

    for cells in row:
        yield tuple(float(c.value) for c in cells)


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
                raise rise_up(*e.args if not message else (message,))
        return inside
    return wrap
