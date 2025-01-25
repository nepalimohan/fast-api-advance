from pydantic import BaseModel, field_validator

class Address(BaseModel):
    street: str
    city: str
    zipcode: str
    

class User(BaseModel):
    id: int
    name: str
    email:str
    address: Address
    
    @field_validator('email')
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("Invalid email")
        return v