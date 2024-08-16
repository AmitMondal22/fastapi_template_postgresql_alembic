from pydantic import BaseModel, EmailStr, Field, field_validator
import re

class AddSuperAdminClient(BaseModel):
    first_name: str = Field(..., pattern=r'^[a-zA-Z]+$', description="First name should contain only alphabetic characters")
    last_name: str = Field(..., pattern=r'^[a-zA-Z]+$', description="Last name should contain only alphabetic characters")
    user_name: str = Field(..., pattern=r'^[a-zA-Z0-9]+$', description="Username should be alphanumeric")
    email: EmailStr
    mobile_no: str = Field(..., pattern=r'^[0-9]{10}$', description="Mobile number should be exactly 10 digits")
    password: str
    city: str
    state: str
    country: str
    
    @field_validator('password')
    def check_password(cls, v):
        forbidden_characters = ["'", "\"", ";", "--"]
        if any(char in v for char in forbidden_characters):
            raise ValueError("Password contains forbidden characters")
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"[0-9]", v):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", v):
            raise ValueError("Password must contain at least one special character")
        return v
