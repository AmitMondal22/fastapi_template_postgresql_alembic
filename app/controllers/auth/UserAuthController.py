from fastapi import HTTPException, Depends
from config.database import SessionLocal
from sqlalchemy.orm import Session
from library.has_password import verify_password
from library.jwt_token import create_access_token

from schemas import AuthSchemas

from app.services.UserService import UserService


db = SessionLocal()

        
        
@staticmethod
async def login(user:AuthSchemas.Login):
    try:
        emailchecked = UserService(db).get_user(user.user_name)
        print(emailchecked)
        if emailchecked is None:
            raise ValueError("Invalid email")
        if emailchecked.user_role.name == "SA":
            if not verify_password(user.password,emailchecked.password):
                raise ValueError("Invalid password")
            else:
                access_token = create_access_token(data={"sub": emailchecked})
                return {"user_data":emailchecked,"token":access_token}
        else:
            raise ValueError("Invalid email")
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    
@staticmethod
async def register(register_data:AuthSchemas.Register):
    try:
        # Create SQLAlchemy model instance
        db_user=UserService(db).create_user(register_data)
        if db_user is None:
            raise ValueError("User not created")
        return db_user
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")