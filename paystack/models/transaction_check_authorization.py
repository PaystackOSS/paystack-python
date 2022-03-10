# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


import inspect
import pprint
import re  # noqa: F401
import six

from paystack.configuration import Configuration


class TransactionCheckAuthorization(object):
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
        'email': 'str',
        'amount': 'int',
        'authorization_code': 'str',
        'currency': 'str'
    }

    attribute_map = {
        'email': 'email',
        'amount': 'amount',
        'authorization_code': 'authorization_code',
        'currency': 'currency'
    }

    def __init__(self, email=None, amount=None, authorization_code=None, currency=None, local_vars_configuration=None):  # noqa: E501
        """TransactionCheckAuthorization - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._amount = None
        self._authorization_code = None
        self._currency = None
        self.discriminator = None

        self.email = email
        self.amount = amount
        if authorization_code is not None:
            self.authorization_code = authorization_code
        if currency is not None:
            self.currency = currency

    @property
    def email(self):
        """Gets the email of this TransactionCheckAuthorization.  # noqa: E501

        Customer's email address  # noqa: E501

        :return: The email of this TransactionCheckAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this TransactionCheckAuthorization.

        Customer's email address  # noqa: E501

        :param email: The email of this TransactionCheckAuthorization.  # noqa: E501
        :type email: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def amount(self):
        """Gets the amount of this TransactionCheckAuthorization.  # noqa: E501

        Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR  # noqa: E501

        :return: The amount of this TransactionCheckAuthorization.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransactionCheckAuthorization.

        Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR  # noqa: E501

        :param amount: The amount of this TransactionCheckAuthorization.  # noqa: E501
        :type amount: int
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def authorization_code(self):
        """Gets the authorization_code of this TransactionCheckAuthorization.  # noqa: E501

        Valid authorization code to charge  # noqa: E501

        :return: The authorization_code of this TransactionCheckAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._authorization_code

    @authorization_code.setter
    def authorization_code(self, authorization_code):
        """Sets the authorization_code of this TransactionCheckAuthorization.

        Valid authorization code to charge  # noqa: E501

        :param authorization_code: The authorization_code of this TransactionCheckAuthorization.  # noqa: E501
        :type authorization_code: str
        """

        self._authorization_code = authorization_code

    @property
    def currency(self):
        """Gets the currency of this TransactionCheckAuthorization.  # noqa: E501

        The transaction currency  # noqa: E501

        :return: The currency of this TransactionCheckAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this TransactionCheckAuthorization.

        The transaction currency  # noqa: E501

        :param currency: The currency of this TransactionCheckAuthorization.  # noqa: E501
        :type currency: str
        """

        self._currency = currency

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
        if not isinstance(other, TransactionCheckAuthorization):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionCheckAuthorization):
            return True

        return self.to_dict() != other.to_dict()
