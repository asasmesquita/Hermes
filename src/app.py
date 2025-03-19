import streamlit
from classes.getData import GetData
from classes.workingWithFiles import WorkingWithFiles
from classes.addEmbeddings import Embeddings
import faiss
from pandas import DataFrame

DIMENSIONS = 768

def main():
    try:
        ########################get data, generate embeddings and vector db with index
        data = GetData.Maps()
        #make index if index.csv does not exist in /resource
        if not WorkingWithFiles.Exists("index.csv"):
            #generate embeddigns for data set
            embed = Embeddings(data=data, arraySize=768, columnWithLink=10).Get()
            #save enbeddigns to index.csv
            WorkingWithFiles.Save(fileName="index.csv", data= embed)
        #get index data
        mapsIndex = WorkingWithFiles.Read("index.csv")
        #vector db with index
        index = faiss.IndexFlatL2(DIMENSIONS)#uses euclidean distance
        #normalize vector
        faiss.normalize_L2(mapsIndex)
        #add normalized index data to vector db
        index.add(mapsIndex)
        ###############################frontend, startup streamlit
        streamlit.title("AGRIVIEW Semantic Search Tool")
        prompt = streamlit.text_area("Insert search terms:")
        if streamlit.button("Search"):
            if prompt:
                with streamlit.spinner("Searching..."):
                    df = DataFrame(data = [prompt], columns = ['prompt'])
                    promptEmbed = Embeddings(data = df, arraySize = DIMENSIONS).Get()
                    faiss.normalize_L2(promptEmbed)
                    #search in index for the 10 closest results
                    distances, indices = index.search(promptEmbed, k = 10)
                    streamlit.subheader("The following links might be related with your search terms:")
                    for i, index in enumerate(indices[0]):
                        distance = distances[0][i]
                        streamlit.write(f"{i+1}: {data['link'][index]}")
    
    except Exception as ex:
        print("An unhandled error as occured on the main app: {ex}")
        raise ex



if __name__ == "__main__":
    main()