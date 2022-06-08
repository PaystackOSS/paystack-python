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


class Refund(object):
    """NOTE: This class is auto generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @classmethod
    def create(cls, transaction, **kwargs):  # noqa: E501
        """Create Refund  # noqa: E501


        :param transaction: Transaction reference or id (required)
        :type transaction: str
        :param amount: Amount ( in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR ) to be refunded to the customer.  Amount cannot be more than the original transaction amount
        :type amount: int
        :param currency: Three-letter ISO currency. Allowed values are NGN, GHS, ZAR or USD
        :type currency: str
        :param customer_note: Customer reason
        :type customer_note: str
        :param merchant_note: Merchant reason
        :type merchant_note: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'transaction',
            'amount',
            'currency',
            'customer_note',
            'merchant_note'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'transaction' is set
        if cls().api_client.client_side_validation and ('transaction' not in local_var_params or  # noqa: E501
                                                        local_var_params['transaction'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `transaction` when calling `create`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'transaction' in local_var_params:
            body_params['transaction'] = local_var_params['transaction']
        if 'amount' in local_var_params:
            body_params['amount'] = local_var_params['amount']
        if 'currency' in local_var_params:
            body_params['currency'] = local_var_params['currency']
        if 'customer_note' in local_var_params:
            body_params['customer_note'] = local_var_params['customer_note']
        if 'merchant_note' in local_var_params:
            body_params['merchant_note'] = local_var_params['merchant_note']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/refund', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def fetch(cls, id, **kwargs):  # noqa: E501
        """Fetch Refund  # noqa: E501


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
            '/refund/{id}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def list(cls, **kwargs):  # noqa: E501
        """List Refunds  # noqa: E501


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
            '/refund', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)

