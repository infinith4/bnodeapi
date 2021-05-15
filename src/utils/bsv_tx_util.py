import multiprocessing
from lib.whats_on_chain_lib import WhatsOnChainLib

class BsvTxUtil():
    def __init__(self):
        pass

    @staticmethod
    def get_txt_on_chain():
        res_get_textdata = []
        #print(trans_list)
        trans_list = ["a6801f8ac9266c077a73b1ec3a24a2f718169b8f44189b25065022cee9c65634","47bdd81af95197b1f6e3d85626d0e6a24e77a596d8b13cfefd8cb971bd7c2db7"]
        if len(trans_list) > 0:
            print(trans_list)
            p = multiprocessing.Pool(6) # プロセス数を6に設定
            network = "test"
            whatsOnChainLib = WhatsOnChainLib(network)
            result = p.map(whatsOnChainLib.get_textdata, trans_list)  ## arg must be array

            for item in result:
                if item is not None and item.mimetype == "text/plain":
                    res_get_textdata.append(item.data)
        print(res_get_textdata)
        return { 'textdata_list': res_get_textdata }, 200