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


class Plan(object):
    """NOTE: This class is auto generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @classmethod
    def create(cls, name, amount, interval, **kwargs):  # noqa: E501
        """Create Plan  # noqa: E501


        :param name: Name of plan (required)
        :type name: str
        :param amount: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR (required)
        :type amount: int
        :param interval: Interval in words. Valid intervals are daily, weekly, monthly,biannually, annually (required)
        :type interval: str
        :param description: A description for this plan
        :type description: bool
        :param send_invoices: Set to false if you don't want invoices to be sent to your customers
        :type send_invoices: bool
        :param send_sms: Set to false if you don't want text messages to be sent to your customers
        :type send_sms: bool
        :param currency: Currency in which amount is set. Allowed values are NGN, GHS, ZAR or USD
        :type currency: str
        :param invoice_limit: Number of invoices to raise during subscription to this plan.  Can be overridden by specifying an invoice_limit while subscribing.
        :type invoice_limit: int
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'name',
            'amount',
            'interval',
            'description',
            'send_invoices',
            'send_sms',
            'currency',
            'invoice_limit'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'name' is set
        if cls().api_client.client_side_validation and ('name' not in local_var_params or  # noqa: E501
                                                        local_var_params['name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `name` when calling `create`")  # noqa: E501
        # verify the required parameter 'amount' is set
        if cls().api_client.client_side_validation and ('amount' not in local_var_params or  # noqa: E501
                                                        local_var_params['amount'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `amount` when calling `create`")  # noqa: E501
        # verify the required parameter 'interval' is set
        if cls().api_client.client_side_validation and ('interval' not in local_var_params or  # noqa: E501
                                                        local_var_params['interval'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `interval` when calling `create`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'name' in local_var_params:
            body_params['name'] = local_var_params['name']
        if 'amount' in local_var_params:
            body_params['amount'] = local_var_params['amount']
        if 'interval' in local_var_params:
            body_params['interval'] = local_var_params['interval']
        if 'description' in local_var_params:
            body_params['description'] = local_var_params['description']
        if 'send_invoices' in local_var_params:
            body_params['send_invoices'] = local_var_params['send_invoices']
        if 'send_sms' in local_var_params:
            body_params['send_sms'] = local_var_params['send_sms']
        if 'currency' in local_var_params:
            body_params['currency'] = local_var_params['currency']
        if 'invoice_limit' in local_var_params:
            body_params['invoice_limit'] = local_var_params['invoice_limit']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/plan', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def fetch(cls, code, **kwargs):  # noqa: E501
        """Fetch Plan  # noqa: E501


        :param code: (required)
        :type code: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'code'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'code' is set
        if cls().api_client.client_side_validation and ('code' not in local_var_params or  # noqa: E501
                                                        local_var_params['code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `code` when calling `fetch`")  # noqa: E501


        path_params = {}
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code'] # noqa: E501

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
            '/plan/{code}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def list(cls, **kwargs):  # noqa: E501
        """List Plans  # noqa: E501


        :param per_page: Number of records to fetch per page
        :type per_page: int
        :param page: The section to retrieve
        :type page: int
        :param interval: Specify interval of the plan
        :type interval: str
        :param amount: The amount on the plans to retrieve
        :type amount: int
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
            'interval',
            'amount',
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
        if 'interval' in local_var_params and local_var_params['interval'] is not None:  # noqa: E501
            query_params.append(('interval', local_var_params['interval']))  # noqa: E501
        if 'amount' in local_var_params and local_var_params['amount'] is not None:  # noqa: E501
            query_params.append(('amount', local_var_params['amount']))  # noqa: E501
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
            '/plan', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def update(cls, code, **kwargs):  # noqa: E501
        """Update Plan  # noqa: E501


        :param code: (required)
        :type code: str
        :param name: Name of plan
        :type name: str
        :param amount: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
        :type amount: int
        :param interval: Interval in words. Valid intervals are daily, weekly, monthly,biannually, annually
        :type interval: str
        :param description: A description for this plan
        :type description: bool
        :param send_invoices: Set to false if you don't want invoices to be sent to your customers
        :type send_invoices: bool
        :param send_sms: Set to false if you don't want text messages to be sent to your customers
        :type send_sms: bool
        :param currency: Currency in which amount is set. Allowed values are NGN, GHS, ZAR or USD
        :type currency: str
        :param invoice_limit: Number of invoices to raise during subscription to this plan.  Can be overridden by specifying an invoice_limit while subscribing.
        :type invoice_limit: int
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'code',
            'name',
            'amount',
            'interval',
            'description',
            'send_invoices',
            'send_sms',
            'currency',
            'invoice_limit'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'code' is set
        if cls().api_client.client_side_validation and ('code' not in local_var_params or  # noqa: E501
                                                        local_var_params['code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `code` when calling `update`")  # noqa: E501


        path_params = {}
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code'] # noqa: E501

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'name' in local_var_params:
            body_params['name'] = local_var_params['name']
        if 'amount' in local_var_params:
            body_params['amount'] = local_var_params['amount']
        if 'interval' in local_var_params:
            body_params['interval'] = local_var_params['interval']
        if 'description' in local_var_params:
            body_params['description'] = local_var_params['description']
        if 'send_invoices' in local_var_params:
            body_params['send_invoices'] = local_var_params['send_invoices']
        if 'send_sms' in local_var_params:
            body_params['send_sms'] = local_var_params['send_sms']
        if 'currency' in local_var_params:
            body_params['currency'] = local_var_params['currency']
        if 'invoice_limit' in local_var_params:
            body_params['invoice_limit'] = local_var_params['invoice_limit']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
            404: "Error",
        }

        return cls().api_client.call_api(
            '/plan/{code}', 'PUT',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)

