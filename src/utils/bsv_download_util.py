import requests
import binascii
from fastapi.responses import StreamingResponse
from libs.models.response_download import ResponseDownload

class BsvDownloadUtil():
    def __init__(self):
        pass

    @staticmethod
    def download(txid, network_name = "test") -> StreamingResponse:
        url = f"https://api.whatsonchain.com/v1/bsv/{network_name}/tx/hash/{txid}"
        headers = {"content-type": "application/json"}
        r = requests.get(url, headers=headers)
        data = r.json()
        op_return = data['vout'][0]['scriptPubKey']['opReturn']
        # たぶん、upload_asm.split()[3] は100KB 未満のときに利用
        # data['vout'][0]['scriptPubKey']['hex'] は 100KB
        upload_asm = data['vout'][0]['scriptPubKey']['asm']
        upload_data = data['vout'][0]['scriptPubKey']['hex'] #upload_asm.split()[3] ##uploaddata (charactor)
        #print(upload_data)
        upload_charset : str = ""
        upload_filename : str = "test"
        upload_mimetype : str = "image/jpeg"
        if(op_return['parts'] != None and len(op_return['parts']) > 2):
            upload_mimetype = op_return['parts'][1] ##MEDIA_Type:  image/png, image/jpeg, text/plain, text/html, text/css, text/javascript, application/pdf, audio/mp3
            upload_charset = op_return['parts'][2] ##ENCODING: binary, utf-8 (Definition polyglot/upload.py)
            upload_filename = op_return['parts'][3] ##filename
            print("upload_mimetype: " + upload_mimetype)
            print("upload_charset: " + upload_charset)
            print("upload_filename: " + upload_filename)
        if upload_charset == "" or upload_charset == 'binary':  #47f0706cdef805761a975d4af2a418c45580d21d4d653e8410537a3de1b1aa4b
            #print(binascii.hexlify(upload_data))
            data = binascii.unhexlify(upload_data)
        elif upload_charset == 'utf-8':  #cc80675a9a64db116c004b79d22756d824b16d485990a7dfdf46d4a183b752b2
            data = op_return['parts'][0]
        else:
            print('upload_charset' + upload_charset)
            data = ''
        downloadFilename = upload_filename
        #headers["Content-Disposition"] = 'attachment; filename=' + downloadFilename
        header_ContentDisposition = 'attachment; filename=' + downloadFilename
        mimetype = upload_mimetype
        
        # response = app.app.make_response(data)
        # response.data = data
        # response.headers["Content-Disposition"] = header_ContentDisposition
        # response.mimetype = mimetype
        headers : dict = {"Content-Disposition": header_ContentDisposition}
        return ResponseDownload(txid, data, mimetype, upload_charset, downloadFilename)