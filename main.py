from fastapi import FastAPI
import dotenv
import os

dotenv.load_dotenv()
DB_URI = os.getenv("DB_URI")

app = FastAPI()

@app.get("/test")
def test():

    print(f"DB URI dari env : {DB_URI}")
    return {
        "message" : "Cuma gini aja OI"
    }