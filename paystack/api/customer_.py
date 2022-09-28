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


class Customer(object):
    """NOTE: This class is auto generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @classmethod
    def create(cls, email, **kwargs):  # noqa: E501
        """Create Customer  # noqa: E501


        :param email: Customer's email address (required)
        :type email: str
        :param first_name: Customer's first name
        :type first_name: str
        :param last_name: Customer's last name
        :type last_name: str
        :param phone: Customer's phone number
        :type phone: str
        :param metadata: Stringified JSON object of custom data
        :type metadata: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'email',
            'first_name',
            'last_name',
            'phone',
            'metadata'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'email' is set
        if cls().api_client.client_side_validation and ('email' not in local_var_params or  # noqa: E501
                                                        local_var_params['email'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `email` when calling `create`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'email' in local_var_params:
            body_params['email'] = local_var_params['email']
        if 'first_name' in local_var_params:
            body_params['first_name'] = local_var_params['first_name']
        if 'last_name' in local_var_params:
            body_params['last_name'] = local_var_params['last_name']
        if 'phone' in local_var_params:
            body_params['phone'] = local_var_params['phone']
        if 'metadata' in local_var_params:
            body_params['metadata'] = local_var_params['metadata']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/customer', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def deactivate_authorization(cls, authorization_code, **kwargs):  # noqa: E501
        """Deactivate Authorization  # noqa: E501

        Deactivate a customer's card  # noqa: E501

        :param authorization_code: Authorization code to be deactivated (required)
        :type authorization_code: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'authorization_code'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deactivate_authorization" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'authorization_code' is set
        if cls().api_client.client_side_validation and ('authorization_code' not in local_var_params or  # noqa: E501
                                                        local_var_params['authorization_code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `authorization_code` when calling `deactivate_authorization`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'authorization_code' in local_var_params:
            body_params['authorization_code'] = local_var_params['authorization_code']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/customer/deactivate_authorization', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def fetch(cls, code, **kwargs):  # noqa: E501
        """Fetch Customer  # noqa: E501


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
            '/customer/{code}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def list(cls, **kwargs):  # noqa: E501
        """List Customers  # noqa: E501

        List customers on your integration  # noqa: E501

        :param use_cursor:
        :type use_cursor: bool
        :param next:
        :type next: str
        :param previous:
        :type previous: str
        :param _from:
        :type _from: str
        :param to:
        :type to: str
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
            'use_cursor',
            'next',
            'previous',
            '_from',
            'to',
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
        if 'use_cursor' in local_var_params and local_var_params['use_cursor'] is not None:  # noqa: E501
            query_params.append(('use_cursor', local_var_params['use_cursor']))  # noqa: E501
        if 'next' in local_var_params and local_var_params['next'] is not None:  # noqa: E501
            query_params.append(('next', local_var_params['next']))  # noqa: E501
        if 'previous' in local_var_params and local_var_params['previous'] is not None:  # noqa: E501
            query_params.append(('previous', local_var_params['previous']))  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'to' in local_var_params and local_var_params['to'] is not None:  # noqa: E501
            query_params.append(('to', local_var_params['to']))  # noqa: E501
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
            '/customer', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def risk_action(cls, customer, **kwargs):  # noqa: E501
        """White/blacklist Customer  # noqa: E501

        Set customer's risk action by whitelisting or blacklisting the customer  # noqa: E501

        :param customer: Customer's code, or email address (required)
        :type customer: str
        :param risk_action: One of the possible risk actions [ default, allow, deny ]. allow to whitelist.  deny to blacklist. Customers start with a default risk action. 
        :type risk_action: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'customer',
            'risk_action'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method risk_action" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'customer' is set
        if cls().api_client.client_side_validation and ('customer' not in local_var_params or  # noqa: E501
                                                        local_var_params['customer'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `customer` when calling `risk_action`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'customer' in local_var_params:
            body_params['customer'] = local_var_params['customer']
        if 'risk_action' in local_var_params:
            body_params['risk_action'] = local_var_params['risk_action']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/customer/set_risk_action', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def update(cls, code, **kwargs):  # noqa: E501
        """Update Customer  # noqa: E501


        :param code: (required)
        :type code: str
        :param first_name: Customer's first name
        :type first_name: str
        :param last_name: Customer's last name
        :type last_name: str
        :param phone: Customer's phone number
        :type phone: str
        :param metadata: Stringified JSON object of custom data
        :type metadata: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'code',
            'first_name',
            'last_name',
            'phone',
            'metadata'
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

        if 'first_name' in local_var_params:
            body_params['first_name'] = local_var_params['first_name']
        if 'last_name' in local_var_params:
            body_params['last_name'] = local_var_params['last_name']
        if 'phone' in local_var_params:
            body_params['phone'] = local_var_params['phone']
        if 'metadata' in local_var_params:
            body_params['metadata'] = local_var_params['metadata']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
            404: "Error",
        }

        return cls().api_client.call_api(
            '/customer/{code}', 'PUT',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def validate(cls, code, first_name, last_name, type, country, bvn, bank_code, account_number, **kwargs):  # noqa: E501
        """Validate Customer  # noqa: E501

        Validate a customer's identity  # noqa: E501

        :param code: (required)
        :type code: str
        :param first_name: Customer's first name (required)
        :type first_name: str
        :param last_name: Customer's last name (required)
        :type last_name: str
        :param type: Predefined types of identification. (required)
        :type type: str
        :param country: Two-letter country code of identification issuer (required)
        :type country: str
        :param bvn: Customer's Bank Verification Number (required)
        :type bvn: str
        :param bank_code: You can get the list of bank codes by calling the List Banks endpoint (https://api.paystack.co/bank). (required)
        :type bank_code: str
        :param account_number: Customer's bank account number. (required)
        :type account_number: str
        :param value: Customer's identification number. Required if type is bvn
        :type value: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Accepted
        """
        local_var_params = locals()

        all_params = [
            'code',
            'first_name',
            'last_name',
            'type',
            'country',
            'bvn',
            'bank_code',
            'account_number',
            'value'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validate" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'code' is set
        if cls().api_client.client_side_validation and ('code' not in local_var_params or  # noqa: E501
                                                        local_var_params['code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `code` when calling `validate`")  # noqa: E501
        # verify the required parameter 'first_name' is set
        if cls().api_client.client_side_validation and ('first_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['first_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `first_name` when calling `validate`")  # noqa: E501
        # verify the required parameter 'last_name' is set
        if cls().api_client.client_side_validation and ('last_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['last_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `last_name` when calling `validate`")  # noqa: E501
        # verify the required parameter 'type' is set
        if cls().api_client.client_side_validation and ('type' not in local_var_params or  # noqa: E501
                                                        local_var_params['type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `type` when calling `validate`")  # noqa: E501
        # verify the required parameter 'country' is set
        if cls().api_client.client_side_validation and ('country' not in local_var_params or  # noqa: E501
                                                        local_var_params['country'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `country` when calling `validate`")  # noqa: E501
        # verify the required parameter 'bvn' is set
        if cls().api_client.client_side_validation and ('bvn' not in local_var_params or  # noqa: E501
                                                        local_var_params['bvn'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `bvn` when calling `validate`")  # noqa: E501
        # verify the required parameter 'bank_code' is set
        if cls().api_client.client_side_validation and ('bank_code' not in local_var_params or  # noqa: E501
                                                        local_var_params['bank_code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `bank_code` when calling `validate`")  # noqa: E501
        # verify the required parameter 'account_number' is set
        if cls().api_client.client_side_validation and ('account_number' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_number'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_number` when calling `validate`")  # noqa: E501


        path_params = {}
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code'] # noqa: E501

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'first_name' in local_var_params:
            body_params['first_name'] = local_var_params['first_name']
        if 'last_name' in local_var_params:
            body_params['last_name'] = local_var_params['last_name']
        if 'type' in local_var_params:
            body_params['type'] = local_var_params['type']
        if 'country' in local_var_params:
            body_params['country'] = local_var_params['country']
        if 'bvn' in local_var_params:
            body_params['bvn'] = local_var_params['bvn']
        if 'bank_code' in local_var_params:
            body_params['bank_code'] = local_var_params['bank_code']
        if 'account_number' in local_var_params:
            body_params['account_number'] = local_var_params['account_number']
        if 'value' in local_var_params:
            body_params['value'] = local_var_params['value']
        
        
        response_types_map = {
            202: "Accepted",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/customer/{code}/identification', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)

