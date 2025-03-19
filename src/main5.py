
from classes.getData import GetData
from classes.addEmbeddings import Embeddings
from classes.workingWithFiles import WorkingWithFiles
import faiss
from pandas import DataFrame


DIMENSIONS = 768 # this is the embedding vector size generated for nomic-embed-text


def main():
    #get data
    data = GetData.Maps()
    #only generate index if ..resource/index.csv is not existent
    if not WorkingWithFiles.Exists("index.csv"):
        #get embeddings for dataset
        embed = Embeddings(data=data, arraySize=768, columnWithLink=5).Get()
        #save embeddings to index.csv
        WorkingWithFiles.Save(fileName="index.csv", data= embed)
    #get index data
    mapIndex = WorkingWithFiles.Read("index.csv")
    #vector db that will hold the index and the embeddings generated based on the text of each tuple
    index = faiss.IndexFlatL2(DIMENSIONS)#uses euclidean distance for all vector coordinates
    #normalize vectors
    faiss.normalize_L2(mapIndex)
    #add the normalized embeddings to the vectorDB
    index.add(mapIndex)
    #get user prompt, 
    prompt = "red wine portugal"
    df = DataFrame(data = [prompt], columns = ['prompt'])
    userEmbed = Embeddings(data=df, arraySize=768).Get()
    faiss.normalize_L2(userEmbed)
    #search index
    distances, indices = index.search(userEmbed, k=5)

    for i, index in enumerate(indices[0]):
        distance = distances[0][i]
        print(f"Nearest neighbour {i+1}: {data['link'][index]}, distance {distance}")

















if __name__ == "__main__":
    main()

