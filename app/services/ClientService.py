from library.date_time_format import get_current_datetime
from library.has_password import get_password_hash
from app.models.ClientModel import ClientModel
from app.models.UserModel import User

from library.date_time_format import get_current_datetime

class ClientService():
    def __init__(self, db) -> None:
        self.db = db
    
    
    def add_client(self, user_credentials,params):
        db_user = User(
            first_name=params.first_name,
            last_name=params.last_name,
            user_name=params.user_name,
            mobile_no=params.mobile_no,
            user_email=params.email,
            email_verified_at=get_current_datetime(),
            user_role="C",
            password=get_password_hash(params.password)
        )
        db_client = ClientModel(
            client_name=params.client_name,
        )
        self.db.add(db_user)
        self.db.add(db_client)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user