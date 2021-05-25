from polyglot.upload import Upload
from io import BytesIO

import polyglot

class BsvUploadUtil():
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
        print(rawtx)

        txid = self.uploader.send_rawtx(rawtx)
        print(txid)
        return txid

wif = "cTqvJoYPXAKUuNWre4B53LDSUQNRq8P6vcRHtrTEnrSSNhUynysF"

uploader = BsvUploadUtil(wif)
file_path : str = "IMG_6855mini.jpg"
file_data = open(file_path, "rb")
contents : bytes = file_data.read()
txid = uploader.upload(contents, media_type="image/jpeg", encoding="binary", file_name=file_path)
print(txid)
# ['cf9dd6c9def26fe88d7936b626e26aa003d221578d17a47b9c091f1dcbabaa10', '14398e32c83c13580d921c1abcec5e2a5cb8f60eabc7e141091c35ac8db245d1']

uploader = Upload(wif)
file_path : str = "IMG_6855mini.jpg"
# txid = uploader.upload_bcat(file_path)
# print(txid)

media_type = uploader.get_media_type_for_file_name(file_path)
encoding = uploader.get_encoding_for_file_name(file_path)
file_name = uploader.get_filename(file_path)
print(media_type)
print(encoding)
print(file_name)
utxos = uploader.get_unspents()
print(utxos)
uploader.get_largest_utxo() #--> largest utxo (for splitting)
uploader.split_biggest_utxo() #--> splits utxo into 100000 satoshi amounts
uploader.filter_utxos_for_bcat() #-- > filters utxos with 0 conf or too low amount to handle a 100kb tx
get_file_ext(file_path) #--> .ext
calculate_txid(rawtx) #--> txid

#rawtx = self.uploader.b_create_rawtx_from_binary(file, media_type, encoding, file_name)  ## < 100kb
file_data = open(file_path, "rb")
print(type(file_data))
# bin = BytesIO(file_data)
# print(type(bin))

rawtx = uploader.bcat_parts_send_from_binary(file_data.read())  ## < 100kb
print(f"rawtx : {rawtx}")
txid = uploader.send_rawtx(rawtx)

print(f"txid : {txid}")