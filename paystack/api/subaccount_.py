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


class Subaccount(object):
    """NOTE: This class is auto generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @classmethod
    def create(cls, business_name, settlement_bank, account_number, percentage_charge, **kwargs):  # noqa: E501
        """Create Subaccount  # noqa: E501


        :param business_name: Name of business for subaccount (required)
        :type business_name: str
        :param settlement_bank: Bank code for the bank. You can get the list of Bank Codes by calling the List Banks endpoint. (required)
        :type settlement_bank: str
        :param account_number: Bank account number (required)
        :type account_number: str
        :param percentage_charge: Customer's phone number (required)
        :type percentage_charge: float
        :param description: A description for this subaccount
        :type description: str
        :param primary_contact_email: A contact email for the subaccount
        :type primary_contact_email: str
        :param primary_contact_name: The name of the contact person for this subaccount
        :type primary_contact_name: str
        :param primary_contact_phone: A phone number to call for this subaccount
        :type primary_contact_phone: str
        :param metadata: Stringified JSON object of custom data
        :type metadata: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'business_name',
            'settlement_bank',
            'account_number',
            'percentage_charge',
            'description',
            'primary_contact_email',
            'primary_contact_name',
            'primary_contact_phone',
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
        # verify the required parameter 'business_name' is set
        if cls().api_client.client_side_validation and ('business_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['business_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `business_name` when calling `create`")  # noqa: E501
        # verify the required parameter 'settlement_bank' is set
        if cls().api_client.client_side_validation and ('settlement_bank' not in local_var_params or  # noqa: E501
                                                        local_var_params['settlement_bank'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `settlement_bank` when calling `create`")  # noqa: E501
        # verify the required parameter 'account_number' is set
        if cls().api_client.client_side_validation and ('account_number' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_number'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_number` when calling `create`")  # noqa: E501
        # verify the required parameter 'percentage_charge' is set
        if cls().api_client.client_side_validation and ('percentage_charge' not in local_var_params or  # noqa: E501
                                                        local_var_params['percentage_charge'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `percentage_charge` when calling `create`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'business_name' in local_var_params:
            body_params['business_name'] = local_var_params['business_name']
        if 'settlement_bank' in local_var_params:
            body_params['settlement_bank'] = local_var_params['settlement_bank']
        if 'account_number' in local_var_params:
            body_params['account_number'] = local_var_params['account_number']
        if 'percentage_charge' in local_var_params:
            body_params['percentage_charge'] = local_var_params['percentage_charge']
        if 'description' in local_var_params:
            body_params['description'] = local_var_params['description']
        if 'primary_contact_email' in local_var_params:
            body_params['primary_contact_email'] = local_var_params['primary_contact_email']
        if 'primary_contact_name' in local_var_params:
            body_params['primary_contact_name'] = local_var_params['primary_contact_name']
        if 'primary_contact_phone' in local_var_params:
            body_params['primary_contact_phone'] = local_var_params['primary_contact_phone']
        if 'metadata' in local_var_params:
            body_params['metadata'] = local_var_params['metadata']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/subaccount', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def fetch(cls, code, **kwargs):  # noqa: E501
        """Fetch Subaccount  # noqa: E501


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
            '/subaccount/{code}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def list(cls, **kwargs):  # noqa: E501
        """List Subaccounts  # noqa: E501


        :param per_page: Number of records to fetch per page
        :type per_page: int
        :param page: The section to retrieve
        :type page: int
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
            '/subaccount', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def update(cls, code, **kwargs):  # noqa: E501
        """Update Subaccount  # noqa: E501


        :param code: (required)
        :type code: str
        :param business_name: Name of business for subaccount
        :type business_name: str
        :param settlement_bank: Bank code for the bank. You can get the list of Bank Codes by calling the List Banks endpoint.
        :type settlement_bank: str
        :param account_number: Bank account number
        :type account_number: str
        :param active: Activate or deactivate a subaccount
        :type active: bool
        :param percentage_charge: Customer's phone number
        :type percentage_charge: float
        :param description: A description for this subaccount
        :type description: str
        :param primary_contact_email: A contact email for the subaccount
        :type primary_contact_email: str
        :param primary_contact_name: The name of the contact person for this subaccount
        :type primary_contact_name: str
        :param primary_contact_phone: A phone number to call for this subaccount
        :type primary_contact_phone: str
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
            'business_name',
            'settlement_bank',
            'account_number',
            'active',
            'percentage_charge',
            'description',
            'primary_contact_email',
            'primary_contact_name',
            'primary_contact_phone',
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

        if 'business_name' in local_var_params:
            body_params['business_name'] = local_var_params['business_name']
        if 'settlement_bank' in local_var_params:
            body_params['settlement_bank'] = local_var_params['settlement_bank']
        if 'account_number' in local_var_params:
            body_params['account_number'] = local_var_params['account_number']
        if 'active' in local_var_params:
            body_params['active'] = local_var_params['active']
        if 'percentage_charge' in local_var_params:
            body_params['percentage_charge'] = local_var_params['percentage_charge']
        if 'description' in local_var_params:
            body_params['description'] = local_var_params['description']
        if 'primary_contact_email' in local_var_params:
            body_params['primary_contact_email'] = local_var_params['primary_contact_email']
        if 'primary_contact_name' in local_var_params:
            body_params['primary_contact_name'] = local_var_params['primary_contact_name']
        if 'primary_contact_phone' in local_var_params:
            body_params['primary_contact_phone'] = local_var_params['primary_contact_phone']
        if 'metadata' in local_var_params:
            body_params['metadata'] = local_var_params['metadata']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
            404: "Error",
        }

        return cls().api_client.call_api(
            '/subaccount/{code}', 'PUT',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)

