from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from services.llama_service import get_llama_response

# Define the router for LLaMA endpoints
llama_router = APIRouter(tags=["LLaMA Chat"])

# Pydantic model for request validation
class ChatRequest(BaseModel):
    message: str
    context: Optional[str] = None  # Optional context for maintaining conversation
    temperature: float = 0.7
    max_tokens: int = 500

class ChatResponse(BaseModel):
    response: str
    context: Optional[str] = None

@llama_router.post("/chat", response_model=ChatResponse, summary="Chat with LLaMA")
async def chat_endpoint(request: ChatRequest):
    """
    Single endpoint for interacting with the LLaMA chat model.
    
    Parameters:
    - `message`: The user's input message
    - `context`: Optional previous conversation context
    - `temperature`: Controls randomness (0.0 - 1.0)
    - `max_tokens`: Maximum length of the response
    """
    if not request.message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    try:
        # Prepare messages list, including context if provided
        messages = []
        if request.context:
            messages.append({
                'role': 'system',
                'content': request.context
            })
        
        messages.append({
            'role': 'user',
            'content': request.message
        })

        # Get response from LLaMA
        response = get_llama_response(
            messages, 
            temperature=request.temperature, 
            max_tokens=request.max_tokens
        )

        # Return response with optional context
        return {
            "response": response,
            "context": request.context  # Can be expanded to return updated context
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))