from .consolecolor import Colors

class Different:

    def __init__(self):
        self.__lines_diff = []
        self.__num_lines_diff = 0
        self.__is_valid = True
        self.__diff_length = False

    def add(self, line1: str, line2: str):
        self.__is_valid = False
        self.__lines_diff.append((line1, line2))
        self.__num_lines_diff += 1

    def diff_length_lines(self, lines1: int, lines2: int):
        if lines1 != lines2:
            self.__diff_length = True

    def show(self):
        valid = Colors.SUCCESS+"Equals." if self.__is_valid else Colors.DANGER+"Distinct."
        length = Colors.SUCCESS+"No." if not self.__diff_length else Colors.DANGER+"Yes."

        valid += Colors.RESET
        length += Colors.RESET
        
        errors_found = "? "+Colors.SUCCESS+"No." if self.__num_lines_diff == 0 else ": "+Colors.DANGER+str(self.__num_lines_diff)+"."

        return {
            "Everything is the same? R.":valid,
            "There are more lines between them? R.":length,
            "\n"+Colors.DANGER+"Errors found": errors_found,
            "Lines: ":self.__lines_diff,
            "": Colors.RESET
        }
