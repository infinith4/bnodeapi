import bitsv
from whatsonchain import api
from openapi_server.models.response_get_balance_model import ResponseGetBalanceModel

class BsvBalanceUtil():
    def __init__(self):
        pass

    @staticmethod
    def get_balance(address: str) -> ResponseGetBalanceModel : 
        woc = api.WhatsonchainTestNet()
        response_get_address = woc.get_balance(address)
        response_get_balance = ResponseGetBalanceModel.from_dict(response_get_address)  # noqa: E501
        return ResponseGetBalanceModel(response_get_balance.confirmed, response_get_balance.unconfirmed).to_dict()
