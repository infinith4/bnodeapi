import polyglot
import bitsv
from io import BytesIO

from polyglot.upload import Upload
from PIL import Image

import gzip

from bitsv.network import NetworkAPI
# [PREFIXES]
B = '19HxigV4QyBv3tHpQVcUEQyq1pzZVdoAut'  # https://b.bitdb.network/
C = '19HxigV4QyBv3tHpQVcUEQyq1pzZVdoAut'  # https://c.bitdb.network/ --> writing to blockchain is same as B://
BCAT = '15DHFxWZJT58f9nhyGnsRBqrgwK4W6h4Up'  # https://bcat.bico.media/
BCATPART = '1ChDHzdd1H4wSjgGMHyndZm6qxEDGjqpJL'  # https://bcat.bico.media/ (raw data only after prefix)
D = '19iG3WTYSsbyos3uJ733yK4zEioi1FesNU'  # Dynamic - ownership over state of address
AIP = '15PciHG22SNLQJXMoSUaWVi7WSqc7hCfva'  # https://github.com/BitcoinFiles/AUTHOR_IDENTITY_PROTOCOL
MAP = '1PuQa7K62MiKCtssSLKy1kh56WWU7MtUR5'  # MAP protocol.

class Download(NetworkAPI):
    @staticmethod
    def do_download(txid : str) -> dict:
        print(f"txid : {txid}")
        dl = Download("test")
        #data_dict : dict = dl.bcat_fields_from_txid(txid)
        scripts = dl.scripts_from_txid(txid)
        #print(scripts)
        data = dl.pushdata_from_script(scripts[0])
        #print(data)
        decodezero = data[0].decode('utf-8')
        print(f"decodezero : {decodezero}")
        decodeone = data[1].decode('utf-8')
        print(f"decodeone : {decodeone}")
        detectfields = dl.bcat_linker_detect_from_pushdata(data)
        print(f"detectfields : {detectfields}")
        subfields = dl.bcat_linker_fields_from_pushdata(data)
        print(f"subfields : {subfields}")
        part_binary = dl.bcat_part_binary_from_pushdata(data)
        #print(f"part_binary : {part_binary}")
        
        fields = dl.bcat_linker_fields_from_txid(txid)
        print(f"fields : {fields}")
        
        data_dict = {}
        try:
            data_dict = dl.download_bcat(txid, "test", False)
        except Exception as e:
            pass
        return data_dict

    def do_download_txids(txids):
        dl = Download("test")
        data = dl.bcat_binary_from_txids(txids)
        img = Image.open(BytesIO(data))
        img.save("write_jpg1.jpg")
        # fw = open("write_jpg.jpg", "wb")

        # while True:
        #     if(len(data) == 0):
        #         break

        #     fw.write(data)
        # fw.close()


    def __init__(self, network='main'):
        super().__init__(network=network)

    # UTILITIES
    @staticmethod
    def binary_to_file(binary, file):
        """Give the pathname to a file
        makes needed subdirectories and writes binary to it
        Example path (for newer users): "C://Users/username/Pictures/my_picture.jpg etc."
        """
        os.makedirs(os.path.dirname(file), exist_ok=True)
        with open(file, 'wb') as f:
            f.write(binary)

    @staticmethod
    def hex_to_binary(hex):
        # FIXME - may not just work for any file
        return bytes.fromhex(hex)

    def scripts_from_txid(self, txid):
        lst = []
        tx = self.get_transaction(txid)
        for output in tx.outputs:
            lst.append(output.scriptpubkey)
        return lst

    @staticmethod
    def binary_to_bsv_string(binary):
        string = binary.decode('utf-8')
        if string in ('\0','\t','\n','\x0B','\r',' ',''):
            string = None
        return string

    @staticmethod
    def pushdata_from_script(script):
        script = Download.hex_to_binary(script)
        offset = 0
        data = []
        while offset < len(script):
            opcode = script[offset]
            offset += 1
            if opcode == 0x00: # OP_0, OP_FALSE
                data.append(bytes(0))
            elif opcode <= 0x4b: # short data
                data.append(script[offset : offset + opcode])
                offset += opcode
            elif opcode == 0x4c: # OP_PUSHDATA1
                length = script[offset]
                data.append(script[offset + 1 : offset + 1 + length])
                offset += 1 + length
            elif opcode == 0x4d: # OP_PUSHDATA2
                length = script[offset] + script[offset + 1] * 0x100
                data.append(script[offset + 2 : offset + 2 + length])
                offset += 2 + length
            elif opcode == 0x4e: # OP_PUSHDATA4
                length = script[offset] + script[offset + 1] * 0x100 + script[offset + 2] * 0x10000 + script[offset + 3] * 0x1000000
                data.append(script[offset + 4 : offset + 4 + length])
                offset += 4 + length
            elif opcode == 0x4f: # OP_1NEGATE
                data.append(bytes([0xff])) # -1 is 0xff in twos complement
            elif opcode == 0x51: # OP_1, OP_TRUE
                data.append(bytes([0x01]))
            elif opcode > 0x50 and opcode <= 0x60: # OP_#
                data.append(bytes([opcode - 0x50]))
            elif opcode == 0x61: # OP_NOP
                pass
            elif opcode == 0x6a: # OP_RETURN
                pass
            elif opcode == 0x80: # OP_RESERVED
                pass
            elif opcode == 0xb0 or (opcode >= 0xb3 and opcode <= 0xb9): # OP_NOP#
                pass
            else:
                # not data-only
                return []
        return data

    # B

    def b_detect_from_pushdata(self, data):
        return len(data) >= 3 and (data[0].decode('utf-8') == B or data[1].decode('utf-8') == B)

    def b_detect_from_txid(self, txid):
        for script in self.scripts_from_txid(txid):
            data = self.pushdata_from_script(script)
            if self.b_detect_from_pushdata(data):
                return True
        return False

    def b_fields_from_pushdata(self, data):
        fields = {}
        if not self.b_detect_from_pushdata(data):
            return fields
        offset = 0
        if len(data[0]) == 0:
            offset = 1
        fields['data'] = data[offset + 1]
        fields['mediatype'] = data[offset + 2].decode('utf-8')
        if len(data) > offset + 3:
            fields['encoding'] = self.binary_to_bsv_string(data[offset + 3])
        if len(data) > offset + 4:
            fields['name'] = self.binary_to_bsv_string(data[offset + 4])
        if len(data) > offset + 5:
            fields['extra'] = data[offset + 5:]
        return fields

    def b_binary_from_pushdata(self, data):
        fields = self.b_fields_from_pushdata(data)
        if len(fields):
            return fields['data']
        else:
            return None

    def b_fields_from_txid(self, txid):
        fields = {}
        for script in self.scripts_from_txid(txid):
            data = self.pushdata_from_script(script)
            newfields = self.b_fields_from_pushdata(data)
            if len(fields):
                if 'extra' not in fields:
                    fields['extra'] = newfields
                else:
                    fields['extra'].extend(newfields)
            elif len(newfields):
                fields = newfields
        return fields

    def b_file_from_txid(self, txid, file):
        fields = self.b_fields_from_txid(txid)
        if not fields:
            raise ValueError('b tx not found')
        self.binary_to_file(fields['data'], file)
        return fields

    # alias
    download_b = b_file_from_txid

    # BCAT
    
    def bcat_part_detect_from_pushdata(self, data):
        return len(data) >= 2 and (data[0].decode('utf-8') == BCATPART or data[1].decode('utf-8') == BCATPART)

    def bcat_part_detect_fromtxid(self, txid):
        for script in self.scripts_from_txid(txid):
            data = self.pushdata_from_script(script)
            if self.bcat_part_detect_from_pushdata(data):
                return True
        return False
   
    def bcat_part_binary_from_pushdata(self, data):
        if not self.bcat_part_detect_from_pushdata(data):
            subfields = self.bcat_linker_fields_from_pushdata(data)
            if subfields:
                return self.bcat_binary_from_txids(subfields['parts'])
            else:
                return self.b_binary_from_pushdata(data)
        offset = 0
        if len(data[0]) == 0:
            offset = 1
        return b''.join(data[offset + 1:])

    def bcat_part_binary_from_txid(self, txid):
        binary = b''
        for script in self.scripts_from_txid(txid):
            data = self.pushdata_from_script(script)
            newbinary = self.bcat_part_binary_from_pushdata(data)
            if newbinary is not None:
                binary += newbinary
        return binary

    def bcat_linker_detect_from_pushdata(self, data):
        return len(data) >= 8 and (data[0].decode('utf-8') == BCAT or data[1].decode('utf-8') == BCAT)

    def bcat_linker_detect_from_txid(self, txid):
        for script in self.scripts_from_txid(txid):
            data = self.pushdata_from_script(script)
            if self.bcat_linker_detect_from_pushdata(data):
                return True
        return False

    def bcat_linker_fields_from_pushdata(self, data):
        fields = {}
        if not self.bcat_linker_detect_from_pushdata(data):
            return fields
        offset = 0
        if len(data[0]) == 0:
            offset = 1
        fields['info'] = self.binary_to_bsv_string(data[offset + 1])
        fields['mediatype'] = self.binary_to_bsv_string(data[offset + 2])
        fields['encoding'] = self.binary_to_bsv_string(data[offset + 3])
        fields['name'] = self.binary_to_bsv_string(data[offset + 4])
        fields['flag'] = self.binary_to_bsv_string(data[offset + 5])
        parts = []
        for link in data[offset + 6:]:
            parts.append(link.hex())
        fields['parts'] = parts

        return fields

    def bcat_linker_fields_from_txid(self, txid):
        fields = {}
        for script in self.scripts_from_txid(txid):
            data = self.pushdata_from_script(script)
            fields = self.bcat_linker_fields_from_pushdata(data)
            if fields:
                break
        return fields

    def bcat_binary_from_txids(self, txids):
        data = bytes()
        for txid in txids:
            data += self.bcat_part_binary_from_txid(txid)
        return data

    def bcat_fields_from_txid(self, txid, gunzip = True):
        fields = self.bcat_linker_fields_from_txid(txid)
        if not fields:
            return fields
        fields['data'] = self.bcat_binary_from_txids(fields['parts'])
        if gunzip and fields['flag'] in ('gzip', 'nested-gzip'):
            # change 'flag' to reflect that we mutated the data
            fields['flag'] = fields['flag'].replace('zip','unzipped')
            # unzip
            fields['data'] = gzip.decompress(fields['data'])
        return fields

    def download_bcat(self, txid, file, gunzip = True):
        fields = self.bcat_linker_fields_from_txid(txid)
        if not fields:
            raise ValueError('bcat tx not found')
        if gunzip and fields['flag'] in ('gzip', 'nested-gzip'):
            # change 'flag' to reflect that we mutated the data
            fields['flag'] = fields['flag'].replace('zip','unzipped')
        else:
            gunzip = False
        with open(file, 'wb') as f:
            for txid in fields['parts']:
                data = self.bcat_part_binary_from_txid(txid)
                if gunzip:
                    data = gzip.decompress(data)
                f.write(data)
        return fields

# txid0: str = "39ac6259c8d0e115192979ea6ec32172d711059e72c7464287292a371559e899"
# data = Download.do_download(txid0)
# print(data)

# txid1: str = "0ae5b5fd7c064644b05d1762f5ca8aadb1cb4ba03eda0bbb248f91648387c8bc"
# data = Download.do_download(txid1)
# print(data)

# txid : 39ac6259c8d0e115192979ea6ec32172d711059e72c7464287292a371559e899
# decodezero : 
# decodeone : 1ChDHzdd1H4wSjgGMHyndZm6qxEDGjqpJL
# detectfields : False
# subfields : {}
# fields : {}
# {}
# txid : 0ae5b5fd7c064644b05d1762f5ca8aadb1cb4ba03eda0bbb248f91648387c8bc
# decodezero : 
# decodeone : 1ChDHzdd1H4wSjgGMHyndZm6qxEDGjqpJL
# detectfields : False
# subfields : {}
# fields : {}
# {}

Download.do_download_txids(['cf9dd6c9def26fe88d7936b626e26aa003d221578d17a47b9c091f1dcbabaa10', '14398e32c83c13580d921c1abcec5e2a5cb8f60eabc7e141091c35ac8db245d1'])

# https://test.whatsonchain.com/tx/613886b7e390c2c04d3c4a271fb685225daae9eabcce391a44bca3fd949868f3

txid2: str = "613886b7e390c2c04d3c4a271fb685225daae9eabcce391a44bca3fd949868f3"
data = Download.do_download(txid2)
print(data)

#Download.do_download_txids(['a6388e4020dca0d5fbe858d685f521e7e4db776e7a9ca94f666dac7bb7cc0756', 'e0689600d433056f9b5884e487a54d5d6c8674209c42ae96fe5e0a08d8a2f35e'])

