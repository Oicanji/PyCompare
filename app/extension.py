import os

class Extension:

    __VALID_EXTENSIONS = ['.csv','.pdf','.xlsx','.xls']

    @staticmethod
    def get(pathname: str):
        _, file_extension = os.path.splitext(pathname)
        return file_extension

    @staticmethod
    def compare(pathname1: str, pathname2: str):
        return Extension.get(pathname1) == Extension.get(pathname2)

    @staticmethod
    def is_valid(pathname: str):
        return Extension.get(pathname) in Extension.__VALID_EXTENSIONS
