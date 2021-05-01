import polyglot

class BsvUploadUtil():
    def __init__(self, private_key_wif: str):
        self.uploader = polyglot.Upload(private_key_wif, "test")

    def upload(self, file: bytes, media_type: str = None, encoding: str =None, file_name: str = None):
        self.uploader.upload_bcat(file, media_type, encoding, file_name)