import os
from pandas import DataFrame
from pandas import read_csv


class GetData:
    PATH_TO_DATA = "hermesMessage.csv"
    PATH_TO_MAPS = "maps.csv"

    @staticmethod
    def Links()-> DataFrame:
        result = None
        try:
            fileName = os.path.join(os.getcwd(), f"resources/{GetData.PATH_TO_DATA}")
            df = read_csv(fileName)
            result = df
        except Exception as ex:
            print(f"Unable to read file: {ex}")
        finally:
            return result
        
    @staticmethod
    def Maps() -> DataFrame:
        retult = None
        try:
            fileName = os.path.join(os.getcwd(), f"resources/{GetData.PATH_TO_MAPS}")
            df = read_csv(fileName)
            result = df
        except Exception as ex:
            print(f"Unable to read file: {ex}")
        finally:
            return result