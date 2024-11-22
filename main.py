from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.llama_controller import llama_router

app = FastAPI(
    title="LLaMA Chat API",
    description="Simple API for chatting with LLaMA",
    version="1.0.0",
    docs_url="/swagger",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Register the router
app.include_router(llama_router, prefix="/api")

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the LLaMA Chat API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True
    )