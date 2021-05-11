import bitsv
from whatsonchain import api
from openapi_server.models.response_get_balance_model import ResponseGetBalanceModel

class BsvBalanceUtil():
    def __init__(self):
        pass

    @staticmethod
    def get_balance(address: str) -> ResponseGetBalanceModel : 
        try:
            woc = api.WhatsonchainTestNet()
            response_get_address = woc.get_balance(address)
            responseGetBalance = ResponseGetBalanceModel.from_dict(response_get_address)  # noqa: E501
            return ResponseGetBalanceModel(0, responseGetBalance.confirmed, responseGetBalance.unconfirmed)
        except Exception as e:
            return ResponseGetBalanceModel()