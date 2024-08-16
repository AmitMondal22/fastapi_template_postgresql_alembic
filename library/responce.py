def successResponse(data, message="Success")-> dict:
    response = {
        "response_flag":1,
        "status": "success",
        "message": message,
        "data": data
    }
    return response

def errorResponse(message="",data=None) -> dict:
    response = {
        "response_flag": 0,
        "status": "error",
        "message": message,
        "data": data if data is not None else ''
    }
    return response
