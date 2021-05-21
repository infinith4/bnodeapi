import polyglot

class BsvDownloadUtil():
    def __init__(self, private_key_wif: str):
        self.uploader = polyglot.Upload(private_key_wif, "test")

    def upload(self, file: bytes, media_type: str = None, encoding: str =None, file_name: str = None):
        #self.uploader.upload_bcat(file, media_type, encoding, file_name)
        #self.uploader.bcat_parts_send_from_binary(file)
        media_type = self.uploader.get_media_type_for_file_name(file_name)
        encoding = self.uploader.get_encoding_for_file_name(file_name)
        print(media_type)
        print(encoding)
        #rawtx = self.uploader.b_create_rawtx_from_binary(file, media_type, encoding, file_name)  ## < 100kb
        rawtx = self.uploader.bcat_parts_send_from_binary(file)  ## < 100kb
        txid = self.uploader.send_rawtx(rawtx)