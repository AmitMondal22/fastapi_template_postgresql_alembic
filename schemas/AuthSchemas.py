from pydantic import BaseModel, EmailStr, Field, field_validator
import re



class Register(BaseModel):
    first_name: str
    last_name: str
    user_name: str
    mobile_no: str
    email: EmailStr
    password: str
    user_role: str
    
    @field_validator('last_name', 'user_name', 'user_role')
    def check_alphanumeric(cls, v):
        if not v.isalnum():
            raise ValueError(f"{v} must be alphanumeric")
        return v

    @field_validator('mobile_no')
    def check_mobile_number(cls, v):
        if not re.match(r'^[0-9]{10}$', v):
            raise ValueError('Invalid mobile number format')
        return v

    @field_validator('email')
    def check_email(cls, v):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", v):
            raise ValueError('Invalid email format')
        return v

    @field_validator('password')
    def check_password(cls, v):
        forbidden_characters = ["'", "\"", ";", "--"]
        if any(char in v for char in forbidden_characters):
            raise ValueError("Invalid input")
        return v
    
    

class Login(BaseModel):
    user_name: str
    password: str
    
    @field_validator('user_name')
    def validate_username(cls, v):
        # Allow alphanumeric characters, underscores, @, and .
        if not re.match(r'^[\w.@]+$', v):
            raise ValueError('Invalid username format')
        return v


