from pydantic import BaseModel, ValidationError, field_validator
from typing import Dict
import json
import os


class WebPage(BaseModel):
    """Pydantic model for webpage data validation"""
    url: str
    university: str
    title: str
    section: str
    content: str
    metadata: Dict
    
    @field_validator('content')
    @classmethod
    def content_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Content cannot be empty')
        return v


def validate_data(data, output_path="data/invalid_records.json"):
    """
    Validate scraped data using Pydantic.
    
    Args:
        data: List of scraped data dictionaries
        output_path: Path to save invalid records
        
    Returns:
        List of validated data dictionaries
    """
    valid_data = []
    invalid_data = []

    for item in data:
        try:
            validated = WebPage(**item)
            valid_data.append(validated.model_dump())
        except ValidationError as e:
            invalid_data.append({
                "error": str(e),
                "data": item
            })

    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save invalid records
    with open(output_path, "w") as f:
        json.dump(invalid_data, f, indent=4)

    print(f"✓ Validated {len(valid_data)} records")
    print(f"✗ Found {len(invalid_data)} invalid records (saved to {output_path})")

    return valid_data