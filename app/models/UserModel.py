from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum
from sqlalchemy.sql import func
from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import date
from config.database import Base
import enum
import re




class UserType(enum.Enum):
    SA = "SA"
    A = "A"

class OTPStatus(enum.Enum):
    A = "A"
    D = "D"

class PasswordStatus(enum.Enum):
    R = "R"
    U = "U"

class ActiveStatus(enum.Enum):
    A = "A"
    D = "D"
    
class User(Base):
    __tablename__ = 'tbl_user'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    user_name = Column(String, unique=True, index=True)
    mobile_no = Column(String)
    user_email = Column(String, unique=True, index=True)
    email_verified_at = Column(DateTime, default=None, nullable=True)
    user_type = Column(Enum(UserType))
    otp = Column(String, default="000000")
    otp_status = Column(Enum(OTPStatus), default=OTPStatus.D)
    password = Column(String)
    password_status = Column(Enum(PasswordStatus), default=PasswordStatus.U)
    wrong_password_attempts = Column(Integer, default=0)
    active_status = Column(Enum(ActiveStatus), default=ActiveStatus.D)
    created_by = Column(Integer, default=None, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())





class Login(BaseModel):
    user_name: str
    password: str
    
    @field_validator('user_name')
    def validate_username(cls, v):
        # Allow alphanumeric characters, underscores, @, and .
        if not re.match(r'^[\w.@]+$', v):
            raise ValueError('Invalid username format')
        return v


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