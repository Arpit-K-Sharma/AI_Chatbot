import ollama
from typing import List, Dict

def get_llama_response(
    messages: List[Dict], 
    model: str = 'llama3.2', 
    temperature: float = 0.7,
    max_tokens: int = 500
) -> str:
    """
    Generates a response using the specified LLaMA model.
    
    Args:
    - messages: List of message dictionaries with 'role' and 'content'
    - model: Ollama model to use
    - temperature: Controls randomness of the output
    - max_tokens: Maximum length of the generated response
    
    Returns:
    - Generated text response
    """
    try:
        # Make the chat request with additional parameters
        response = ollama.chat(
            model=model,
            messages=messages,
            options={
                'temperature': temperature,
                'num_predict': max_tokens  # Equivalent to max_tokens
            }
        )
        
        # Extract and return the content
        return response['message']['content']
    
    except Exception as e:
        # Log the error and re-raise
        print(f"Error in LLaMA response: {e}")
        raise