from fastapi import FastAPI
import dotenv
import os
import requests

dotenv.load_dotenv()
DB_URI = os.getenv("DB_URI")
NAME = os.getenv("NAME")
SOURCE_URL = os.getenv("SOURCE_URL")

app = FastAPI()

@app.get("/test")
def test():

    print(f"DB URI dari env : {DB_URI}")
    return {
        "message" : "Cuma gini aja OI"
    }

@app.get("/source")
def source():
    return {"source": NAME}

@app.get("/data")
def get_data():
    response = requests.get(SOURCE_URL)
    return response.json()