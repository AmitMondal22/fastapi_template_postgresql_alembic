from fastapi import HTTPException
from config.database import Session
from library.has_password import verify_password
from library.jwt_token import create_access_token

from app.models import UserModel

from app.services.UserService import UserService

db = Session()
@staticmethod
async def login(user:UserModel.Login):
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
async def register(register_data:UserModel.Register):
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