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
    first_name = Column(String(50))  # Length of 50 characters
    last_name = Column(String(50))   # Length of 50 characters
    user_name = Column(String(30), unique=True, index=True)  # Length of 30 characters
    mobile_no = Column(String(15))   # Length of 15 characters
    user_email = Column(String(100), unique=True, index=True)  # Length of 100 characters
    email_verified_at = Column(DateTime, default=None, nullable=True)
    user_type = Column(Enum(UserType))
    otp = Column(String(6), default="000000")  # Length of 6 characters
    otp_status = Column(Enum(OTPStatus), default=OTPStatus.D)
    password = Column(String(255))  # Length of 255 characters
    password_status = Column(Enum(PasswordStatus), default=PasswordStatus.U)
    wrong_password_attempts = Column(Integer, default=0)
    active_status = Column(Enum(ActiveStatus), default=ActiveStatus.D)
    created_by = Column(Integer, default=None, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())




