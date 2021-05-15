# https://github.com/trezor/python-mnemonic

import mnemonic ##pipenv install mnemonic
import hashlib
import hmac
import sys
#from pycoin.key.Key import Key
from pycoin.symbols.btc import network
#from pycoin.ui.key_from_text import key_from_text
import pycoin
from pycoin.symbols.btc import network as BTC
from pycoin.symbols.xtn import network as XTN
from pycoin.encoding.hexbytes import h2b

class Bip39MnemonicUtil(object):
    def __init__(self, mnemonic_words, passphrase="", network_name = 'main'):
        #master = BTC.keys.bip32_seed(mnemonic_words.tobytes())
        #uag = master.subkey(i=0, is_hardened=True, as_private=True)
        #priv = master.hwif(as_private=True)
        seed = mnemonic.Mnemonic.to_seed(mnemonic_words, passphrase)
        #self.masterkey = mnemonic.Mnemonic.to_hd_master_key(seed)

        print(network)
        key = BTC.keys.bip32_seed(seed)
        address = key.address()
        wif = key.wif()
        
        #self.extended_key = self.to_hd_master_key(seed, network_name == 'test')
        #print(self.extended_key)
        self.privatekey_wif = wif
        # master = XTN.keys.bip32_seed(h2b("000102030405060708090a0b0c0d0e0f"))
        # wif = master.hwif(as_private=True)
        # self.node = network.parse.secret(self.extended_key)
        # wif = network.parse.wif
        # #self.node = Key.from_text(self.extended_key)
        # if self.node.is_private():
        #     self.privatekey_wif = self.node.wif()
        # else:
        #     raise ValueError("Your Bip32_Node is not derived from an xprv")

    @classmethod
    def b58encode(self, v):
        alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

        p, acc = 1, 0
        for c in reversed(v):
            if sys.version < "3":
                c = ord(c)
            acc += p * c
            p = p << 8

        string = ""
        while acc:
            acc, idx = divmod(acc, 58)
            string = alphabet[idx : idx + 1] + string
        return string

    @classmethod
    def to_hd_master_key(self, seed, testnet=False):
        if len(seed) != 64:
            raise ValueError("Provided seed should have length of 64")

        # Compute HMAC-SHA512 of seed
        seed = hmac.new(b"Bitcoin seed", seed, digestmod=hashlib.sha512).digest()

        # Serialization format can be found at: https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki#Serialization_format
        xprv = b"\x04\x88\xad\xe4"  # Version for private mainnet
        if testnet:
            xprv = b"\x04\x35\x83\x94"  # Version for private testnet
        xprv += b"\x00" * 9  # Depth, parent fingerprint, and child number
        xprv += seed[32:]  # Chain code
        xprv += b"\x00" + seed[:32]  # Master key

        # Double hash using SHA256
        hashed_xprv = hashlib.sha256(xprv).digest()
        hashed_xprv = hashlib.sha256(hashed_xprv).digest()

        # Append 4 bytes of checksum
        xprv += hashed_xprv[:4]

        return self.b58encode(xprv)