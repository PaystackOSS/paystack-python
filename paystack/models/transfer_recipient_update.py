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


class TransferRecipientUpdate(object):
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
        'email': 'str'
    }

    attribute_map = {
        'name': 'name',
        'email': 'email'
    }

    def __init__(self, name=None, email=None, local_vars_configuration=None):  # noqa: E501
        """TransferRecipientUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._email = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if email is not None:
            self.email = email

    @property
    def name(self):
        """Gets the name of this TransferRecipientUpdate.  # noqa: E501

        Recipient's name  # noqa: E501

        :return: The name of this TransferRecipientUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TransferRecipientUpdate.

        Recipient's name  # noqa: E501

        :param name: The name of this TransferRecipientUpdate.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this TransferRecipientUpdate.  # noqa: E501

        Recipient's email address  # noqa: E501

        :return: The email of this TransferRecipientUpdate.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this TransferRecipientUpdate.

        Recipient's email address  # noqa: E501

        :param email: The email of this TransferRecipientUpdate.  # noqa: E501
        :type email: str
        """

        self._email = email

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
        if not isinstance(other, TransferRecipientUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransferRecipientUpdate):
            return True

        return self.to_dict() != other.to_dict()
