from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Union
from model import LLMWrapper

# Initialize FastAPI app
app = FastAPI()

# Initialize LLMWrapper
llm = LLMWrapper()


# Define request and response models
class PipelineRequest(BaseModel):
    name: str
    input_data: Union[str, Dict[str, Any]]
    max_length: int = 142


class PipelineResponse(BaseModel):
    output: Any


# Create an endpoint to run the pipeline
@app.post("/run_pipeline", response_model=PipelineResponse)
def run_pipeline(request: PipelineRequest):
    try:
        output = llm.run_pipeline(request.name, request.input_data)
        return PipelineResponse(output=output)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# Example usage to test the server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
