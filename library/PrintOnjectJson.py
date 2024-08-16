from fastapi.encoders import jsonable_encoder
def print_json(result):
    return jsonable_encoder(result)