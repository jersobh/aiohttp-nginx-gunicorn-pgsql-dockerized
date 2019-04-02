from aiohttp import web
from playhouse.shortcuts import model_to_dict, dict_to_model
from json import dumps


async def json(data, status, headers=None):
    response = web.json_response(data, status=status, headers=headers, content_type='application/json')
    return response


async def json_model(data, status, headers=None):
    serialized_data = model_to_dict(data, recurse=True)
    response = web.json_response(serialized_data, status=status, headers=headers, content_type='application/json')
    return response


async def raw_json(data, status, headers=None):
    response = web.Response(text=data, status=status, headers=headers, content_type='application/json')
    return response


async def raw(data, status, headers=None):
    response = web.Response(text=data, status=status, headers=headers, content_type='text/plain')
    return response
