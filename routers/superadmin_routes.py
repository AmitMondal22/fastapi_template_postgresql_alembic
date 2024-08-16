from fastapi import APIRouter, HTTPException,Depends,Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from library.responce import successResponse,errorResponse

# from app.controllers.auper_admin import ClientController

from schemas.superadmin import ClientSchemas

from app.middleware.auth import superAdminMW


superadmin_routes = APIRouter()



@superadmin_routes.post('/client/add',dependencies=[Depends(superAdminMW)])
async def add_client(request: Request,params:ClientSchemas.AddSuperAdminClient):
    try:
        user_credentials = request.state.user
        # data= ClientController.add_client(user_credentials,params)
        data=""
        resdata = successResponse(data, message="Register Success")
        return JSONResponse(status_code=200, content=jsonable_encoder(resdata))
    except HTTPException as he:
        return JSONResponse(status_code=he.status_code, content=jsonable_encoder(errorResponse(message=he.detail)))
    except Exception as e:
        # Handle any other unexpected exceptions
        return JSONResponse(status_code=500, content=jsonable_encoder(errorResponse(message="Internal server error")))