from .different import Different

class Csv:

    @staticmethod
    def compare(pathname1: str, pathname2: str):
        error_data = Different()

        with open(pathname1, 'r') as file1, open(pathname2, 'r') as file2:
            fileone = file1.readlines()
            filetwo = file2.readlines()
            line_1 = 0
            line_2 = 0

            error_data.diff_length_lines(len(fileone),len(filetwo))
            
            #compare line by line
            for line1, line2 in zip(fileone, filetwo):
                line_1 += 1
                line_2 += 1
                if line1 != line2:
                    error_data.add(line1, line2)

        return error_data
