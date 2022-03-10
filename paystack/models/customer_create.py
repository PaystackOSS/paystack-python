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


class CustomerCreate(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'phone': 'str',
        'metadata': 'str'
    }

    attribute_map = {
        'email': 'email',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'phone': 'phone',
        'metadata': 'metadata'
    }

    def __init__(self, email=None, first_name=None, last_name=None, phone=None, metadata=None, local_vars_configuration=None):  # noqa: E501
        """CustomerCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._first_name = None
        self._last_name = None
        self._phone = None
        self._metadata = None
        self.discriminator = None

        self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if phone is not None:
            self.phone = phone
        if metadata is not None:
            self.metadata = metadata

    @property
    def email(self):
        """Gets the email of this CustomerCreate.  # noqa: E501

        Customer's email address  # noqa: E501

        :return: The email of this CustomerCreate.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CustomerCreate.

        Customer's email address  # noqa: E501

        :param email: The email of this CustomerCreate.  # noqa: E501
        :type email: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this CustomerCreate.  # noqa: E501

        Customer's first name  # noqa: E501

        :return: The first_name of this CustomerCreate.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this CustomerCreate.

        Customer's first name  # noqa: E501

        :param first_name: The first_name of this CustomerCreate.  # noqa: E501
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this CustomerCreate.  # noqa: E501

        Customer's last name  # noqa: E501

        :return: The last_name of this CustomerCreate.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this CustomerCreate.

        Customer's last name  # noqa: E501

        :param last_name: The last_name of this CustomerCreate.  # noqa: E501
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def phone(self):
        """Gets the phone of this CustomerCreate.  # noqa: E501

        Customer's phone number  # noqa: E501

        :return: The phone of this CustomerCreate.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CustomerCreate.

        Customer's phone number  # noqa: E501

        :param phone: The phone of this CustomerCreate.  # noqa: E501
        :type phone: str
        """

        self._phone = phone

    @property
    def metadata(self):
        """Gets the metadata of this CustomerCreate.  # noqa: E501

        Stringified JSON object of custom data  # noqa: E501

        :return: The metadata of this CustomerCreate.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CustomerCreate.

        Stringified JSON object of custom data  # noqa: E501

        :param metadata: The metadata of this CustomerCreate.  # noqa: E501
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
        if not isinstance(other, CustomerCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerCreate):
            return True

        return self.to_dict() != other.to_dict()
