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


class Page(object):
    """NOTE: This class is auto generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @classmethod
    def add_products(cls, id, product, **kwargs):  # noqa: E501
        """Add Products  # noqa: E501


        :param id: (required)
        :type id: str
        :param product: IDs of all products to add to a page (required)
        :type product: list[str]
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'id',
            'product'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_products" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if cls().api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `add_products`")  # noqa: E501
        # verify the required parameter 'product' is set
        if cls().api_client.client_side_validation and ('product' not in local_var_params or  # noqa: E501
                                                        local_var_params['product'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `product` when calling `add_products`")  # noqa: E501


        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id'] # noqa: E501

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'product' in local_var_params:
            body_params['product'] = local_var_params['product']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/page/{id}/product', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def check_slug_availability(cls, slug, **kwargs):  # noqa: E501
        """Check Slug Availability  # noqa: E501


        :param slug: (required)
        :type slug: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'slug'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_slug_availability" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'slug' is set
        if cls().api_client.client_side_validation and ('slug' not in local_var_params or  # noqa: E501
                                                        local_var_params['slug'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `slug` when calling `check_slug_availability`")  # noqa: E501


        path_params = {}
        if 'slug' in local_var_params:
            path_params['slug'] = local_var_params['slug'] # noqa: E501

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
            '/page/check_slug_availability/{slug}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def create(cls, name, **kwargs):  # noqa: E501
        """Create Page  # noqa: E501


        :param name: Name of page (required)
        :type name: str
        :param description: The description of the page
        :type description: str
        :param amount: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
        :type amount: int
        :param slug: URL slug you would like to be associated with this page. Page will be accessible at https://paystack.com/pay/[slug]
        :type slug: str
        :param metadata: Stringified JSON object of custom data
        :type metadata: str
        :param redirect_url: If you would like Paystack to redirect to a URL upon successful payment, specify the URL here.
        :type redirect_url: str
        :param custom_fields: If you would like to accept custom fields, specify them here.
        :type custom_fields: list[object]
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'name',
            'description',
            'amount',
            'slug',
            'metadata',
            'redirect_url',
            'custom_fields'
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


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'name' in local_var_params:
            body_params['name'] = local_var_params['name']
        if 'description' in local_var_params:
            body_params['description'] = local_var_params['description']
        if 'amount' in local_var_params:
            body_params['amount'] = local_var_params['amount']
        if 'slug' in local_var_params:
            body_params['slug'] = local_var_params['slug']
        if 'metadata' in local_var_params:
            body_params['metadata'] = local_var_params['metadata']
        if 'redirect_url' in local_var_params:
            body_params['redirect_url'] = local_var_params['redirect_url']
        if 'custom_fields' in local_var_params:
            body_params['custom_fields'] = local_var_params['custom_fields']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/page', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def fetch(cls, id, **kwargs):  # noqa: E501
        """Fetch Page  # noqa: E501


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
            '/page/{id}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def list(cls, **kwargs):  # noqa: E501
        """List Pages  # noqa: E501


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
            '/page', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def update(cls, id, **kwargs):  # noqa: E501
        """Update Page  # noqa: E501


        :param id: (required)
        :type id: str
        :param name: Name of page
        :type name: str
        :param description: The description of the page
        :type description: str
        :param amount: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
        :type amount: int
        :param active: Set to false to deactivate page url
        :type active: bool
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
            'amount',
            'active'
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
        if 'amount' in local_var_params:
            body_params['amount'] = local_var_params['amount']
        if 'active' in local_var_params:
            body_params['active'] = local_var_params['active']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
            404: "Error",
        }

        return cls().api_client.call_api(
            '/page/{id}', 'PUT',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)

