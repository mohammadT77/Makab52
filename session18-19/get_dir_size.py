import os
from typing import Literal


def convert_unit(unit: Literal['B', 'KB', 'MB', 'GB']):
    def inner(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if unit == 'B':
                pass
            elif unit == 'KB':
                res = res // 1024
            elif unit == 'MB':
                res = res // 1024 ** 2
            elif unit == 'GB':
                res = res // 1024 ** 3
            else:
                raise Exception("Invalid unit.")

            return res

        return wrapper

    return inner


@convert_unit('KB')
def get_directory_size(directory):
    """Returns the `directory` size in bytes."""
    total = 0
    try:
        for entry in os.scandir(directory):
            if entry.is_file():
                # if it's a file, use stat() function
                total += entry.stat().st_size
            elif entry.is_dir():
                # if it's a directory, recursively call this function
                total += get_directory_size(entry.path)
    except NotADirectoryError:
        # if `directory` isn't a directory, get the file size then
        return os.path.getsize(directory)
    except PermissionError:
        # if for whatever reason we can't open the folder, return 0
        return 0
    return total


if __name__ == '__main__':
    print(get_directory_size(os.getcwd()))
