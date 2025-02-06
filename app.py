from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Enable CORS to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change for security)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve index.html from the frontend directory
@app.get("/")
def serve_index():
    return FileResponse("index.html")

# Sample API endpoint
@app.get("/pipeline_status")
def get_pipeline_status():
    return {"status": "Pipeline is running", "last_run": "2025-02-06 10:30 AM"}

# Run with: uvicorn app:app --reload
