import bitsv
from whatsonchain import api

from utils.mnemonic.bip39_mnemonic_util import Bip39MnemonicUtil

from openapi_server.models.response_mnemonic_model import ResponseMnemonicModel

class BsvMnemonicUtil():
    def __init__(self):
        pass
    
    @staticmethod
    def get_mnemonic(mnemonic) -> ResponseMnemonicModel :
        bip39MnemonicUtil = Bip39MnemonicUtil(mnemonic, passphrase="", network="test")
        privateKey = bitsv.Key(bip39MnemonicUtil.privatekey_wif, network = 'test')
        address = privateKey.address
        balance_satoshi = privateKey.get_balance()
        #balance_bsv = float(balance_satoshi) / float(100000000)
            # html = render_template(
            #     'mnemonic.html',
            #     privatekey_wif = bip39Mnemonic.privatekey_wif,
            #     address = address,
            #     balance_satoshi = balance_satoshi,
            #     balance_bsv = balance_bsv,
            #     title="mnemonic")
        return ResponseMnemonicModel(bip39MnemonicUtil.privatekey_wif, address, balance_satoshi).to_dict()