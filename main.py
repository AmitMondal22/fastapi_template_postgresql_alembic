from fastapi import Depends, FastAPI, Body, HTTPException, Path, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
from json import JSONEncoder
from decimal import Decimal
from datetime import date, datetime, timedelta
import uvicorn
from config.database import SessionLocal, engine, Base


from routers.auth_routes import auth_routes
from routers.superadmin_routes import superadmin_routes

app = FastAPI()
app.title = "Fastapi Template PostgreSQL"
app.version = "0.0.1"
origins = [
    "http://127.0.0.1:8002",
    "http://localhost:8002",
    "*"
]
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(auth_routes, prefix="/api/v1/auth", tags=["authorization"])

app.include_router(superadmin_routes, prefix="/api/v1/superadmin", tags=["superadmin"])



app.get("/")(lambda: {"message": "Welcome to IoTBlitz"})

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    # Run the FastAPI application
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)