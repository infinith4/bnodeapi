from openapi_server.models.request_add_address_model import RequestAddAddressModel  # noqa: E501
from openapi_server.models.request_download_from_cloud_model import RequestDownloadFromCloudModel  # noqa: E501
from openapi_server.models.request_mnemonic_model import RequestMnemonicModel  # noqa: E501
from openapi_server.models.request_upload_model import RequestUploadModel  # noqa: E501
from openapi_server.models.request_upload_text_model import RequestUploadTextModel  # noqa: E501
from openapi_server.models.request_login_model import RequestLoginModel  # noqa: E501

from openapi_server.models.base_api_response_error_model import BaseApiResponseErrorModel, error_response, InvalidRequestModel
from openapi_server.models.response_add_address_model import ResponseAddAddressModel  # noqa: E501
from openapi_server.models.response_gen_key_model import ResponseGenKeyModel  # noqa: E501
from openapi_server.models.response_get_balance_model import ResponseGetBalanceModel  # noqa: E501
from openapi_server.models.response_mnemonic_model import ResponseMnemonicModel  # noqa: E501
from openapi_server.models.response_tx_model import ResponseTxModel  # noqa: E501
from openapi_server.models.response_upload_model import ResponseUploadModel  # noqa: E501
from openapi_server.models.response_upload_text_model import ResponseUploadTextModel  # noqa: E501
from openapi_server.models.response_upload_to_cloud_model import ResponseUploadToCloudModel  # noqa: E501
from openapi_server.models.response_login_model import ResponseLoginModel  # noqa: E501
from openapi_server import util

from controllers._base_controller import app, templates
from fastapi import FastAPI, Request, Form, UploadFile, File, status
from fastapi.responses import JSONResponse

from utils.upload_util.bsv_upload_util import BsvUploadUtil
from utils.crypt_util import CryptUtil
from utils.bsv_balance_util import BsvBalanceUtil
from utils.bsv_tx_util import BsvTxUtil
from utils.bsv_mnemonic_util import BsvMnemonicUtil

@app.post(
    "/api/add-address",
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
    "/api/download",
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


# def api_download_from_cloud(body=None):  # noqa: E501
#     """get data for transaction id on Bitcoin SV.

#     download from cloud # noqa: E501

#     :param body: 
#     :type body: dict | bytes

#     :rtype: file
#     """
#     # if connexion.request.is_json:
#     #     body = RequestDownloadFromCloudModel.from_dict(connexion.request.get_json())  # noqa: E501
#     return 'do some magic!'

@app.get(
    "/api/genkey",
    tags=["api"],
    response_class=JSONResponse,
    responses=error_response([BaseApiResponseErrorModel, InvalidRequestModel])
    #     200: {
    #     "public_key_hex": "0xe5************",
    #     "secret_key_hex": "0x45************"
    #     },
    #     400: {}
    # },
    )
def api_genkey(typeid):  # noqa: E501
    """Generate Ecies Public Key and Secret Key.

    Generate Ecies Public Key and Secret Key. # noqa: E501

    :param typeid: bitcoin sv address
    :type typeid: str

    :rtype: ResponseGenKeyModel
    """
    #return 'do some magic!'
    if typeid == 'ecies':
        cryptUtil = CryptUtil()
        ec_key = cryptUtil.generateEciesKey()
        secret_key_hex = ec_key.to_hex()
        public_key_hex = ec_key.public_key.to_hex()

        return JSONResponse(status_code=status.HTTP_200_OK, content=ResponseGenKeyModel(secret_key_hex, public_key_hex).to_dict())
    else:
        invalid_request = InvalidRequestModel()
        return invalid_request.response

@app.get(
    "/api/get-balance",
    tags=["api"],
    response_class=JSONResponse,
    responses=error_response([BaseApiResponseErrorModel, InvalidRequestModel]))
def api_get_balance(addr):  # noqa: E501
    """get balance from address using woc.

    get balance from address using woc. # noqa: E501

    :param addr: bitcoin sv address
    :type addr: str

    :rtype: ResponseGetBalanceModel
    """
    try:
        return BsvBalanceUtil.get_balance(addr)
    except Exception as e:
        invalid_request = InvalidRequestModel()
        return invalid_request.response

@app.post(
    "/api/login",
    tags=["api"],
    response_class=JSONResponse,
    response_model=ResponseLoginModel)
def api_login(loginUser: RequestLoginModel):  # noqa: E501
    """search data for added address on bitcoin sv

    login # noqa: E501

    :param body: request /api/login
    :type body: dict | bytes

    :rtype: ResponseAddAddressModel
    """
    # if connexion.request.is_json:
    #     body = RequestAddAddressModel.from_dict(connexion.request.get_json())  # noqa: E501
    return ResponseLoginModel(200)

@app.get(
    "/api/mnemonic",
    tags=["api"],
    response_class=JSONResponse,
    responses=error_response([BaseApiResponseErrorModel, InvalidRequestModel])
    )
def api_mnemonic(mnemonic: str):  # noqa: E501
    """convert mnemonic words to wif, asset on Bitcoin SV.

    convert mnemonic words to wif, asset on Bitcoin SV. # noqa: E501

    :param body: request /api/mnemonic
    :type body: dict | bytes

    :rtype: ResponseMnemonicModel
    """
    # if connexion.request.is_json:
    #     body = RequestMnemonicModel.from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'
    try:
        #app.app.logger.info("start /api/mnemonic")
        # if connexion.request.is_json:
        #     body = RequestMnemonicModel.from_dict(connexion.request.get_json())  # noqa: E501
        return BsvMnemonicUtil.get_mnemonic(mnemonic)
    except Exception as e:
        print(e)
        invalid_request = InvalidRequestModel()
        return invalid_request.response

@app.get(
    "/api/tx",
    tags=["api"],
    response_class=JSONResponse)
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
    txt_on_chain = BsvTxUtil.get_txt_on_chain()
    return 'do some magic!'

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

#curl -X POST "http://localhost:8000/uploadfile" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "file=@IMG_6855.jpeg;type=image/jpeg"

@app.post("/api/uploadfile",
    tags=["api"],
    response_class=JSONResponse)
async def create_upload_file(upload_file: UploadFile = File(...)):
    private_key_wif = ""
    uploader = BsvUploadUtil(private_key_wif)
    contents = await upload_file.read()
    uploader.upload("", media_type="image/jpeg", encoding="binary", file_name=upload_file.filename)
    return {"file": upload_file}

@app.post(
    "/upload")
async def api_upload(upload_file: UploadFile = Form(...)):  # noqa: E501

    #print(request.body)
    """upload file on Bitcoin SV. (100kb)

    convert mnemonic words to wif, asset on Bitcoin SV. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ResponseUploadModel
    """
    # if connexion.request.is_json:
    #     body = InlineObject.from_dict(connexion.request.get_json())  # noqa: E501
    #curl -X POST "http://localhost:8000/api/upload" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "file=@test_image/IMG_6855.jpeg;type=image/jpeg"
    # private_key_wif = "cTqvJoYPXAKUuNWre4B53LDSUQNRq8P6vcRHtrTEnrSSNhUynysF"
    # uploader = BsvUploadUtil(private_key_wif)
    # uploader.upload(upload_file)
    return {"file": upload_file}

@app.post(
    "/api/upload_text",
    tags=["api"],
    response_class=JSONResponse)
def api_upload_text(body):  # noqa: E501
    """upload text data on Bitcoin SV.

    upload text data on Bitcoin SV. # noqa: E501

    :param body: upload text data on Bitcoin SV.
    :type body: dict | bytes

    :rtype: ResponseUploadTextModel
    """
    # if connexion.request.is_json:
    #     body = RequestUploadTextModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


# def api_upload_to_cloud(body):  # noqa: E501
#     """upload file on Cloud Storage.

#     convert mnemonic words to wif, asset on Bitcoin SV. # noqa: E501

#     :param body: 
#     :type body: dict | bytes

#     :rtype: ResponseUploadToCloudModel
#     """
#     # if connexion.request.is_json:
#     #     body = InlineObjectcloud.from_dict(connexion.request.get_json())  # noqa: E501
#     return 'do some magic!'
