from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import uvicorn

app = FastAPI(
    title="Nginx Demo API",
    description="A demo FastAPI backend for the nginx web app",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class HealthResponse(BaseModel):
    status: str
    message: str
    version: str

class MessageRequest(BaseModel):
    message: str

class MessageResponse(BaseModel):
    original_message: str
    processed_message: str
    timestamp: str

@app.get("/")
async def root():
    return {"message": "Welcome to Nginx Demo API"}

@app.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="healthy",
        message="FastAPI backend is running smoothly",
        version="1.0.0"
    )

@app.get("/api/health", response_model=HealthResponse)
async def api_health_check():
    return HealthResponse(
        status="healthy",
        message="API endpoint is working",
        version="1.0.0"
    )

@app.post("/api/process", response_model=MessageResponse)
async def process_message(request: MessageRequest):
    processed = f"Processed: {request.message.upper()}"
    timestamp = datetime.now().isoformat()
    
    return MessageResponse(
        original_message=request.message,
        processed_message=processed,
        timestamp=timestamp
    )

@app.get("/api/info")
async def get_info():
    return {
        "app_name": "Nginx Demo API",
        "framework": "FastAPI",
        "python_version": "3.11+",
        "features": [
            "RESTful API",
            "CORS enabled",
            "Pydantic validation",
            "OpenAPI documentation",
            "Docker ready"
        ],
        "endpoints": [
            "GET /health",
            "GET /api/health", 
            "POST /api/process",
            "GET /api/info"
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)