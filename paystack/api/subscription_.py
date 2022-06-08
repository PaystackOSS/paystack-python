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


class Subscription(object):
    """NOTE: This class is auto generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @classmethod
    def create(cls, customer, plan, **kwargs):  # noqa: E501
        """Create Subscription  # noqa: E501


        :param customer: Customer's email address or customer code (required)
        :type customer: str
        :param plan: Plan code (required)
        :type plan: str
        :param authorization: If customer has multiple authorizations, you can set the desired authorization you wish to use for this subscription here.  If this is not supplied, the customer's most recent authorization would be used
        :type authorization: str
        :param start_date: Set the date for the first debit. (ISO 8601 format) e.g. 2017-05-16T00:30:13+01:00
        :type start_date: datetime
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'customer',
            'plan',
            'authorization',
            'start_date'
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
        # verify the required parameter 'plan' is set
        if cls().api_client.client_side_validation and ('plan' not in local_var_params or  # noqa: E501
                                                        local_var_params['plan'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `plan` when calling `create`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'customer' in local_var_params:
            body_params['customer'] = local_var_params['customer']
        if 'plan' in local_var_params:
            body_params['plan'] = local_var_params['plan']
        if 'authorization' in local_var_params:
            body_params['authorization'] = local_var_params['authorization']
        if 'start_date' in local_var_params:
            body_params['start_date'] = local_var_params['start_date']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/subscription', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def disable(cls, code, token, **kwargs):  # noqa: E501
        """Disable Subscription  # noqa: E501


        :param code: Subscription code (required)
        :type code: str
        :param token: Email token (required)
        :type token: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'code',
            'token'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method disable" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'code' is set
        if cls().api_client.client_side_validation and ('code' not in local_var_params or  # noqa: E501
                                                        local_var_params['code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `code` when calling `disable`")  # noqa: E501
        # verify the required parameter 'token' is set
        if cls().api_client.client_side_validation and ('token' not in local_var_params or  # noqa: E501
                                                        local_var_params['token'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `token` when calling `disable`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'code' in local_var_params:
            body_params['code'] = local_var_params['code']
        if 'token' in local_var_params:
            body_params['token'] = local_var_params['token']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/subscription/disable', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def enable(cls, code, token, **kwargs):  # noqa: E501
        """Enable Subscription  # noqa: E501


        :param code: Subscription code (required)
        :type code: str
        :param token: Email token (required)
        :type token: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'code',
            'token'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enable" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'code' is set
        if cls().api_client.client_side_validation and ('code' not in local_var_params or  # noqa: E501
                                                        local_var_params['code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `code` when calling `enable`")  # noqa: E501
        # verify the required parameter 'token' is set
        if cls().api_client.client_side_validation and ('token' not in local_var_params or  # noqa: E501
                                                        local_var_params['token'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `token` when calling `enable`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'code' in local_var_params:
            body_params['code'] = local_var_params['code']
        if 'token' in local_var_params:
            body_params['token'] = local_var_params['token']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/subscription/enable', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def fetch(cls, code, **kwargs):  # noqa: E501
        """Fetch Subscription  # noqa: E501


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
            '/subscription/{code}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def list(cls, **kwargs):  # noqa: E501
        """List Subscriptions  # noqa: E501


        :param per_page: Number of records to fetch per page
        :type per_page: int
        :param page: The section to retrieve
        :type page: int
        :param plan: Plan ID
        :type plan: str
        :param customer: Customer ID
        :type customer: str
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
            'plan',
            'customer',
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
        if 'plan' in local_var_params and local_var_params['plan'] is not None:  # noqa: E501
            query_params.append(('plan', local_var_params['plan']))  # noqa: E501
        if 'customer' in local_var_params and local_var_params['customer'] is not None:  # noqa: E501
            query_params.append(('customer', local_var_params['customer']))  # noqa: E501
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
            '/subscription', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def manage_email(cls, code, **kwargs):  # noqa: E501
        """Send Update Subscription Link  # noqa: E501


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
                    " to method manage_email" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'code' is set
        if cls().api_client.client_side_validation and ('code' not in local_var_params or  # noqa: E501
                                                        local_var_params['code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `code` when calling `manage_email`")  # noqa: E501


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
        }

        return cls().api_client.call_api(
            '/subscription/{code}/manage/email', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def manage_link(cls, code, **kwargs):  # noqa: E501
        """Generate Update Subscription Link  # noqa: E501


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
                    " to method manage_link" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'code' is set
        if cls().api_client.client_side_validation and ('code' not in local_var_params or  # noqa: E501
                                                        local_var_params['code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `code` when calling `manage_link`")  # noqa: E501


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
        }

        return cls().api_client.call_api(
            '/subscription/{code}/manage/link', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)

