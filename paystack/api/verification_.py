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


class Verification(object):
    """NOTE: This class is auto generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @classmethod
    def avs(cls, **kwargs):  # noqa: E501
        """List States (AVS)  # noqa: E501


        :param type:
        :type type: str
        :param country:
        :type country: str
        :param currency:
        :type currency: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'type',
            'country',
            'currency'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method avs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']


        path_params = {}

        query_params = []
        if 'type' in local_var_params and local_var_params['type'] is not None:  # noqa: E501
            query_params.append(('type', local_var_params['type']))  # noqa: E501
        if 'country' in local_var_params and local_var_params['country'] is not None:  # noqa: E501
            query_params.append(('country', local_var_params['country']))  # noqa: E501
        if 'currency' in local_var_params and local_var_params['currency'] is not None:  # noqa: E501
            query_params.append(('currency', local_var_params['currency']))  # noqa: E501

        form_params = []
        local_var_files = {}
        body_params = {}

        
        
        response_types_map = {
            200: "Response",
            401: "Error",
            404: "Error",
        }

        return cls().api_client.call_api(
            '/address_verification/states', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def fetch_banks(cls, **kwargs):  # noqa: E501
        """Fetch Banks  # noqa: E501


        :param country:
        :type country: str
        :param pay_with_bank_transfer:
        :type pay_with_bank_transfer: bool
        :param use_cursor:
        :type use_cursor: bool
        :param per_page:
        :type per_page: int
        :param next:
        :type next: str
        :param previous:
        :type previous: str
        :param gateway:
        :type gateway: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'country',
            'pay_with_bank_transfer',
            'use_cursor',
            'per_page',
            'next',
            'previous',
            'gateway'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_banks" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']


        path_params = {}

        query_params = []
        if 'country' in local_var_params and local_var_params['country'] is not None:  # noqa: E501
            query_params.append(('country', local_var_params['country']))  # noqa: E501
        if 'pay_with_bank_transfer' in local_var_params and local_var_params['pay_with_bank_transfer'] is not None:  # noqa: E501
            query_params.append(('pay_with_bank_transfer', local_var_params['pay_with_bank_transfer']))  # noqa: E501
        if 'use_cursor' in local_var_params and local_var_params['use_cursor'] is not None:  # noqa: E501
            query_params.append(('use_cursor', local_var_params['use_cursor']))  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] is not None:  # noqa: E501
            query_params.append(('perPage', local_var_params['per_page']))  # noqa: E501
        if 'next' in local_var_params and local_var_params['next'] is not None:  # noqa: E501
            query_params.append(('next', local_var_params['next']))  # noqa: E501
        if 'previous' in local_var_params and local_var_params['previous'] is not None:  # noqa: E501
            query_params.append(('previous', local_var_params['previous']))  # noqa: E501
        if 'gateway' in local_var_params and local_var_params['gateway'] is not None:  # noqa: E501
            query_params.append(('gateway', local_var_params['gateway']))  # noqa: E501

        form_params = []
        local_var_files = {}
        body_params = {}

        
        
        response_types_map = {
            200: "Response",
            401: "Error",
            404: "Error",
        }

        return cls().api_client.call_api(
            '/bank', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def list_countries(cls, **kwargs):  # noqa: E501
        """List Countries  # noqa: E501


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
                    " to method list_countries" % key
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
            '/country', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def resolve_account_number(cls, **kwargs):  # noqa: E501
        """Resolve Account Number  # noqa: E501


        :param account_number:
        :type account_number: int
        :param bank_code:
        :type bank_code: int
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'account_number',
            'bank_code'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resolve_account_number" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']


        path_params = {}

        query_params = []
        if 'account_number' in local_var_params and local_var_params['account_number'] is not None:  # noqa: E501
            query_params.append(('account_number', local_var_params['account_number']))  # noqa: E501
        if 'bank_code' in local_var_params and local_var_params['bank_code'] is not None:  # noqa: E501
            query_params.append(('bank_code', local_var_params['bank_code']))  # noqa: E501

        form_params = []
        local_var_files = {}
        body_params = {}

        
        
        response_types_map = {
            200: "Response",
            401: "Error",
            404: "Error",
        }

        return cls().api_client.call_api(
            '/bank/resolve', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def resolve_card_bin(cls, bin, **kwargs):  # noqa: E501
        """Resolve Card BIN  # noqa: E501


        :param bin: (required)
        :type bin: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'bin'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resolve_card_bin" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'bin' is set
        if cls().api_client.client_side_validation and ('bin' not in local_var_params or  # noqa: E501
                                                        local_var_params['bin'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `bin` when calling `resolve_card_bin`")  # noqa: E501


        path_params = {}
        if 'bin' in local_var_params:
            path_params['bin'] = local_var_params['bin'] # noqa: E501

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
            '/decision/bin/{bin}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)

