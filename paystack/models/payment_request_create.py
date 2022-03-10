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


class PaymentRequestCreate(object):
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
        'customer': 'str',
        'amount': 'int',
        'currency': 'str',
        'due_date': 'datetime',
        'description': 'str',
        'line_items': 'list[object]',
        'tax': 'list[object]',
        'send_notification': 'list[object]',
        'draft': 'list[object]',
        'has_invoice': 'list[object]',
        'invoice_number': 'int',
        'split_code': 'str'
    }

    attribute_map = {
        'customer': 'customer',
        'amount': 'amount',
        'currency': 'currency',
        'due_date': 'due_date',
        'description': 'description',
        'line_items': 'line_items',
        'tax': 'tax',
        'send_notification': 'send_notification',
        'draft': 'draft',
        'has_invoice': 'has_invoice',
        'invoice_number': 'invoice_number',
        'split_code': 'split_code'
    }

    def __init__(self, customer=None, amount=None, currency=None, due_date=None, description=None, line_items=None, tax=None, send_notification=None, draft=None, has_invoice=None, invoice_number=None, split_code=None, local_vars_configuration=None):  # noqa: E501
        """PaymentRequestCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._customer = None
        self._amount = None
        self._currency = None
        self._due_date = None
        self._description = None
        self._line_items = None
        self._tax = None
        self._send_notification = None
        self._draft = None
        self._has_invoice = None
        self._invoice_number = None
        self._split_code = None
        self.discriminator = None

        self.customer = customer
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if due_date is not None:
            self.due_date = due_date
        if description is not None:
            self.description = description
        if line_items is not None:
            self.line_items = line_items
        if tax is not None:
            self.tax = tax
        if send_notification is not None:
            self.send_notification = send_notification
        if draft is not None:
            self.draft = draft
        if has_invoice is not None:
            self.has_invoice = has_invoice
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if split_code is not None:
            self.split_code = split_code

    @property
    def customer(self):
        """Gets the customer of this PaymentRequestCreate.  # noqa: E501

        Customer id or code  # noqa: E501

        :return: The customer of this PaymentRequestCreate.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this PaymentRequestCreate.

        Customer id or code  # noqa: E501

        :param customer: The customer of this PaymentRequestCreate.  # noqa: E501
        :type customer: str
        """
        if self.local_vars_configuration.client_side_validation and customer is None:  # noqa: E501
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def amount(self):
        """Gets the amount of this PaymentRequestCreate.  # noqa: E501

        Payment request amount. Only useful if line items and tax values are ignored.  The endpoint will throw a friendly warning if neither is available.  # noqa: E501

        :return: The amount of this PaymentRequestCreate.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentRequestCreate.

        Payment request amount. Only useful if line items and tax values are ignored.  The endpoint will throw a friendly warning if neither is available.  # noqa: E501

        :param amount: The amount of this PaymentRequestCreate.  # noqa: E501
        :type amount: int
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this PaymentRequestCreate.  # noqa: E501

        Specify the currency of the invoice. Allowed values are NGN, GHS, ZAR and USD. Defaults to NGN  # noqa: E501

        :return: The currency of this PaymentRequestCreate.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PaymentRequestCreate.

        Specify the currency of the invoice. Allowed values are NGN, GHS, ZAR and USD. Defaults to NGN  # noqa: E501

        :param currency: The currency of this PaymentRequestCreate.  # noqa: E501
        :type currency: str
        """

        self._currency = currency

    @property
    def due_date(self):
        """Gets the due_date of this PaymentRequestCreate.  # noqa: E501

        ISO 8601 representation of request due date  # noqa: E501

        :return: The due_date of this PaymentRequestCreate.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this PaymentRequestCreate.

        ISO 8601 representation of request due date  # noqa: E501

        :param due_date: The due_date of this PaymentRequestCreate.  # noqa: E501
        :type due_date: datetime
        """

        self._due_date = due_date

    @property
    def description(self):
        """Gets the description of this PaymentRequestCreate.  # noqa: E501

        A short description of the payment request  # noqa: E501

        :return: The description of this PaymentRequestCreate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PaymentRequestCreate.

        A short description of the payment request  # noqa: E501

        :param description: The description of this PaymentRequestCreate.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def line_items(self):
        """Gets the line_items of this PaymentRequestCreate.  # noqa: E501

        Array of line items  # noqa: E501

        :return: The line_items of this PaymentRequestCreate.  # noqa: E501
        :rtype: list[object]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this PaymentRequestCreate.

        Array of line items  # noqa: E501

        :param line_items: The line_items of this PaymentRequestCreate.  # noqa: E501
        :type line_items: list[object]
        """

        self._line_items = line_items

    @property
    def tax(self):
        """Gets the tax of this PaymentRequestCreate.  # noqa: E501

        Array of taxes  # noqa: E501

        :return: The tax of this PaymentRequestCreate.  # noqa: E501
        :rtype: list[object]
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this PaymentRequestCreate.

        Array of taxes  # noqa: E501

        :param tax: The tax of this PaymentRequestCreate.  # noqa: E501
        :type tax: list[object]
        """

        self._tax = tax

    @property
    def send_notification(self):
        """Gets the send_notification of this PaymentRequestCreate.  # noqa: E501

        Indicates whether Paystack sends an email notification to customer. Defaults to true  # noqa: E501

        :return: The send_notification of this PaymentRequestCreate.  # noqa: E501
        :rtype: list[object]
        """
        return self._send_notification

    @send_notification.setter
    def send_notification(self, send_notification):
        """Sets the send_notification of this PaymentRequestCreate.

        Indicates whether Paystack sends an email notification to customer. Defaults to true  # noqa: E501

        :param send_notification: The send_notification of this PaymentRequestCreate.  # noqa: E501
        :type send_notification: list[object]
        """

        self._send_notification = send_notification

    @property
    def draft(self):
        """Gets the draft of this PaymentRequestCreate.  # noqa: E501

        Indicate if request should be saved as draft. Defaults to false and overrides send_notification  # noqa: E501

        :return: The draft of this PaymentRequestCreate.  # noqa: E501
        :rtype: list[object]
        """
        return self._draft

    @draft.setter
    def draft(self, draft):
        """Sets the draft of this PaymentRequestCreate.

        Indicate if request should be saved as draft. Defaults to false and overrides send_notification  # noqa: E501

        :param draft: The draft of this PaymentRequestCreate.  # noqa: E501
        :type draft: list[object]
        """

        self._draft = draft

    @property
    def has_invoice(self):
        """Gets the has_invoice of this PaymentRequestCreate.  # noqa: E501

        Set to true to create a draft invoice (adds an auto incrementing invoice number if none is provided)  even if there are no line_items or tax passed  # noqa: E501

        :return: The has_invoice of this PaymentRequestCreate.  # noqa: E501
        :rtype: list[object]
        """
        return self._has_invoice

    @has_invoice.setter
    def has_invoice(self, has_invoice):
        """Sets the has_invoice of this PaymentRequestCreate.

        Set to true to create a draft invoice (adds an auto incrementing invoice number if none is provided)  even if there are no line_items or tax passed  # noqa: E501

        :param has_invoice: The has_invoice of this PaymentRequestCreate.  # noqa: E501
        :type has_invoice: list[object]
        """

        self._has_invoice = has_invoice

    @property
    def invoice_number(self):
        """Gets the invoice_number of this PaymentRequestCreate.  # noqa: E501

        Numeric value of invoice. Invoice will start from 1 and auto increment from there. This field is to help  override whatever value Paystack decides. Auto increment for subsequent invoices continue from this point.  # noqa: E501

        :return: The invoice_number of this PaymentRequestCreate.  # noqa: E501
        :rtype: int
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this PaymentRequestCreate.

        Numeric value of invoice. Invoice will start from 1 and auto increment from there. This field is to help  override whatever value Paystack decides. Auto increment for subsequent invoices continue from this point.  # noqa: E501

        :param invoice_number: The invoice_number of this PaymentRequestCreate.  # noqa: E501
        :type invoice_number: int
        """

        self._invoice_number = invoice_number

    @property
    def split_code(self):
        """Gets the split_code of this PaymentRequestCreate.  # noqa: E501

        The split code of the transaction split.  # noqa: E501

        :return: The split_code of this PaymentRequestCreate.  # noqa: E501
        :rtype: str
        """
        return self._split_code

    @split_code.setter
    def split_code(self, split_code):
        """Sets the split_code of this PaymentRequestCreate.

        The split code of the transaction split.  # noqa: E501

        :param split_code: The split_code of this PaymentRequestCreate.  # noqa: E501
        :type split_code: str
        """

        self._split_code = split_code

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
        if not isinstance(other, PaymentRequestCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentRequestCreate):
            return True

        return self.to_dict() != other.to_dict()
