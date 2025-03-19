
from classes.getData import GetData
from classes.addEmbeddings import Embeddings
import faiss
from pandas import DataFrame


DIMENSIONS = 768 # this is the embedding vector size generated for nomic-embed-text


def main():
    #get data and
    data = GetData.Links()
    #get embeddings fro dataset
    embed = Embeddings(data=data, arraySize=768).Get()
    #vector db that will hold the index and the embeddings generated based on the text of each tuple
    index = faiss.IndexFlatL2(DIMENSIONS)#uses euclidean distance for all vector coordinates
    #normalize vectors
    faiss.normalize_L2(embed)
    #add the normalized embeddings to the vectorDB
    index.add(embed)
    #get user prompt, 
    prompt = "cow products"
    df = DataFrame(data = [prompt], columns = ['prompt'])
    userEmbed = Embeddings(data=df, arraySize=768).Get()
    faiss.normalize_L2(userEmbed)
    #search index
    distances, indices = index.search(userEmbed, k=5)

    for i, index in enumerate(indices[0]):
        distance = distances[0][i]
        print(f"Nearest neighbor {i+1}: {data['link'][index]}, distance {distance}")

















if __name__ == "__main__":
    main()

