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


class DedicatedVirtualAccount(object):
    """NOTE: This class is auto generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @classmethod
    def add_split(cls, account_number, **kwargs):  # noqa: E501
        """Split Dedicated Account Transaction  # noqa: E501


        :param account_number: Valid Dedicated virtual account (required)
        :type account_number: str
        :param subaccount: Subaccount code of the account you want to split the transaction with
        :type subaccount: str
        :param split_code: Split code consisting of the lists of accounts you want to split the transaction with
        :type split_code: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'account_number',
            'subaccount',
            'split_code'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_split" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'account_number' is set
        if cls().api_client.client_side_validation and ('account_number' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_number'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_number` when calling `add_split`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'account_number' in local_var_params:
            body_params['account_number'] = local_var_params['account_number']
        if 'subaccount' in local_var_params:
            body_params['subaccount'] = local_var_params['subaccount']
        if 'split_code' in local_var_params:
            body_params['split_code'] = local_var_params['split_code']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/dedicated_account/split', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def available_providers(cls, **kwargs):  # noqa: E501
        """Fetch Bank Providers  # noqa: E501


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
                    " to method available_providers" % key
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
            '/dedicated_account/available_providers', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def create(cls, customer, **kwargs):  # noqa: E501
        """Create Dedicated Account  # noqa: E501


        :param customer: Customer ID or code (required)
        :type customer: str
        :param preferred_bank: The bank slug for preferred bank. To get a list of available banks, use the List Providers endpoint
        :type preferred_bank: str
        :param subaccount: Subaccount code of the account you want to split the transaction with
        :type subaccount: str
        :param split_code: Split code consisting of the lists of accounts you want to split the transaction with
        :type split_code: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'customer',
            'preferred_bank',
            'subaccount',
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
        if 'preferred_bank' in local_var_params:
            body_params['preferred_bank'] = local_var_params['preferred_bank']
        if 'subaccount' in local_var_params:
            body_params['subaccount'] = local_var_params['subaccount']
        if 'split_code' in local_var_params:
            body_params['split_code'] = local_var_params['split_code']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/dedicated_account', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def deactivate(cls, account_id, **kwargs):  # noqa: E501
        """Deactivate Dedicated Account  # noqa: E501


        :param account_id: (required)
        :type account_id: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'account_id'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deactivate" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'account_id' is set
        if cls().api_client.client_side_validation and ('account_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_id` when calling `deactivate`")  # noqa: E501


        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id'] # noqa: E501

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
            '/dedicated_account/{account_id}', 'DELETE',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def fetch(cls, account_id, **kwargs):  # noqa: E501
        """Fetch Dedicated Account  # noqa: E501


        :param account_id: (required)
        :type account_id: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'account_id'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'account_id' is set
        if cls().api_client.client_side_validation and ('account_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_id` when calling `fetch`")  # noqa: E501


        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id'] # noqa: E501

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
            '/dedicated_account/{account_id}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def list(cls, **kwargs):  # noqa: E501
        """List Dedicated Accounts  # noqa: E501


        :param account_number:
        :type account_number: str
        :param customer:
        :type customer: str
        :param active:
        :type active: bool
        :param currency:
        :type currency: str
        :param provider_slug:
        :type provider_slug: str
        :param bank_id:
        :type bank_id: str
        :param per_page:
        :type per_page: str
        :param page:
        :type page: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'account_number',
            'customer',
            'active',
            'currency',
            'provider_slug',
            'bank_id',
            'per_page',
            'page'
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
        if 'account_number' in local_var_params and local_var_params['account_number'] is not None:  # noqa: E501
            query_params.append(('account_number', local_var_params['account_number']))  # noqa: E501
        if 'customer' in local_var_params and local_var_params['customer'] is not None:  # noqa: E501
            query_params.append(('customer', local_var_params['customer']))  # noqa: E501
        if 'active' in local_var_params and local_var_params['active'] is not None:  # noqa: E501
            query_params.append(('active', local_var_params['active']))  # noqa: E501
        if 'currency' in local_var_params and local_var_params['currency'] is not None:  # noqa: E501
            query_params.append(('currency', local_var_params['currency']))  # noqa: E501
        if 'provider_slug' in local_var_params and local_var_params['provider_slug'] is not None:  # noqa: E501
            query_params.append(('provider_slug', local_var_params['provider_slug']))  # noqa: E501
        if 'bank_id' in local_var_params and local_var_params['bank_id'] is not None:  # noqa: E501
            query_params.append(('bank_id', local_var_params['bank_id']))  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] is not None:  # noqa: E501
            query_params.append(('perPage', local_var_params['per_page']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

        form_params = []
        local_var_files = {}
        body_params = {}

        
        
        response_types_map = {
            200: "Response",
            401: "Error",
            404: "Error",
        }

        return cls().api_client.call_api(
            '/dedicated_account', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def remove_split(cls, account_number, **kwargs):  # noqa: E501
        """Remove Split from Dedicated Account  # noqa: E501


        :param account_number: Valid Dedicated virtual account (required)
        :type account_number: str
        :param subaccount: Subaccount code of the account you want to split the transaction with
        :type subaccount: str
        :param split_code: Split code consisting of the lists of accounts you want to split the transaction with
        :type split_code: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'account_number',
            'subaccount',
            'split_code'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_split" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'account_number' is set
        if cls().api_client.client_side_validation and ('account_number' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_number'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_number` when calling `remove_split`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'account_number' in local_var_params:
            body_params['account_number'] = local_var_params['account_number']
        if 'subaccount' in local_var_params:
            body_params['subaccount'] = local_var_params['subaccount']
        if 'split_code' in local_var_params:
            body_params['split_code'] = local_var_params['split_code']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
            404: "Error",
        }

        return cls().api_client.call_api(
            '/dedicated_account/split', 'DELETE',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)

