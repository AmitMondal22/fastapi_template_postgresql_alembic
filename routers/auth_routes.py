from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


from app.controllers.auth import UserAuthController
from schemas import AuthSchemas
from library.responce import successResponse,errorResponse


auth_routes = APIRouter()


@auth_routes.post('/register')
async def register(user:AuthSchemas.Register):
    try:
        data= await UserAuthController.register(user)
        resdata = successResponse(data, message="Register Success")
        return JSONResponse(status_code=200, content=jsonable_encoder(resdata))
    except HTTPException as he:
        return JSONResponse(status_code=he.status_code, content=jsonable_encoder(errorResponse(message=he.detail)))
    except Exception as e:
        # Handle any other unexpected exceptions
        return JSONResponse(status_code=500, content=jsonable_encoder(errorResponse(message="Internal server error")))
    
    
@auth_routes.post('/login')
async def login(user:AuthSchemas.Login):
    try:
        data= await UserAuthController.login(user)
        resdata = successResponse(data, message="Login Success")
        return JSONResponse(status_code=200, content=jsonable_encoder(resdata))
    except HTTPException as he:
        # Handle HTTPException raised from UserAuthController.login
        return JSONResponse(status_code=he.status_code, content=jsonable_encoder(errorResponse(message=he.detail)))
    except Exception as e:
        # Handle any other unexpected exceptions
        return JSONResponse(status_code=500, content=jsonable_encoder(errorResponse(message="Internal server error")))
    