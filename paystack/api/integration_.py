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


class Integration(object):
    """NOTE: This class is auto generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @classmethod
    def fetch_payment_session_timeout(cls, **kwargs):  # noqa: E501
        """Fetch Payment Session Timeout  # noqa: E501


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
                    " to method fetch_payment_session_timeout" % key
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
            '/integration/payment_session_timeout', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def update_payment_session_timeout(cls, **kwargs):  # noqa: E501
        """Update Payment Session Timeout  # noqa: E501


        :param body:
        :type body: object
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'body'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_payment_session_timeout" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        
        response_types_map = {
            200: "Response",
            401: "Error",
            404: "Error",
        }

        return cls().api_client.call_api(
            '/integration/payment_session_timeout', 'PUT',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)

