from fastapi import FastAPI
import dotenv
import os
dotenv.load_dotenv()
DB_HOST = os.getenv("DB_HOST")


app = FastAPI()

@app.get("/test")
def test():
    print(f"Envi variable nih : {DB_HOST}")
    return {
        "message" : "Cuma gini aja woi"
    }