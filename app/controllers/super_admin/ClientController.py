from fastapi import HTTPException
from config.database import Session
from app.services.ClientService import ClientService

db = Session()
async def add_client(user_credentials,params):
    try:
        # Create SQLAlchemy model instance
        db_user=ClientService(db).add_client(user_credentials,params)
        if db_user is None:
            raise ValueError("User not created")
        return db_user
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")