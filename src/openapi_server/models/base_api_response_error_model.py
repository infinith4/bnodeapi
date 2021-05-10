from typing import Optional, Tuple, List, Type

from fastapi import status
from fastapi.responses import JSONResponse

#https://github.com/pistatium/fastapi_error_sample/blob/master/api/main.py

class BaseApiResponseErrorModel(Exception):
    """ エラーの基底となるクラス """
    status_code: int = status.HTTP_400_BAD_REQUEST
    detail: str = 'bad request'  # エラー概要

class InvalidRequestModel(BaseApiResponseErrorModel):
    def __init__(self):
        self.response = JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={})

# error_types に列挙した ApiError を OpenAPI の書式で定義する
def error_response(error_types: List[Type[BaseApiResponseErrorModel]]) -> dict:
    d = {}
    for et in error_types:
        if not d.get(et.status_code):
            d[et.status_code] = {
                'description': f'"{et.detail}"',
                'content': {
                    'application/json': {
                        'example': {
                            'detail': et.detail
                        }
                    }
                }}
        else:
            # 同じステータスコードなら description に追記
            d[et.status_code]['description'] += f'<br>"{et.detail}"'
    return d