import requests
 
#using ollama running locally

url = "http://localhost:11434/api/embed"

response = requests.post(url=url,
                         json={
                             'model': 'nomic-embed-text:latest',
                             'input': 'Text to get the embeddings from'
                            }
                         )

if response.status_code == 200:
    messageContent = response.json()
    vector = messageContent["embeddings"]
    print(vector[0])
    print(f"Embedding vector size is {len(vector[0])}")
    #this is the dimension size to use: 3072 with ollama3.2:latest
else:
    print(f"Error {response.status_code}: {response.text}")