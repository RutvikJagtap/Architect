
from pymongo import MongoClient

url = "mongodb+srv://Rutvik07:Rutvik07@cluster0.txxteea.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(url)
db = client['Architect']