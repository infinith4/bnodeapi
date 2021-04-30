# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.inline_object import InlineObject  # noqa: E501
from openapi_server.models.inline_objectcloud import InlineObjectcloud  # noqa: E501
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
from openapi_server.test import BaseTestCase


class TestApiController(BaseTestCase):
    """ApiController integration test stubs"""

    def test_api_addaddress(self):
        """Test case for api_addaddress

        search data for added address on bitcoin sv
        """
        body = {
  "address" : "bitcoin sv address"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/v1/api/add-address',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_download(self):
        """Test case for api_download

        get data for transaction id on Bitcoin SV.
        """
        headers = { 
            'Accept': 'text/plain',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/v1/api/download/{txid}'.format(txid='txid_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_download_from_cloud(self):
        """Test case for api_download_from_cloud

        get data for transaction id on Bitcoin SV.
        """
        body = {
  "file_id" : "20200729224416_a08f746009a64784b591b423a2c599b5",
  "secret_key_hex" : "secret_key_hex",
  "encrypt_hex" : "0436dd6bc2791f768383494346be916402fd8f4206ceb4b869c8b20841865578c412c3713c2db67f4639967b4a50a94f15acb88baae1fa2a2c5bf3093cd38089c47d077c78177a7ba2d6f0dcaceab0970505c8a323c7005ff41b2dcbc3320254c007f602",
  "on_chain" : true,
  "tx_id_list" : [ "txid01", "txid02" ]
}
        headers = { 
            'Accept': 'text/plain',
            'Content-Type': 'application/json',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/v1/api/download-from-cloud',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_genkey(self):
        """Test case for api_genkey

        Generate Ecies Public Key and Secret Key.
        """
        headers = { 
            'Accept': 'application/json',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/v1/api/genkey/{typeid}'.format(typeid='typeid_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_get_balance(self):
        """Test case for api_get_balance

        get balance from address using woc.
        """
        headers = { 
            'Accept': 'application/json',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/v1/api/get-balance/{addr}'.format(addr='addr_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_login(self):
        """Test case for api_login

        search data for added address on bitcoin sv
        """
        body = {
  "address" : "bitcoin sv address"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/v1/api/login',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_mnemonic(self):
        """Test case for api_mnemonic

        convert mnemonic words to wif, asset on Bitcoin SV.
        """
        body = {
  "mnemonic" : "bitcoin sv mnemonic words"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/v1/api/mnemonic',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_tx(self):
        """Test case for api_tx

        get transactions.
        """
        query_string = [('start_index', 56),
                        ('count', 56)]
        headers = { 
            'Accept': 'application/json',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/v1/api/tx/{addr}'.format(addr='addr_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_api_upload(self):
        """Test case for api_upload

        upload file on Bitcoin SV. (100kb)
        """
        body = openapi_server.InlineObject()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/v1/api/upload',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_upload_text(self):
        """Test case for api_upload_text

        upload text data on Bitcoin SV.
        """
        body = {
  "mnemonic_words" : "",
  "message" : "upload text"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/v1/api/upload-text',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_api_upload_to_cloud(self):
        """Test case for api_upload_to_cloud

        upload file on Cloud Storage.
        """
        body = openapi_server.InlineObjectcloud()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/v1/api/upload-to-cloud',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
