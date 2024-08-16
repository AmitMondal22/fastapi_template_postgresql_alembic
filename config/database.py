from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection configuration
database_username = 'postgres'
database_password = 'root'
# database_ip       = 'localhost'  # Assuming your database is running locally
database_ip       = '127.0.0.1'  # Assuming your database is running locally
database_name     = 'cold_storage'
database_port     = 5432         # Default PostgreSQL port

# Update the connection string for PostgreSQL
engine = create_engine(f'postgresql://{database_username}:{database_password}@{database_ip}:{database_port}/{database_name}')

# SQLAlchemy session and base class
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

