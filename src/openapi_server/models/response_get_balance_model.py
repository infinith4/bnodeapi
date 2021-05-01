# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ResponseGetBalanceModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, confirmed=None, unconfirmed=None):  # noqa: E501
        """ResponseGetBalanceModel - a model defined in OpenAPI

        :param confirmed: The confirmed of this ResponseGetBalanceModel.  # noqa: E501
        :type confirmed: int
        :param unconfirmed: The unconfirmed of this ResponseGetBalanceModel.  # noqa: E501
        :type unconfirmed: int
        """
        self.openapi_types = {
            'confirmed': int,
            'unconfirmed': int
        }

        self.attribute_map = {
            'confirmed': 'confirmed',
            'unconfirmed': 'unconfirmed'
        }

        self._confirmed = confirmed
        self._unconfirmed = unconfirmed

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseGetBalanceModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseGetBalanceModel of this ResponseGetBalanceModel.  # noqa: E501
        :rtype: ResponseGetBalanceModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def confirmed(self):
        """Gets the confirmed of this ResponseGetBalanceModel.


        :return: The confirmed of this ResponseGetBalanceModel.
        :rtype: int
        """
        return self._confirmed

    @confirmed.setter
    def confirmed(self, confirmed):
        """Sets the confirmed of this ResponseGetBalanceModel.


        :param confirmed: The confirmed of this ResponseGetBalanceModel.
        :type confirmed: int
        """

        self._confirmed = confirmed

    @property
    def unconfirmed(self):
        """Gets the unconfirmed of this ResponseGetBalanceModel.


        :return: The unconfirmed of this ResponseGetBalanceModel.
        :rtype: int
        """
        return self._unconfirmed

    @unconfirmed.setter
    def unconfirmed(self, unconfirmed):
        """Sets the unconfirmed of this ResponseGetBalanceModel.


        :param unconfirmed: The unconfirmed of this ResponseGetBalanceModel.
        :type unconfirmed: int
        """

        self._unconfirmed = unconfirmed