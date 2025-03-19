import os
from numpy import savetxt, array, loadtxt

class WorkingWithFiles:
    @staticmethod
    def Exists(fileName : str) -> bool:
        result = False
        try:
            filePath = os.path.join(os.getcwd(), f"resources/{fileName}")
            if os.path.isfile(filePath):
                result = True
            
        except Exception as ex:
            print(f"Unable to confirm if file named {fileName} exists.")
        finally:
            return result
    
    @staticmethod
    def Save(fileName : str, data : array):
        try:
            filePath = os.path.join(os.getcwd(), f"resources/{fileName}")
            with open(filePath, mode='w', encoding='utf-8') as file:
                #no header as this is only an index
                savetxt(filePath, data, delimiter=',', comments='', encoding='utf-8')

        except Exception as ex:
            print(f"Unable to save {fileName} with data.")
    
    @staticmethod
    def Read(fileName :str)-> array:
        result = None
        try:
            filePath = os.path.join(os.getcwd(), f"resources/{fileName}")
            result = loadtxt(filePath, delimiter=',', dtype='float32')
        except Exception as ex:
            print(f"Unable to read data from {fileName}")
        finally:
            return result