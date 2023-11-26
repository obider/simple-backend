from fastapi import FastAPI, File, UploadFile
import dotenv
import os
import requests

dotenv.load_dotenv()
DB_URI = os.getenv("DB_URI")
NAME = os.getenv("NAME")
SOURCE_URL = os.getenv("SOURCE_URL")

# Define the folder where you want to save the uploaded files
BERKAS_RAHASIA = "berkas_rahasia"
os.makedirs(BERKAS_RAHASIA, exist_ok=True)


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

@app.post("/upload")
def upload_files(file: UploadFile = File(...)):
    file_info = {"filename": file.filename, "content_type": file.content_type}

    # Save the file
    with open(f"{BERKAS_RAHASIA}/{file.filename}", "wb") as f:
        f.write(file.file.read())

    return file_info

@app.get("/list_file")
def list_files():
    return os.listdir(BERKAS_RAHASIA)
    