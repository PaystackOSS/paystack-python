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


class Product(object):
    """NOTE: This class is auto generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @classmethod
    def create(cls, name, description, price, currency, **kwargs):  # noqa: E501
        """Create Product  # noqa: E501


        :param name: Name of product (required)
        :type name: str
        :param description: The description of the product (required)
        :type description: str
        :param price: Price should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR (required)
        :type price: int
        :param currency: Currency in which price is set. Allowed values are: NGN, GHS, ZAR or USD (required)
        :type currency: str
        :param limited: Set to true if the product has limited stock. Leave as false if the product has unlimited stock
        :type limited: bool
        :param quantity: Number of products in stock. Use if limited is true
        :type quantity: int
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'name',
            'description',
            'price',
            'currency',
            'limited',
            'quantity'
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
        # verify the required parameter 'description' is set
        if cls().api_client.client_side_validation and ('description' not in local_var_params or  # noqa: E501
                                                        local_var_params['description'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `description` when calling `create`")  # noqa: E501
        # verify the required parameter 'price' is set
        if cls().api_client.client_side_validation and ('price' not in local_var_params or  # noqa: E501
                                                        local_var_params['price'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `price` when calling `create`")  # noqa: E501
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
        if 'description' in local_var_params:
            body_params['description'] = local_var_params['description']
        if 'price' in local_var_params:
            body_params['price'] = local_var_params['price']
        if 'currency' in local_var_params:
            body_params['currency'] = local_var_params['currency']
        if 'limited' in local_var_params:
            body_params['limited'] = local_var_params['limited']
        if 'quantity' in local_var_params:
            body_params['quantity'] = local_var_params['quantity']
        
        
        response_types_map = {
            201: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/product', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def delete(cls, id, **kwargs):  # noqa: E501
        """Delete Product  # noqa: E501


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
                    " to method delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if cls().api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `delete`")  # noqa: E501


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
            '/product/{id}', 'DELETE',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def fetch(cls, id, **kwargs):  # noqa: E501
        """Fetch Product  # noqa: E501


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
            '/product/{id}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def list(cls, **kwargs):  # noqa: E501
        """List Products  # noqa: E501


        :param per_page:
        :type per_page: int
        :param page:
        :type page: int
        :param active:
        :type active: bool
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
            'active',
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
        if 'active' in local_var_params and local_var_params['active'] is not None:  # noqa: E501
            query_params.append(('active', local_var_params['active']))  # noqa: E501
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
            '/product', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def update(cls, id, **kwargs):  # noqa: E501
        """Update product  # noqa: E501


        :param id: (required)
        :type id: str
        :param name: Name of product
        :type name: str
        :param description: The description of the product
        :type description: str
        :param price: Price should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
        :type price: int
        :param currency: Currency in which price is set. Allowed values are: NGN, GHS, ZAR or USD
        :type currency: str
        :param limited: Set to true if the product has limited stock. Leave as false if the product has unlimited stock
        :type limited: bool
        :param quantity: Number of products in stock. Use if limited is true
        :type quantity: int
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'id',
            'name',
            'description',
            'price',
            'currency',
            'limited',
            'quantity'
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
        if 'description' in local_var_params:
            body_params['description'] = local_var_params['description']
        if 'price' in local_var_params:
            body_params['price'] = local_var_params['price']
        if 'currency' in local_var_params:
            body_params['currency'] = local_var_params['currency']
        if 'limited' in local_var_params:
            body_params['limited'] = local_var_params['limited']
        if 'quantity' in local_var_params:
            body_params['quantity'] = local_var_params['quantity']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
            404: "Error",
        }

        return cls().api_client.call_api(
            '/product/{id}', 'PUT',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)

