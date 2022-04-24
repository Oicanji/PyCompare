import os

class ConsoleLog:

    def __init__(self, version: str, extension: str):
        self.__extension = extension
        self.__version = version
        self.clear = lambda: os.system('cls')

    def Log(self, message_dict: dict):
        self.clear()

        #title
        print("-"*50)
        print("PYCOMPARE v"+self.__version+" - Compare "+self.__extension.upper()[1:]+" files.")
        print("-"*50)

        #content
        print("\n")
        self.content(message_dict)

        #footer
        print("-"*50)


    def content(self, message_dict: dict):
        #show each attribute in turn
        for key, value in message_dict.items():
            if key == "diff":
                for line in value:
                    print("\nDifferences:")
                    print(" -"+line[0])
                    print(" -"+line[1])
            else:
                print(key+str(value))

            

