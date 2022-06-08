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


class Split(object):
    """NOTE: This class is auto generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @classmethod
    def add_subaccount(cls, id, **kwargs):  # noqa: E501
        """Add Subaccount to Split  # noqa: E501


        :param id: (required)
        :type id: str
        :param subaccount: Subaccount code of the customer or partner
        :type subaccount: str
        :param share: The percentage or flat quota of the customer or partner
        :type share: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'id',
            'subaccount',
            'share'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_subaccount" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if cls().api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `add_subaccount`")  # noqa: E501


        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id'] # noqa: E501

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'subaccount' in local_var_params:
            body_params['subaccount'] = local_var_params['subaccount']
        if 'share' in local_var_params:
            body_params['share'] = local_var_params['share']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/split/{id}/subaccount/add', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def create(cls, name, type, subaccounts, currency, **kwargs):  # noqa: E501
        """Create Split  # noqa: E501


        :param name: Name of the transaction split (required)
        :type name: str
        :param type: The type of transaction split you want to create. (required)
        :type type: str
        :param subaccounts: A list of object containing subaccount code and number of shares (required)
        :type subaccounts: list[SplitSubaccounts]
        :param currency: The transaction currency (required)
        :type currency: str
        :param bearer_type: This allows you specify how the transaction charge should be processed
        :type bearer_type: str
        :param bearer_subaccount: This is the subaccount code of the customer or partner that would bear the transaction charge if you specified subaccount as the bearer type
        :type bearer_subaccount: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'name',
            'type',
            'subaccounts',
            'currency',
            'bearer_type',
            'bearer_subaccount'
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
        # verify the required parameter 'type' is set
        if cls().api_client.client_side_validation and ('type' not in local_var_params or  # noqa: E501
                                                        local_var_params['type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `type` when calling `create`")  # noqa: E501
        # verify the required parameter 'subaccounts' is set
        if cls().api_client.client_side_validation and ('subaccounts' not in local_var_params or  # noqa: E501
                                                        local_var_params['subaccounts'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `subaccounts` when calling `create`")  # noqa: E501
        # verify the required parameter 'currency' is set
        if cls().api_client.client_side_validation and ('currency' not in local_var_params or  # noqa: E501
                                                        local_var_params['currency'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `currency` when calling `create`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'name' in local_var_params:
            body_params['name'] = local_var_params['name']
        if 'type' in local_var_params:
            body_params['type'] = local_var_params['type']
        if 'subaccounts' in local_var_params:
            body_params['subaccounts'] = local_var_params['subaccounts']
        if 'currency' in local_var_params:
            body_params['currency'] = local_var_params['currency']
        if 'bearer_type' in local_var_params:
            body_params['bearer_type'] = local_var_params['bearer_type']
        if 'bearer_subaccount' in local_var_params:
            body_params['bearer_subaccount'] = local_var_params['bearer_subaccount']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/split', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def fetch(cls, id, **kwargs):  # noqa: E501
        """Fetch Split  # noqa: E501


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
            '/split/{id}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def list(cls, **kwargs):  # noqa: E501
        """List/Search Splits  # noqa: E501


        :param name:
        :type name: str
        :param active:
        :type active: str
        :param sort_by:
        :type sort_by: str
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
            'name',
            'active',
            'sort_by',
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
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'active' in local_var_params and local_var_params['active'] is not None:  # noqa: E501
            query_params.append(('active', local_var_params['active']))  # noqa: E501
        if 'sort_by' in local_var_params and local_var_params['sort_by'] is not None:  # noqa: E501
            query_params.append(('sort_by', local_var_params['sort_by']))  # noqa: E501
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
            '/split', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def remove_subaccount(cls, id, **kwargs):  # noqa: E501
        """Remove Subaccount from split  # noqa: E501


        :param id: (required)
        :type id: str
        :param subaccount: Subaccount code of the customer or partner
        :type subaccount: str
        :param share: The percentage or flat quota of the customer or partner
        :type share: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'id',
            'subaccount',
            'share'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_subaccount" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if cls().api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `remove_subaccount`")  # noqa: E501


        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id'] # noqa: E501

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'subaccount' in local_var_params:
            body_params['subaccount'] = local_var_params['subaccount']
        if 'share' in local_var_params:
            body_params['share'] = local_var_params['share']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/split/{id}/subaccount/remove', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def update(cls, id, **kwargs):  # noqa: E501
        """Update Split  # noqa: E501


        :param id: (required)
        :type id: str
        :param name: Name of the transaction split
        :type name: str
        :param active: Toggle status of split. When true, the split is active, else it's inactive
        :type active: bool
        :param bearer_type: This allows you specify how the transaction charge should be processed
        :type bearer_type: str
        :param bearer_subaccount: This is the subaccount code of the customer or partner that would bear the transaction charge if you specified subaccount as the bearer type
        :type bearer_subaccount: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'id',
            'name',
            'active',
            'bearer_type',
            'bearer_subaccount'
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

        if 'name' in local_var_params:
            body_params['name'] = local_var_params['name']
        if 'active' in local_var_params:
            body_params['active'] = local_var_params['active']
        if 'bearer_type' in local_var_params:
            body_params['bearer_type'] = local_var_params['bearer_type']
        if 'bearer_subaccount' in local_var_params:
            body_params['bearer_subaccount'] = local_var_params['bearer_subaccount']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
            404: "Error",
        }

        return cls().api_client.call_api(
            '/split/{id}', 'PUT',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)

