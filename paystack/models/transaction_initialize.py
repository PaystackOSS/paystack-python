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


class TransactionInitialize(object):
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
        'currency': 'str',
        'reference': 'str',
        'callback_url': 'str',
        'plan': 'str',
        'invoice_limit': 'int',
        'metadata': 'str',
        'channels': 'list[str]',
        'split_code': 'str',
        'subaccount': 'str',
        'transaction_charge': 'str',
        'bearer': 'str'
    }

    attribute_map = {
        'email': 'email',
        'amount': 'amount',
        'currency': 'currency',
        'reference': 'reference',
        'callback_url': 'callback_url',
        'plan': 'plan',
        'invoice_limit': 'invoice_limit',
        'metadata': 'metadata',
        'channels': 'channels',
        'split_code': 'split_code',
        'subaccount': 'subaccount',
        'transaction_charge': 'transaction_charge',
        'bearer': 'bearer'
    }

    def __init__(self, email=None, amount=None, currency=None, reference=None, callback_url=None, plan=None, invoice_limit=None, metadata=None, channels=None, split_code=None, subaccount=None, transaction_charge=None, bearer=None, local_vars_configuration=None):  # noqa: E501
        """TransactionInitialize - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._amount = None
        self._currency = None
        self._reference = None
        self._callback_url = None
        self._plan = None
        self._invoice_limit = None
        self._metadata = None
        self._channels = None
        self._split_code = None
        self._subaccount = None
        self._transaction_charge = None
        self._bearer = None
        self.discriminator = None

        self.email = email
        self.amount = amount
        if currency is not None:
            self.currency = currency
        if reference is not None:
            self.reference = reference
        if callback_url is not None:
            self.callback_url = callback_url
        if plan is not None:
            self.plan = plan
        if invoice_limit is not None:
            self.invoice_limit = invoice_limit
        if metadata is not None:
            self.metadata = metadata
        if channels is not None:
            self.channels = channels
        if split_code is not None:
            self.split_code = split_code
        if subaccount is not None:
            self.subaccount = subaccount
        if transaction_charge is not None:
            self.transaction_charge = transaction_charge
        if bearer is not None:
            self.bearer = bearer

    @property
    def email(self):
        """Gets the email of this TransactionInitialize.  # noqa: E501

        Customer's email address  # noqa: E501

        :return: The email of this TransactionInitialize.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this TransactionInitialize.

        Customer's email address  # noqa: E501

        :param email: The email of this TransactionInitialize.  # noqa: E501
        :type email: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def amount(self):
        """Gets the amount of this TransactionInitialize.  # noqa: E501

        Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR  # noqa: E501

        :return: The amount of this TransactionInitialize.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransactionInitialize.

        Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR  # noqa: E501

        :param amount: The amount of this TransactionInitialize.  # noqa: E501
        :type amount: int
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this TransactionInitialize.  # noqa: E501

        The transaction currency  # noqa: E501

        :return: The currency of this TransactionInitialize.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this TransactionInitialize.

        The transaction currency  # noqa: E501

        :param currency: The currency of this TransactionInitialize.  # noqa: E501
        :type currency: str
        """

        self._currency = currency

    @property
    def reference(self):
        """Gets the reference of this TransactionInitialize.  # noqa: E501

        Unique transaction reference. Only -, ., = and alphanumeric characters allowed.  # noqa: E501

        :return: The reference of this TransactionInitialize.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this TransactionInitialize.

        Unique transaction reference. Only -, ., = and alphanumeric characters allowed.  # noqa: E501

        :param reference: The reference of this TransactionInitialize.  # noqa: E501
        :type reference: str
        """

        self._reference = reference

    @property
    def callback_url(self):
        """Gets the callback_url of this TransactionInitialize.  # noqa: E501

        Fully qualified url, e.g. https://example.com/ . Use this to override the callback url provided on the dashboard for this transaction  # noqa: E501

        :return: The callback_url of this TransactionInitialize.  # noqa: E501
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """Sets the callback_url of this TransactionInitialize.

        Fully qualified url, e.g. https://example.com/ . Use this to override the callback url provided on the dashboard for this transaction  # noqa: E501

        :param callback_url: The callback_url of this TransactionInitialize.  # noqa: E501
        :type callback_url: str
        """

        self._callback_url = callback_url

    @property
    def plan(self):
        """Gets the plan of this TransactionInitialize.  # noqa: E501

        If transaction is to create a subscription to a predefined plan, provide plan code here.  This would invalidate the value provided in amount  # noqa: E501

        :return: The plan of this TransactionInitialize.  # noqa: E501
        :rtype: str
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this TransactionInitialize.

        If transaction is to create a subscription to a predefined plan, provide plan code here.  This would invalidate the value provided in amount  # noqa: E501

        :param plan: The plan of this TransactionInitialize.  # noqa: E501
        :type plan: str
        """

        self._plan = plan

    @property
    def invoice_limit(self):
        """Gets the invoice_limit of this TransactionInitialize.  # noqa: E501

        Number of times to charge customer during subscription to plan  # noqa: E501

        :return: The invoice_limit of this TransactionInitialize.  # noqa: E501
        :rtype: int
        """
        return self._invoice_limit

    @invoice_limit.setter
    def invoice_limit(self, invoice_limit):
        """Sets the invoice_limit of this TransactionInitialize.

        Number of times to charge customer during subscription to plan  # noqa: E501

        :param invoice_limit: The invoice_limit of this TransactionInitialize.  # noqa: E501
        :type invoice_limit: int
        """

        self._invoice_limit = invoice_limit

    @property
    def metadata(self):
        """Gets the metadata of this TransactionInitialize.  # noqa: E501

        Stringified JSON object of custom data  # noqa: E501

        :return: The metadata of this TransactionInitialize.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this TransactionInitialize.

        Stringified JSON object of custom data  # noqa: E501

        :param metadata: The metadata of this TransactionInitialize.  # noqa: E501
        :type metadata: str
        """

        self._metadata = metadata

    @property
    def channels(self):
        """Gets the channels of this TransactionInitialize.  # noqa: E501

        An array of payment channels to control what channels you want to make available to the user to make a payment with  # noqa: E501

        :return: The channels of this TransactionInitialize.  # noqa: E501
        :rtype: list[str]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this TransactionInitialize.

        An array of payment channels to control what channels you want to make available to the user to make a payment with  # noqa: E501

        :param channels: The channels of this TransactionInitialize.  # noqa: E501
        :type channels: list[str]
        """

        self._channels = channels

    @property
    def split_code(self):
        """Gets the split_code of this TransactionInitialize.  # noqa: E501

        The split code of the transaction split  # noqa: E501

        :return: The split_code of this TransactionInitialize.  # noqa: E501
        :rtype: str
        """
        return self._split_code

    @split_code.setter
    def split_code(self, split_code):
        """Sets the split_code of this TransactionInitialize.

        The split code of the transaction split  # noqa: E501

        :param split_code: The split_code of this TransactionInitialize.  # noqa: E501
        :type split_code: str
        """

        self._split_code = split_code

    @property
    def subaccount(self):
        """Gets the subaccount of this TransactionInitialize.  # noqa: E501

        The code for the subaccount that owns the payment  # noqa: E501

        :return: The subaccount of this TransactionInitialize.  # noqa: E501
        :rtype: str
        """
        return self._subaccount

    @subaccount.setter
    def subaccount(self, subaccount):
        """Sets the subaccount of this TransactionInitialize.

        The code for the subaccount that owns the payment  # noqa: E501

        :param subaccount: The subaccount of this TransactionInitialize.  # noqa: E501
        :type subaccount: str
        """

        self._subaccount = subaccount

    @property
    def transaction_charge(self):
        """Gets the transaction_charge of this TransactionInitialize.  # noqa: E501

        A flat fee to charge the subaccount for a transaction.  This overrides the split percentage set when the subaccount was created  # noqa: E501

        :return: The transaction_charge of this TransactionInitialize.  # noqa: E501
        :rtype: str
        """
        return self._transaction_charge

    @transaction_charge.setter
    def transaction_charge(self, transaction_charge):
        """Sets the transaction_charge of this TransactionInitialize.

        A flat fee to charge the subaccount for a transaction.  This overrides the split percentage set when the subaccount was created  # noqa: E501

        :param transaction_charge: The transaction_charge of this TransactionInitialize.  # noqa: E501
        :type transaction_charge: str
        """

        self._transaction_charge = transaction_charge

    @property
    def bearer(self):
        """Gets the bearer of this TransactionInitialize.  # noqa: E501

        The beare of the transaction charge  # noqa: E501

        :return: The bearer of this TransactionInitialize.  # noqa: E501
        :rtype: str
        """
        return self._bearer

    @bearer.setter
    def bearer(self, bearer):
        """Sets the bearer of this TransactionInitialize.

        The beare of the transaction charge  # noqa: E501

        :param bearer: The bearer of this TransactionInitialize.  # noqa: E501
        :type bearer: str
        """

        self._bearer = bearer

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
        if not isinstance(other, TransactionInitialize):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionInitialize):
            return True

        return self.to_dict() != other.to_dict()
