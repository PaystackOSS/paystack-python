# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: techsupport@paystack.com
"""


from __future__ import absolute_import

import re  # noqa: F401

import six

from paystack.api_client import ApiClient
from paystack.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PaymentRequest(object):
    """NOTE: This class is auto generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @classmethod
    def archive(cls, id, **kwargs):  # noqa: E501
        """Archive Payment Request  # noqa: E501


        :param id: (required)
        :type id: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'id'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method archive" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if cls().api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `archive`")  # noqa: E501


        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id'] # noqa: E501

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/paymentrequest/archive/{id}', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def create(cls, customer, **kwargs):  # noqa: E501
        """Create Payment Request  # noqa: E501


        :param customer: Customer id or code (required)
        :type customer: str
        :param amount: Payment request amount. Only useful if line items and tax values are ignored.  The endpoint will throw a friendly warning if neither is available.
        :type amount: int
        :param currency: Specify the currency of the invoice. Allowed values are NGN, GHS, ZAR and USD. Defaults to NGN
        :type currency: str
        :param due_date: ISO 8601 representation of request due date
        :type due_date: datetime
        :param description: A short description of the payment request
        :type description: str
        :param line_items: Array of line items
        :type line_items: list[object]
        :param tax: Array of taxes
        :type tax: list[object]
        :param send_notification: Indicates whether Paystack sends an email notification to customer. Defaults to true
        :type send_notification: list[object]
        :param draft: Indicate if request should be saved as draft. Defaults to false and overrides send_notification
        :type draft: list[object]
        :param has_invoice: Set to true to create a draft invoice (adds an auto incrementing invoice number if none is provided)  even if there are no line_items or tax passed
        :type has_invoice: list[object]
        :param invoice_number: Numeric value of invoice. Invoice will start from 1 and auto increment from there. This field is to help  override whatever value Paystack decides. Auto increment for subsequent invoices continue from this point.
        :type invoice_number: int
        :param split_code: The split code of the transaction split.
        :type split_code: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'customer',
            'amount',
            'currency',
            'due_date',
            'description',
            'line_items',
            'tax',
            'send_notification',
            'draft',
            'has_invoice',
            'invoice_number',
            'split_code'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'customer' is set
        if cls().api_client.client_side_validation and ('customer' not in local_var_params or  # noqa: E501
                                                        local_var_params['customer'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `customer` when calling `create`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'customer' in local_var_params:
            body_params['customer'] = local_var_params['customer']
        if 'amount' in local_var_params:
            body_params['amount'] = local_var_params['amount']
        if 'currency' in local_var_params:
            body_params['currency'] = local_var_params['currency']
        if 'due_date' in local_var_params:
            body_params['due_date'] = local_var_params['due_date']
        if 'description' in local_var_params:
            body_params['description'] = local_var_params['description']
        if 'line_items' in local_var_params:
            body_params['line_items'] = local_var_params['line_items']
        if 'tax' in local_var_params:
            body_params['tax'] = local_var_params['tax']
        if 'send_notification' in local_var_params:
            body_params['send_notification'] = local_var_params['send_notification']
        if 'draft' in local_var_params:
            body_params['draft'] = local_var_params['draft']
        if 'has_invoice' in local_var_params:
            body_params['has_invoice'] = local_var_params['has_invoice']
        if 'invoice_number' in local_var_params:
            body_params['invoice_number'] = local_var_params['invoice_number']
        if 'split_code' in local_var_params:
            body_params['split_code'] = local_var_params['split_code']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/paymentrequest', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def fetch(cls, id, **kwargs):  # noqa: E501
        """Fetch Payment Request  # noqa: E501


        :param id: (required)
        :type id: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'id'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if cls().api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `fetch`")  # noqa: E501


        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id'] # noqa: E501

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        
        
        response_types_map = {
            200: "Response",
            401: "Error",
            404: "Error",
        }

        return cls().api_client.call_api(
            '/paymentrequest/{id}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def finalize(cls, id, **kwargs):  # noqa: E501
        """Finalize Payment Request  # noqa: E501


        :param id: (required)
        :type id: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'id'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method finalize" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if cls().api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `finalize`")  # noqa: E501


        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id'] # noqa: E501

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/paymentrequest/finalize/{id}', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def list(cls, **kwargs):  # noqa: E501
        """List Payment Request  # noqa: E501


        :param per_page: Number of records to fetch per page
        :type per_page: int
        :param page: The section to retrieve
        :type page: int
        :param customer: Customer ID
        :type customer: str
        :param status: Invoice status to filter
        :type status: str
        :param currency: If your integration supports more than one currency, choose the one to filter
        :type currency: str
        :param _from: The start date
        :type _from: datetime
        :param to: The end date
        :type to: datetime
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'per_page',
            'page',
            'customer',
            'status',
            'currency',
            '_from',
            'to'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']


        path_params = {}

        query_params = []
        if 'per_page' in local_var_params and local_var_params['per_page'] is not None:  # noqa: E501
            query_params.append(('perPage', local_var_params['per_page']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'customer' in local_var_params and local_var_params['customer'] is not None:  # noqa: E501
            query_params.append(('customer', local_var_params['customer']))  # noqa: E501
        if 'status' in local_var_params and local_var_params['status'] is not None:  # noqa: E501
            query_params.append(('status', local_var_params['status']))  # noqa: E501
        if 'currency' in local_var_params and local_var_params['currency'] is not None:  # noqa: E501
            query_params.append(('currency', local_var_params['currency']))  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'to' in local_var_params and local_var_params['to'] is not None:  # noqa: E501
            query_params.append(('to', local_var_params['to']))  # noqa: E501

        form_params = []
        local_var_files = {}
        body_params = {}

        
        
        response_types_map = {
            200: "Response",
            401: "Error",
            404: "Error",
        }

        return cls().api_client.call_api(
            '/paymentrequest', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def notify(cls, id, **kwargs):  # noqa: E501
        """Send Notification  # noqa: E501


        :param id: (required)
        :type id: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'id'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method notify" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if cls().api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `notify`")  # noqa: E501


        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id'] # noqa: E501

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/paymentrequest/notify/{id}', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def totals(cls, **kwargs):  # noqa: E501
        """Payment Request Total  # noqa: E501


        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method totals" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        
        
        response_types_map = {
            200: "Response",
            401: "Error",
            404: "Error",
        }

        return cls().api_client.call_api(
            '/paymentrequest/totals', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def update(cls, id, **kwargs):  # noqa: E501
        """Update Payment Request  # noqa: E501


        :param id: (required)
        :type id: str
        :param customer: Customer id or code
        :type customer: str
        :param amount: Payment request amount. Only useful if line items and tax values are ignored.  The endpoint will throw a friendly warning if neither is available.
        :type amount: int
        :param currency: Specify the currency of the invoice. Allowed values are NGN, GHS, ZAR and USD. Defaults to NGN
        :type currency: str
        :param due_date: ISO 8601 representation of request due date
        :type due_date: datetime
        :param description: A short description of the payment request
        :type description: str
        :param line_items: Array of line items
        :type line_items: list[object]
        :param tax: Array of taxes
        :type tax: list[object]
        :param send_notification: Indicates whether Paystack sends an email notification to customer. Defaults to true
        :type send_notification: list[object]
        :param draft: Indicate if request should be saved as draft. Defaults to false and overrides send_notification
        :type draft: list[object]
        :param has_invoice: Set to true to create a draft invoice (adds an auto incrementing invoice number if none is provided)  even if there are no line_items or tax passed
        :type has_invoice: list[object]
        :param invoice_number: Numeric value of invoice. Invoice will start from 1 and auto increment from there. This field is to help  override whatever value Paystack decides. Auto increment for subsequent invoices continue from this point.
        :type invoice_number: int
        :param split_code: The split code of the transaction split.
        :type split_code: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'id',
            'customer',
            'amount',
            'currency',
            'due_date',
            'description',
            'line_items',
            'tax',
            'send_notification',
            'draft',
            'has_invoice',
            'invoice_number',
            'split_code'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if cls().api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `update`")  # noqa: E501


        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id'] # noqa: E501

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'customer' in local_var_params:
            body_params['customer'] = local_var_params['customer']
        if 'amount' in local_var_params:
            body_params['amount'] = local_var_params['amount']
        if 'currency' in local_var_params:
            body_params['currency'] = local_var_params['currency']
        if 'due_date' in local_var_params:
            body_params['due_date'] = local_var_params['due_date']
        if 'description' in local_var_params:
            body_params['description'] = local_var_params['description']
        if 'line_items' in local_var_params:
            body_params['line_items'] = local_var_params['line_items']
        if 'tax' in local_var_params:
            body_params['tax'] = local_var_params['tax']
        if 'send_notification' in local_var_params:
            body_params['send_notification'] = local_var_params['send_notification']
        if 'draft' in local_var_params:
            body_params['draft'] = local_var_params['draft']
        if 'has_invoice' in local_var_params:
            body_params['has_invoice'] = local_var_params['has_invoice']
        if 'invoice_number' in local_var_params:
            body_params['invoice_number'] = local_var_params['invoice_number']
        if 'split_code' in local_var_params:
            body_params['split_code'] = local_var_params['split_code']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
            404: "Error",
        }

        return cls().api_client.call_api(
            '/paymentrequest/{id}', 'PUT',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def verify(cls, id, **kwargs):  # noqa: E501
        """Verify Payment Request  # noqa: E501


        :param id: (required)
        :type id: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'id'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method verify" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if cls().api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `verify`")  # noqa: E501


        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id'] # noqa: E501

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        
        
        response_types_map = {
            200: "Response",
            401: "Error",
            404: "Error",
        }

        return cls().api_client.call_api(
            '/paymentrequest/verify/{id}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)

