# MongoDB
# 
# see https://www.mongodb.com/products/platform/atlas-vector-search
# 
import pymongo
import requests

#  Connecting to MongoDB
client = pymongo.MongoClient("<YOUR_URL>")
db = client.sample_mflix
collection = db.movies

hf_token = "<YOUR_HUGGINGFACE_TOKEN"
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

# Generating embedding using hugging face model
def generate_embedding(text: str) -> list[float]:
    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {hf_token}"},
        json={"inputs": text})

    if response.status_code != 200:
        raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")
    
    return response.json()

# print(generate_embedding("MongoDB is awesome"))

# Create and Store embeddings
for doc in collection.find({'plot':{"$exists": True}}).limit(50):
	doc['plot_embedding_hf'] = generate_embedding(doc['plot'])
	collection.replace_one({'_id': doc['_id']}, doc)
     

# We created the index in the UI


#  Querying the data
query = "imaginary characters from outer space at war"

results = collection.aggregate([
    {
        '$search': {
            "index": "PlotSemanticSearch",
            "knnBeta": {
                "vector": generate_embedding(query),
                "k": 4,
                "path": "plot_embedding_hf"}
        }
    }
])

for document in results:
    print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')
