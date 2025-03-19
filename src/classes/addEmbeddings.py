from pandas import DataFrame
from requests import post
import numpy


class Embeddings:
    def __init__(self, data:DataFrame, arraySize=3072, columnWithLink = 0):
        self.__dataFrame =  data
        self.__array = numpy.zeros(shape=(len(self.__dataFrame), arraySize), dtype='float32')
        if columnWithLink == 0:
            self.Builder()
        else:
            self.Builder2(columnWithLink = columnWithLink)#because python does not implement polymorphism

    def Get(self):
        return self.__array

    def Builder(self, 
                llmUrl="http://localhost:11434/api/embed",
                modelname="nomic-embed-text:latest"
                ):
        '''
        Builder method that generates embedding for each row in self.__dataFrame
        Link is column 0 and all others are considered
        '''
        try:
            for i, row in self.__dataFrame.iterrows():
                if len(self.__dataFrame) > 1:
                    dataStr = ", ".join(map(str, row.tolist()[1:]))
                else:#case of the prompt
                    dataStr = row.to_list()
                
                response = post(url=llmUrl,
                                json={
                                    'model': modelname,
                                    'input': dataStr
                                })
                if response.status_code == 200:
                    responseJson = response.json()
                    if 'embeddings' in responseJson:
                        embedding = responseJson["embeddings"][0]
                        self.__array[i] = numpy.array(embedding)
                else:
                    print(f"Request failed with status: {response.status_code}")
                
        except Exception as ex:
            print(f"Unable to generate embeddings: {ex}")
            raise ex
    
    def Builder2(self,
                columnWithLink,  
                llmUrl="http://localhost:11434/api/embed",
                modelname="nomic-embed-text:latest"
                ):
        '''
        Builder method that generates embedding for the dataself
        Link is column defined in columnWithLink parameter and all columns until the column with link are considered
        '''
        try:
            for i, row in self.__dataFrame.iterrows():
                if len(self.__dataFrame) > 1:
                    dataStr = ", ".join(map(str, row.tolist()[:columnWithLink]))
                else:#case of the prompt
                    dataStr = row.to_list()
                
                response = post(url=llmUrl,
                                json={
                                    'model': modelname,
                                    'input': dataStr
                                })
                if response.status_code == 200:
                    responseJson = response.json()
                    if 'embeddings' in responseJson:
                        embedding = responseJson["embeddings"][0]
                        self.__array[i] = numpy.array(embedding)
                else:
                    print(f"Request failed with status: {response.status_code}")
                
        except Exception as ex:
            print(f"Unable to generate embeddings: {ex}")
            raise ex
        


