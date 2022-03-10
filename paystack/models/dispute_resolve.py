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


class DisputeResolve(object):
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
        'resolution': 'str',
        'message': 'str',
        'refund_amount': 'str',
        'uploaded_filename': 'str',
        'evidence': 'int'
    }

    attribute_map = {
        'resolution': 'resolution',
        'message': 'message',
        'refund_amount': 'refund_amount',
        'uploaded_filename': 'uploaded_filename',
        'evidence': 'evidence'
    }

    def __init__(self, resolution=None, message=None, refund_amount=None, uploaded_filename=None, evidence=None, local_vars_configuration=None):  # noqa: E501
        """DisputeResolve - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._resolution = None
        self._message = None
        self._refund_amount = None
        self._uploaded_filename = None
        self._evidence = None
        self.discriminator = None

        self.resolution = resolution
        self.message = message
        self.refund_amount = refund_amount
        self.uploaded_filename = uploaded_filename
        if evidence is not None:
            self.evidence = evidence

    @property
    def resolution(self):
        """Gets the resolution of this DisputeResolve.  # noqa: E501

        Dispute resolution. Accepted values, merchant-accepted, declined  # noqa: E501

        :return: The resolution of this DisputeResolve.  # noqa: E501
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this DisputeResolve.

        Dispute resolution. Accepted values, merchant-accepted, declined  # noqa: E501

        :param resolution: The resolution of this DisputeResolve.  # noqa: E501
        :type resolution: str
        """
        if self.local_vars_configuration.client_side_validation and resolution is None:  # noqa: E501
            raise ValueError("Invalid value for `resolution`, must not be `None`")  # noqa: E501

        self._resolution = resolution

    @property
    def message(self):
        """Gets the message of this DisputeResolve.  # noqa: E501

        Reason for resolving  # noqa: E501

        :return: The message of this DisputeResolve.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DisputeResolve.

        Reason for resolving  # noqa: E501

        :param message: The message of this DisputeResolve.  # noqa: E501
        :type message: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def refund_amount(self):
        """Gets the refund_amount of this DisputeResolve.  # noqa: E501

        The amount to refund, in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR  # noqa: E501

        :return: The refund_amount of this DisputeResolve.  # noqa: E501
        :rtype: str
        """
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, refund_amount):
        """Sets the refund_amount of this DisputeResolve.

        The amount to refund, in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR  # noqa: E501

        :param refund_amount: The refund_amount of this DisputeResolve.  # noqa: E501
        :type refund_amount: str
        """
        if self.local_vars_configuration.client_side_validation and refund_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `refund_amount`, must not be `None`")  # noqa: E501

        self._refund_amount = refund_amount

    @property
    def uploaded_filename(self):
        """Gets the uploaded_filename of this DisputeResolve.  # noqa: E501

        Filename of attachment returned via response from the Dispute upload URL  # noqa: E501

        :return: The uploaded_filename of this DisputeResolve.  # noqa: E501
        :rtype: str
        """
        return self._uploaded_filename

    @uploaded_filename.setter
    def uploaded_filename(self, uploaded_filename):
        """Sets the uploaded_filename of this DisputeResolve.

        Filename of attachment returned via response from the Dispute upload URL  # noqa: E501

        :param uploaded_filename: The uploaded_filename of this DisputeResolve.  # noqa: E501
        :type uploaded_filename: str
        """
        if self.local_vars_configuration.client_side_validation and uploaded_filename is None:  # noqa: E501
            raise ValueError("Invalid value for `uploaded_filename`, must not be `None`")  # noqa: E501

        self._uploaded_filename = uploaded_filename

    @property
    def evidence(self):
        """Gets the evidence of this DisputeResolve.  # noqa: E501

        Evidence Id for fraud claims  # noqa: E501

        :return: The evidence of this DisputeResolve.  # noqa: E501
        :rtype: int
        """
        return self._evidence

    @evidence.setter
    def evidence(self, evidence):
        """Sets the evidence of this DisputeResolve.

        Evidence Id for fraud claims  # noqa: E501

        :param evidence: The evidence of this DisputeResolve.  # noqa: E501
        :type evidence: int
        """

        self._evidence = evidence

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
        if not isinstance(other, DisputeResolve):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DisputeResolve):
            return True

        return self.to_dict() != other.to_dict()
