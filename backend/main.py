from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Diet Auto-Cook is running 🚀"}
