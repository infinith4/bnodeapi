from typing import Optional, Tuple, List, Type

from fastapi import status

#https://github.com/pistatium/fastapi_error_sample/blob/master/api/main.py

class BaseApiResponseErrorModel(Exception):
    """ エラーの基底となるクラス """
    status_code: int = status.HTTP_400_BAD_REQUEST
    detail: str = 'bad request'  # エラー概要
    def __init__(self, reason: Optional[str] = None):
        if reason:
            self.reason = reason

    def __str__(self):
        return f'{self.detail}\n{self.reason}'

class InvalidFizzBuzzInput(BaseApiResponseErrorModel):
    status_code = 400
    detail = 'input の値が不正です'

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