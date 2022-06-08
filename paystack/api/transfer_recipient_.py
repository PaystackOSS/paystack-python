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


class TransferRecipient(object):
    """NOTE: This class is auto generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @classmethod
    def bulk(cls, batch, **kwargs):  # noqa: E501
        """Bulk Create Transfer Recipient  # noqa: E501


        :param batch: A list of transfer recipient object. Each object should contain type, name, and bank_code.  Any Create Transfer Recipient param can also be passed. (required)
        :type batch: list[TransferRecipientCreate]
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'batch'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bulk" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'batch' is set
        if cls().api_client.client_side_validation and ('batch' not in local_var_params or  # noqa: E501
                                                        local_var_params['batch'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `batch` when calling `bulk`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'batch' in local_var_params:
            body_params['batch'] = local_var_params['batch']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/transferrecipient/bulk', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def create(cls, type, name, account_number, bank_code, **kwargs):  # noqa: E501
        """Create Transfer Recipient  # noqa: E501


        :param type: Recipient Type (Only nuban at this time) (required)
        :type type: str
        :param name: Recipient's name (required)
        :type name: str
        :param account_number: Recipient's bank account number (required)
        :type account_number: str
        :param bank_code: Recipient's bank code. You can get the list of Bank Codes by calling the List Banks endpoint (required)
        :type bank_code: str
        :param description: A description for this recipient
        :type description: str
        :param currency: Currency for the account receiving the transfer
        :type currency: str
        :param authorization_code: An authorization code from a previous transaction
        :type authorization_code: str
        :param metadata: Stringified JSON object of custom data
        :type metadata: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'type',
            'name',
            'account_number',
            'bank_code',
            'description',
            'currency',
            'authorization_code',
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
        # verify the required parameter 'type' is set
        if cls().api_client.client_side_validation and ('type' not in local_var_params or  # noqa: E501
                                                        local_var_params['type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `type` when calling `create`")  # noqa: E501
        # verify the required parameter 'name' is set
        if cls().api_client.client_side_validation and ('name' not in local_var_params or  # noqa: E501
                                                        local_var_params['name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `name` when calling `create`")  # noqa: E501
        # verify the required parameter 'account_number' is set
        if cls().api_client.client_side_validation and ('account_number' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_number'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_number` when calling `create`")  # noqa: E501
        # verify the required parameter 'bank_code' is set
        if cls().api_client.client_side_validation and ('bank_code' not in local_var_params or  # noqa: E501
                                                        local_var_params['bank_code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `bank_code` when calling `create`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'type' in local_var_params:
            body_params['type'] = local_var_params['type']
        if 'name' in local_var_params:
            body_params['name'] = local_var_params['name']
        if 'account_number' in local_var_params:
            body_params['account_number'] = local_var_params['account_number']
        if 'bank_code' in local_var_params:
            body_params['bank_code'] = local_var_params['bank_code']
        if 'description' in local_var_params:
            body_params['description'] = local_var_params['description']
        if 'currency' in local_var_params:
            body_params['currency'] = local_var_params['currency']
        if 'authorization_code' in local_var_params:
            body_params['authorization_code'] = local_var_params['authorization_code']
        if 'metadata' in local_var_params:
            body_params['metadata'] = local_var_params['metadata']
        
        
        response_types_map = {
            201: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/transferrecipient', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def fetch(cls, code, **kwargs):  # noqa: E501
        """Fetch Transfer recipient  # noqa: E501


        :param code: Transfer recipient code (required)
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
            '/transferrecipient/{code}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def list(cls, **kwargs):  # noqa: E501
        """List Transfer Recipients  # noqa: E501


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
            '/transferrecipient', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def transferrecipient_code_delete(cls, code, **kwargs):  # noqa: E501
        """Delete Transfer Recipient  # noqa: E501


        :param code: Transfer recipient code (required)
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
                    " to method transferrecipient_code_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'code' is set
        if cls().api_client.client_side_validation and ('code' not in local_var_params or  # noqa: E501
                                                        local_var_params['code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `code` when calling `transferrecipient_code_delete`")  # noqa: E501


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
            '/transferrecipient/{code}', 'DELETE',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def transferrecipient_code_put(cls, code, **kwargs):  # noqa: E501
        """Update Transfer recipient  # noqa: E501


        :param code: Transfer recipient code (required)
        :type code: str
        :param name: Recipient's name
        :type name: str
        :param email: Recipient's email address
        :type email: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'code',
            'name',
            'email'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transferrecipient_code_put" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'code' is set
        if cls().api_client.client_side_validation and ('code' not in local_var_params or  # noqa: E501
                                                        local_var_params['code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `code` when calling `transferrecipient_code_put`")  # noqa: E501


        path_params = {}
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code'] # noqa: E501

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'name' in local_var_params:
            body_params['name'] = local_var_params['name']
        if 'email' in local_var_params:
            body_params['email'] = local_var_params['email']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
            404: "Error",
        }

        return cls().api_client.call_api(
            '/transferrecipient/{code}', 'PUT',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)

