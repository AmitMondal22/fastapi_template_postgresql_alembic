from fastapi import Request, HTTPException,status
from library.jwt_token import verify_token



async def superAdminMW(request: Request):
    try:
        authorization: str = request.headers.get("Authorization")
        if not authorization:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authorization header not provided",
            )
        
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication scheme",
            )
        userdata_list = await verify_token(token)
        # print(userdata_list['user_name'])
        # Check user_type and set user_data in request state
        request.state.user = userdata_list
            
    

    except HTTPException:
        raise  # Re-raise HTTPException to propagate the error response
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error MW")