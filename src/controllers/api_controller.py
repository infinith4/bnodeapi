from openapi_server.models.request_add_address_model import RequestAddAddressModel  # noqa: E501
from openapi_server.models.request_download_from_cloud_model import RequestDownloadFromCloudModel  # noqa: E501
from openapi_server.models.request_mnemonic_model import RequestMnemonicModel  # noqa: E501
from openapi_server.models.request_upload_text_model import RequestUploadTextModel  # noqa: E501
from openapi_server.models.response_add_address_model import ResponseAddAddressModel  # noqa: E501
from openapi_server.models.response_gen_key_model import ResponseGenKeyModel  # noqa: E501
from openapi_server.models.response_get_balance_model import ResponseGetBalanceModel  # noqa: E501
from openapi_server.models.response_mnemonic_model import ResponseMnemonicModel  # noqa: E501
from openapi_server.models.response_tx_model import ResponseTxModel  # noqa: E501
from openapi_server.models.response_upload_model import ResponseUploadModel  # noqa: E501
from openapi_server.models.response_upload_text_model import ResponseUploadTextModel  # noqa: E501
from openapi_server.models.response_upload_to_cloud_model import ResponseUploadToCloudModel  # noqa: E501
from openapi_server import util

from controllers._base_controller import app, templates
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

@app.post(
    "/add-address",
    tags=["api"],
    response_class=JSONResponse)
async def api_addaddress(request: Request):  # noqa: E501
    """search data for added address on bitcoin sv

    search data for added address on Bitcoin SV. # noqa: E501

    :param body: request /api/add-address
    :type body: dict | bytes

    :rtype: ResponseAddAddressModel
    """
    # if connexion.request.is_json:
    #     body = RequestAddAddressModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

@app.get(
    "/add-download",
    tags=["api"],
    response_class=JSONResponse)
def api_download(txid):  # noqa: E501
    """get data for transaction id on Bitcoin SV.

    get data for transaction id on Bitcoin SV. # noqa: E501

    :param txid: bitcoin sv transaction id
    :type txid: str

    :rtype: file
    """
    return 'do some magic!'


def api_download_from_cloud(body=None):  # noqa: E501
    """get data for transaction id on Bitcoin SV.

    download from cloud # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: file
    """
    if connexion.request.is_json:
        body = RequestDownloadFromCloudModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_genkey(typeid):  # noqa: E501
    """Generate Ecies Public Key and Secret Key.

    Generate Ecies Public Key and Secret Key. # noqa: E501

    :param typeid: bitcoin sv address
    :type typeid: str

    :rtype: ResponseGenKeyModel
    """
    return 'do some magic!'


def api_get_balance(addr):  # noqa: E501
    """get balance from address using woc.

    get balance from address using woc. # noqa: E501

    :param addr: bitcoin sv address
    :type addr: str

    :rtype: ResponseGetBalanceModel
    """
    return 'do some magic!'


def api_login(body):  # noqa: E501
    """search data for added address on bitcoin sv

    login # noqa: E501

    :param body: request /api/add-address
    :type body: dict | bytes

    :rtype: ResponseAddAddressModel
    """
    if connexion.request.is_json:
        body = RequestAddAddressModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_mnemonic(body):  # noqa: E501
    """convert mnemonic words to wif, asset on Bitcoin SV.

    convert mnemonic words to wif, asset on Bitcoin SV. # noqa: E501

    :param body: request /api/mnemonic
    :type body: dict | bytes

    :rtype: ResponseMnemonicModel
    """
    if connexion.request.is_json:
        body = RequestMnemonicModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_tx(addr, start_index=None, count=None):  # noqa: E501
    """get transactions.

    get transaction from mongodb. # noqa: E501

    :param addr: bitcoin sv address
    :type addr: str
    :param start_index: start index ( default is 0 )
    :type start_index: int
    :param count: get transaction count ( default is 5 )
    :type count: int

    :rtype: List[ResponseTxModel]
    """
    return 'do some magic!'


def api_upload(body):  # noqa: E501
    """upload file on Bitcoin SV. (100kb)

    convert mnemonic words to wif, asset on Bitcoin SV. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ResponseUploadModel
    """
    if connexion.request.is_json:
        body = InlineObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_upload_text(body):  # noqa: E501
    """upload text data on Bitcoin SV.

    upload text data on Bitcoin SV. # noqa: E501

    :param body: upload text data on Bitcoin SV.
    :type body: dict | bytes

    :rtype: ResponseUploadTextModel
    """
    if connexion.request.is_json:
        body = RequestUploadTextModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_upload_to_cloud(body):  # noqa: E501
    """upload file on Cloud Storage.

    convert mnemonic words to wif, asset on Bitcoin SV. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ResponseUploadToCloudModel
    """
    if connexion.request.is_json:
        body = InlineObjectcloud.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
