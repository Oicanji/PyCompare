from os import listdir
from os.path import isfile, join

from .config import Config
from .extension import Extension
from .consolelog import ConsoleLog

from .csv import Csv
from .pdf import Pdf

class App:
    __compare = {
        ".csv": Csv.compare,
        ".pdf": Pdf.compare
    }

    def run():
        files = [f for f in listdir(Config.FILES) if isfile(join(Config.FILES, f))]

        if not len(files) == 2:
            raise Exception('More or insufficient files')

        pathname1 = join(Config.FILES, files[0])
        pathname2 = join(Config.FILES, files[1])

        if not Extension.compare(pathname1,pathname2):
            raise Exception('Files has extension different')

        if not Extension.is_valid(pathname1):
            raise Exception('This extension not support')

        extension = Extension.get(pathname1)

        comparation = App.__compare[extension]
        result = comparation(pathname1, pathname2)
        result = result.show()

        #Javascript bad joke
        console = ConsoleLog(Config.VERSION, extension)
        console.Log(result)
