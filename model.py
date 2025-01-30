from transformers import pipeline
from pydantic import BaseModel, Field
from typing import Dict, Union, Any


class LLMWrapper(BaseModel):
    pipelines: Dict[str, Any] = Field(default_factory=dict)

    def __init__(self, **data):
        super().__init__(**data)
        # Initialize pipelines with models
        self.pipelines["summarization"] = pipeline(
            "summarization", model="facebook/bart-large-cnn", device=-1
        )
        self.pipelines["text-classification"] = pipeline(
            "text-classification",
            model="nlptown/bert-base-multilingual-uncased-sentiment",
            device=-1,
        )
        self.pipelines["translation"] = pipeline(
            "translation", model="Helsinki-NLP/opus-mt-en-fr", device=-1
        )

    def run_pipeline(self, name: str, input_data: Union[str, Dict[str, Any]]) -> Any:
        """Run a pipeline by name with input data."""
        if name not in self.pipelines:
            raise ValueError(f"Pipeline '{name}' is not available.")
        return self.pipelines[name](input_data)


if __name__ == "__main__":
    llm = LLMWrapper()
