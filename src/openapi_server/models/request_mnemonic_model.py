# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class RequestMnemonicModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, mnemonic=None):  # noqa: E501
        """RequestMnemonicModel - a model defined in OpenAPI

        :param mnemonic: The mnemonic of this RequestMnemonicModel.  # noqa: E501
        :type mnemonic: str
        """
        self.openapi_types = {
            'mnemonic': str
        }

        self.attribute_map = {
            'mnemonic': 'mnemonic'
        }

        self._mnemonic = mnemonic

    @classmethod
    def from_dict(cls, dikt) -> 'RequestMnemonicModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RequestMnemonicModel of this RequestMnemonicModel.  # noqa: E501
        :rtype: RequestMnemonicModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mnemonic(self):
        """Gets the mnemonic of this RequestMnemonicModel.


        :return: The mnemonic of this RequestMnemonicModel.
        :rtype: str
        """
        return self._mnemonic

    @mnemonic.setter
    def mnemonic(self, mnemonic):
        """Sets the mnemonic of this RequestMnemonicModel.


        :param mnemonic: The mnemonic of this RequestMnemonicModel.
        :type mnemonic: str
        """

        self._mnemonic = mnemonic
