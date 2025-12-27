from fastapi import FastAPI, UploadFile, File
from typing import List

app = FastAPI(title="Intelligent Gem Analysis API")

@app.get("/")
def root():
    return {"message": "Gem Backend is Running"}

@app.post("/analyze-gem/")
async def analyze_gem(
    gem_type: str,
    gem_color: str,
    images: List[UploadFile] = File(...)
):
    return {
        "gem_type": gem_type,
        "gem_color": gem_color,
        "images_received": len(images),
        "status": "Processing started"
    }
