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


class ProductUpdate(object):
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
        'name': 'str',
        'description': 'str',
        'price': 'int',
        'currency': 'str',
        'limited': 'bool',
        'quantity': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'price': 'price',
        'currency': 'currency',
        'limited': 'limited',
        'quantity': 'quantity'
    }

    def __init__(self, name=None, description=None, price=None, currency=None, limited=None, quantity=None, local_vars_configuration=None):  # noqa: E501
        """ProductUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._price = None
        self._currency = None
        self._limited = None
        self._quantity = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if price is not None:
            self.price = price
        if currency is not None:
            self.currency = currency
        if limited is not None:
            self.limited = limited
        if quantity is not None:
            self.quantity = quantity

    @property
    def name(self):
        """Gets the name of this ProductUpdate.  # noqa: E501

        Name of product  # noqa: E501

        :return: The name of this ProductUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductUpdate.

        Name of product  # noqa: E501

        :param name: The name of this ProductUpdate.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ProductUpdate.  # noqa: E501

        The description of the product  # noqa: E501

        :return: The description of this ProductUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProductUpdate.

        The description of the product  # noqa: E501

        :param description: The description of this ProductUpdate.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def price(self):
        """Gets the price of this ProductUpdate.  # noqa: E501

        Price should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR  # noqa: E501

        :return: The price of this ProductUpdate.  # noqa: E501
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ProductUpdate.

        Price should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR  # noqa: E501

        :param price: The price of this ProductUpdate.  # noqa: E501
        :type price: int
        """

        self._price = price

    @property
    def currency(self):
        """Gets the currency of this ProductUpdate.  # noqa: E501

        Currency in which price is set. Allowed values are: NGN, GHS, ZAR or USD  # noqa: E501

        :return: The currency of this ProductUpdate.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ProductUpdate.

        Currency in which price is set. Allowed values are: NGN, GHS, ZAR or USD  # noqa: E501

        :param currency: The currency of this ProductUpdate.  # noqa: E501
        :type currency: str
        """

        self._currency = currency

    @property
    def limited(self):
        """Gets the limited of this ProductUpdate.  # noqa: E501

        Set to true if the product has limited stock. Leave as false if the product has unlimited stock  # noqa: E501

        :return: The limited of this ProductUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._limited

    @limited.setter
    def limited(self, limited):
        """Sets the limited of this ProductUpdate.

        Set to true if the product has limited stock. Leave as false if the product has unlimited stock  # noqa: E501

        :param limited: The limited of this ProductUpdate.  # noqa: E501
        :type limited: bool
        """

        self._limited = limited

    @property
    def quantity(self):
        """Gets the quantity of this ProductUpdate.  # noqa: E501

        Number of products in stock. Use if limited is true  # noqa: E501

        :return: The quantity of this ProductUpdate.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ProductUpdate.

        Number of products in stock. Use if limited is true  # noqa: E501

        :param quantity: The quantity of this ProductUpdate.  # noqa: E501
        :type quantity: int
        """

        self._quantity = quantity

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
        if not isinstance(other, ProductUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductUpdate):
            return True

        return self.to_dict() != other.to_dict()
