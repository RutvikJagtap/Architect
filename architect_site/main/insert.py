import base64
from pymongo import MongoClient

url = "mongodb+srv://Rutvik07:Rutvik07@cluster0.txxteea.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(url)
db = client['Architect']
portfolio = db["Portfolio"]

# Read and encode the image as base64
with open("static/img/apartment.jpg", "rb") as image_file:
    encoded_string1 = base64.b64encode(image_file.read()).decode('utf-8')

with open("static/img/apartment.jpg", "rb") as image_file:
    encoded_string2 = base64.b64encode(image_file.read()).decode('utf-8')

# Create a document with base64 image
portfolio_data = {
    "name": "Apartment",
    "description": "This is a description of Bungalow And. You successfully connected to MongoDB!",
    "render": encoded_string1,
    "design" : encoded_string2,
    "category" : "Apartment"
}

# Insert into MongoDB
portfolio.insert_one(portfolio_data)
