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


class ChargeCreate(object):
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
        'amount': 'str',
        'authorization_code': 'str',
        'pin': 'str',
        'reference': 'str',
        'birthday': 'datetime',
        'device_id': 'str',
        'metadata': 'str'
    }

    attribute_map = {
        'email': 'email',
        'amount': 'amount',
        'authorization_code': 'authorization_code',
        'pin': 'pin',
        'reference': 'reference',
        'birthday': 'birthday',
        'device_id': 'device_id',
        'metadata': 'metadata'
    }

    def __init__(self, email=None, amount=None, authorization_code=None, pin=None, reference=None, birthday=None, device_id=None, metadata=None, local_vars_configuration=None):  # noqa: E501
        """ChargeCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._amount = None
        self._authorization_code = None
        self._pin = None
        self._reference = None
        self._birthday = None
        self._device_id = None
        self._metadata = None
        self.discriminator = None

        self.email = email
        self.amount = amount
        if authorization_code is not None:
            self.authorization_code = authorization_code
        if pin is not None:
            self.pin = pin
        if reference is not None:
            self.reference = reference
        if birthday is not None:
            self.birthday = birthday
        if device_id is not None:
            self.device_id = device_id
        if metadata is not None:
            self.metadata = metadata

    @property
    def email(self):
        """Gets the email of this ChargeCreate.  # noqa: E501

        Customer's email address  # noqa: E501

        :return: The email of this ChargeCreate.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ChargeCreate.

        Customer's email address  # noqa: E501

        :param email: The email of this ChargeCreate.  # noqa: E501
        :type email: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def amount(self):
        """Gets the amount of this ChargeCreate.  # noqa: E501

        Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR  # noqa: E501

        :return: The amount of this ChargeCreate.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ChargeCreate.

        Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR  # noqa: E501

        :param amount: The amount of this ChargeCreate.  # noqa: E501
        :type amount: str
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def authorization_code(self):
        """Gets the authorization_code of this ChargeCreate.  # noqa: E501

        An authorization code to charge.  # noqa: E501

        :return: The authorization_code of this ChargeCreate.  # noqa: E501
        :rtype: str
        """
        return self._authorization_code

    @authorization_code.setter
    def authorization_code(self, authorization_code):
        """Sets the authorization_code of this ChargeCreate.

        An authorization code to charge.  # noqa: E501

        :param authorization_code: The authorization_code of this ChargeCreate.  # noqa: E501
        :type authorization_code: str
        """

        self._authorization_code = authorization_code

    @property
    def pin(self):
        """Gets the pin of this ChargeCreate.  # noqa: E501

        4-digit PIN (send with a non-reusable authorization code)  # noqa: E501

        :return: The pin of this ChargeCreate.  # noqa: E501
        :rtype: str
        """
        return self._pin

    @pin.setter
    def pin(self, pin):
        """Sets the pin of this ChargeCreate.

        4-digit PIN (send with a non-reusable authorization code)  # noqa: E501

        :param pin: The pin of this ChargeCreate.  # noqa: E501
        :type pin: str
        """

        self._pin = pin

    @property
    def reference(self):
        """Gets the reference of this ChargeCreate.  # noqa: E501

        Unique transaction reference. Only -, .`, = and alphanumeric characters allowed.  # noqa: E501

        :return: The reference of this ChargeCreate.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this ChargeCreate.

        Unique transaction reference. Only -, .`, = and alphanumeric characters allowed.  # noqa: E501

        :param reference: The reference of this ChargeCreate.  # noqa: E501
        :type reference: str
        """

        self._reference = reference

    @property
    def birthday(self):
        """Gets the birthday of this ChargeCreate.  # noqa: E501

        The customer's birthday in the format YYYY-MM-DD e.g 2017-05-16  # noqa: E501

        :return: The birthday of this ChargeCreate.  # noqa: E501
        :rtype: datetime
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        """Sets the birthday of this ChargeCreate.

        The customer's birthday in the format YYYY-MM-DD e.g 2017-05-16  # noqa: E501

        :param birthday: The birthday of this ChargeCreate.  # noqa: E501
        :type birthday: datetime
        """

        self._birthday = birthday

    @property
    def device_id(self):
        """Gets the device_id of this ChargeCreate.  # noqa: E501

        This is the unique identifier of the device a user uses in making payment.  Only -, .`, = and alphanumeric characters are allowed.  # noqa: E501

        :return: The device_id of this ChargeCreate.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this ChargeCreate.

        This is the unique identifier of the device a user uses in making payment.  Only -, .`, = and alphanumeric characters are allowed.  # noqa: E501

        :param device_id: The device_id of this ChargeCreate.  # noqa: E501
        :type device_id: str
        """

        self._device_id = device_id

    @property
    def metadata(self):
        """Gets the metadata of this ChargeCreate.  # noqa: E501

        Stringified JSON object of custom data  # noqa: E501

        :return: The metadata of this ChargeCreate.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ChargeCreate.

        Stringified JSON object of custom data  # noqa: E501

        :param metadata: The metadata of this ChargeCreate.  # noqa: E501
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
        if not isinstance(other, ChargeCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChargeCreate):
            return True

        return self.to_dict() != other.to_dict()