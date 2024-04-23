from pydantic import BaseModel, Field, field_validator
from typing import List
import re


class ConvertesInput(BaseModel):
    price: float = Field(gt=0)
    to_currencies: List[str]

    @field_validator('to_currencies')
    def validate_to_currencies(cls, value):
        for currency in value:
            if not re.match('^[A-Z]{3}$', currency):
                raise ValueError(f'Invalid Currency {currency}')
        return value
    

class ConverterOutput(BaseModel):
    message:str
    data: List[dict]