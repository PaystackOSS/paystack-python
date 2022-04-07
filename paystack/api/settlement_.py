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


class Settlement(object):
    """NOTE: This class is auto generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @classmethod
    def fetch(cls, **kwargs):  # noqa: E501
        """Fetch Settlements  # noqa: E501


        :param per_page:
        :type per_page: int
        :param page:
        :type page: int
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'per_page',
            'page'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']


        path_params = {}

        query_params = []
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
            '/settlement', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def transaction(cls, id, **kwargs):  # noqa: E501
        """Settlement Transactions  # noqa: E501


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
                    " to method transaction" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if cls().api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `transaction`")  # noqa: E501


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
            '/settlement/{id}/transaction', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)

