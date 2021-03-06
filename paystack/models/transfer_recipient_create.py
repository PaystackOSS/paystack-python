# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: techsupport@paystack.com
"""


import inspect
import pprint
import re  # noqa: F401
import six

from paystack.configuration import Configuration


class TransferRecipientCreate(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'name': 'str',
        'account_number': 'str',
        'bank_code': 'str',
        'description': 'str',
        'currency': 'str',
        'authorization_code': 'str',
        'metadata': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'account_number': 'account_number',
        'bank_code': 'bank_code',
        'description': 'description',
        'currency': 'currency',
        'authorization_code': 'authorization_code',
        'metadata': 'metadata'
    }

    def __init__(self, type=None, name=None, account_number=None, bank_code=None, description=None, currency=None, authorization_code=None, metadata=None, local_vars_configuration=None):  # noqa: E501
        """TransferRecipientCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._account_number = None
        self._bank_code = None
        self._description = None
        self._currency = None
        self._authorization_code = None
        self._metadata = None
        self.discriminator = None

        self.type = type
        self.name = name
        self.account_number = account_number
        self.bank_code = bank_code
        if description is not None:
            self.description = description
        if currency is not None:
            self.currency = currency
        if authorization_code is not None:
            self.authorization_code = authorization_code
        if metadata is not None:
            self.metadata = metadata

    @property
    def type(self):
        """Gets the type of this TransferRecipientCreate.  # noqa: E501

        Recipient Type (Only nuban at this time)  # noqa: E501

        :return: The type of this TransferRecipientCreate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TransferRecipientCreate.

        Recipient Type (Only nuban at this time)  # noqa: E501

        :param type: The type of this TransferRecipientCreate.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this TransferRecipientCreate.  # noqa: E501

        Recipient's name  # noqa: E501

        :return: The name of this TransferRecipientCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TransferRecipientCreate.

        Recipient's name  # noqa: E501

        :param name: The name of this TransferRecipientCreate.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def account_number(self):
        """Gets the account_number of this TransferRecipientCreate.  # noqa: E501

        Recipient's bank account number  # noqa: E501

        :return: The account_number of this TransferRecipientCreate.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this TransferRecipientCreate.

        Recipient's bank account number  # noqa: E501

        :param account_number: The account_number of this TransferRecipientCreate.  # noqa: E501
        :type account_number: str
        """
        if self.local_vars_configuration.client_side_validation and account_number is None:  # noqa: E501
            raise ValueError("Invalid value for `account_number`, must not be `None`")  # noqa: E501

        self._account_number = account_number

    @property
    def bank_code(self):
        """Gets the bank_code of this TransferRecipientCreate.  # noqa: E501

        Recipient's bank code. You can get the list of Bank Codes by calling the List Banks endpoint  # noqa: E501

        :return: The bank_code of this TransferRecipientCreate.  # noqa: E501
        :rtype: str
        """
        return self._bank_code

    @bank_code.setter
    def bank_code(self, bank_code):
        """Sets the bank_code of this TransferRecipientCreate.

        Recipient's bank code. You can get the list of Bank Codes by calling the List Banks endpoint  # noqa: E501

        :param bank_code: The bank_code of this TransferRecipientCreate.  # noqa: E501
        :type bank_code: str
        """
        if self.local_vars_configuration.client_side_validation and bank_code is None:  # noqa: E501
            raise ValueError("Invalid value for `bank_code`, must not be `None`")  # noqa: E501

        self._bank_code = bank_code

    @property
    def description(self):
        """Gets the description of this TransferRecipientCreate.  # noqa: E501

        A description for this recipient  # noqa: E501

        :return: The description of this TransferRecipientCreate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TransferRecipientCreate.

        A description for this recipient  # noqa: E501

        :param description: The description of this TransferRecipientCreate.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def currency(self):
        """Gets the currency of this TransferRecipientCreate.  # noqa: E501

        Currency for the account receiving the transfer  # noqa: E501

        :return: The currency of this TransferRecipientCreate.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this TransferRecipientCreate.

        Currency for the account receiving the transfer  # noqa: E501

        :param currency: The currency of this TransferRecipientCreate.  # noqa: E501
        :type currency: str
        """

        self._currency = currency

    @property
    def authorization_code(self):
        """Gets the authorization_code of this TransferRecipientCreate.  # noqa: E501

        An authorization code from a previous transaction  # noqa: E501

        :return: The authorization_code of this TransferRecipientCreate.  # noqa: E501
        :rtype: str
        """
        return self._authorization_code

    @authorization_code.setter
    def authorization_code(self, authorization_code):
        """Sets the authorization_code of this TransferRecipientCreate.

        An authorization code from a previous transaction  # noqa: E501

        :param authorization_code: The authorization_code of this TransferRecipientCreate.  # noqa: E501
        :type authorization_code: str
        """

        self._authorization_code = authorization_code

    @property
    def metadata(self):
        """Gets the metadata of this TransferRecipientCreate.  # noqa: E501

        Stringified JSON object of custom data  # noqa: E501

        :return: The metadata of this TransferRecipientCreate.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this TransferRecipientCreate.

        Stringified JSON object of custom data  # noqa: E501

        :param metadata: The metadata of this TransferRecipientCreate.  # noqa: E501
        :type metadata: str
        """

        self._metadata = metadata

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TransferRecipientCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransferRecipientCreate):
            return True

        return self.to_dict() != other.to_dict()
