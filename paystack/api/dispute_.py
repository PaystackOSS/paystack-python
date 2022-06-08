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


class Dispute(object):
    """NOTE: This class is auto generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @classmethod
    def download(cls, **kwargs):  # noqa: E501
        """Export Disputes  # noqa: E501


        :param per_page: Number of records to fetch per page
        :type per_page: int
        :param page: The section to retrieve
        :type page: int
        :param status:
        :type status: str
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
            'status',
            '_from',
            'to'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']


        path_params = {}

        query_params = []
        if 'per_page' in local_var_params and local_var_params['per_page'] is not None:  # noqa: E501
            query_params.append(('perPage', local_var_params['per_page']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'status' in local_var_params and local_var_params['status'] is not None:  # noqa: E501
            query_params.append(('status', local_var_params['status']))  # noqa: E501
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
            '/dispute/export', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def evidence(cls, id, customer_email, customer_name, customer_phone, service_details, **kwargs):  # noqa: E501
        """Add Evidence  # noqa: E501


        :param id: Dispute ID (required)
        :type id: str
        :param customer_email: Customer email (required)
        :type customer_email: str
        :param customer_name: Customer name (required)
        :type customer_name: str
        :param customer_phone: Customer mobile number (required)
        :type customer_phone: str
        :param service_details: Details of service offered (required)
        :type service_details: str
        :param delivery_address: Delivery address
        :type delivery_address: str
        :param delivery_date: ISO 8601 representation of delivery date (YYYY-MM-DD)
        :type delivery_date: datetime
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'id',
            'customer_email',
            'customer_name',
            'customer_phone',
            'service_details',
            'delivery_address',
            'delivery_date'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method evidence" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if cls().api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `evidence`")  # noqa: E501
        # verify the required parameter 'customer_email' is set
        if cls().api_client.client_side_validation and ('customer_email' not in local_var_params or  # noqa: E501
                                                        local_var_params['customer_email'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `customer_email` when calling `evidence`")  # noqa: E501
        # verify the required parameter 'customer_name' is set
        if cls().api_client.client_side_validation and ('customer_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['customer_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `customer_name` when calling `evidence`")  # noqa: E501
        # verify the required parameter 'customer_phone' is set
        if cls().api_client.client_side_validation and ('customer_phone' not in local_var_params or  # noqa: E501
                                                        local_var_params['customer_phone'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `customer_phone` when calling `evidence`")  # noqa: E501
        # verify the required parameter 'service_details' is set
        if cls().api_client.client_side_validation and ('service_details' not in local_var_params or  # noqa: E501
                                                        local_var_params['service_details'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `service_details` when calling `evidence`")  # noqa: E501


        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id'] # noqa: E501

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'customer_email' in local_var_params:
            body_params['customer_email'] = local_var_params['customer_email']
        if 'customer_name' in local_var_params:
            body_params['customer_name'] = local_var_params['customer_name']
        if 'customer_phone' in local_var_params:
            body_params['customer_phone'] = local_var_params['customer_phone']
        if 'service_details' in local_var_params:
            body_params['service_details'] = local_var_params['service_details']
        if 'delivery_address' in local_var_params:
            body_params['delivery_address'] = local_var_params['delivery_address']
        if 'delivery_date' in local_var_params:
            body_params['delivery_date'] = local_var_params['delivery_date']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/dispute/{id}/evidence', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def fetch(cls, id, **kwargs):  # noqa: E501
        """Fetch Dispute  # noqa: E501


        :param id: Dispute ID (required)
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
            '/dispute/{id}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def list(cls, **kwargs):  # noqa: E501
        """List Disputes  # noqa: E501


        :param per_page: Number of records to fetch per page
        :type per_page: int
        :param page: The section to retrieve
        :type page: int
        :param status: Dispute Status. Acceptable values are awaiting-merchant-feedback, awaiting-bank-feedback, pending, resolved
        :type status: str
        :param transaction: Transaction ID
        :type transaction: str
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
            'status',
            'transaction',
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
        if 'status' in local_var_params and local_var_params['status'] is not None:  # noqa: E501
            query_params.append(('status', local_var_params['status']))  # noqa: E501
        if 'transaction' in local_var_params and local_var_params['transaction'] is not None:  # noqa: E501
            query_params.append(('transaction', local_var_params['transaction']))  # noqa: E501
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
            '/dispute', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def resolve(cls, id, resolution, message, refund_amount, uploaded_filename, **kwargs):  # noqa: E501
        """Resolve a Dispute  # noqa: E501


        :param id: Dispute ID (required)
        :type id: str
        :param resolution: Dispute resolution. Accepted values, merchant-accepted, declined (required)
        :type resolution: str
        :param message: Reason for resolving (required)
        :type message: str
        :param refund_amount: The amount to refund, in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR (required)
        :type refund_amount: str
        :param uploaded_filename: Filename of attachment returned via response from the Dispute upload URL (required)
        :type uploaded_filename: str
        :param evidence: Evidence Id for fraud claims
        :type evidence: int
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'id',
            'resolution',
            'message',
            'refund_amount',
            'uploaded_filename',
            'evidence'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resolve" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if cls().api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `resolve`")  # noqa: E501
        # verify the required parameter 'resolution' is set
        if cls().api_client.client_side_validation and ('resolution' not in local_var_params or  # noqa: E501
                                                        local_var_params['resolution'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `resolution` when calling `resolve`")  # noqa: E501
        # verify the required parameter 'message' is set
        if cls().api_client.client_side_validation and ('message' not in local_var_params or  # noqa: E501
                                                        local_var_params['message'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `message` when calling `resolve`")  # noqa: E501
        # verify the required parameter 'refund_amount' is set
        if cls().api_client.client_side_validation and ('refund_amount' not in local_var_params or  # noqa: E501
                                                        local_var_params['refund_amount'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `refund_amount` when calling `resolve`")  # noqa: E501
        # verify the required parameter 'uploaded_filename' is set
        if cls().api_client.client_side_validation and ('uploaded_filename' not in local_var_params or  # noqa: E501
                                                        local_var_params['uploaded_filename'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `uploaded_filename` when calling `resolve`")  # noqa: E501


        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id'] # noqa: E501

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'resolution' in local_var_params:
            body_params['resolution'] = local_var_params['resolution']
        if 'message' in local_var_params:
            body_params['message'] = local_var_params['message']
        if 'refund_amount' in local_var_params:
            body_params['refund_amount'] = local_var_params['refund_amount']
        if 'uploaded_filename' in local_var_params:
            body_params['uploaded_filename'] = local_var_params['uploaded_filename']
        if 'evidence' in local_var_params:
            body_params['evidence'] = local_var_params['evidence']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
            404: "Error",
        }

        return cls().api_client.call_api(
            '/dispute/{id}/resolve', 'PUT',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def transaction(cls, id, **kwargs):  # noqa: E501
        """List Transaction Disputes  # noqa: E501


        :param id: Transaction ID (required)
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
            '/dispute/transaction/{id}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def update(cls, id, refund_amount, **kwargs):  # noqa: E501
        """Update Dispute  # noqa: E501


        :param id: Dispute ID (required)
        :type id: str
        :param refund_amount: The amount to refund, in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR (required)
        :type refund_amount: str
        :param uploaded_filename: Filename of attachment returned via response from the Dispute upload URL
        :type uploaded_filename: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'id',
            'refund_amount',
            'uploaded_filename'
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
        # verify the required parameter 'refund_amount' is set
        if cls().api_client.client_side_validation and ('refund_amount' not in local_var_params or  # noqa: E501
                                                        local_var_params['refund_amount'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `refund_amount` when calling `update`")  # noqa: E501


        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id'] # noqa: E501

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'refund_amount' in local_var_params:
            body_params['refund_amount'] = local_var_params['refund_amount']
        if 'uploaded_filename' in local_var_params:
            body_params['uploaded_filename'] = local_var_params['uploaded_filename']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
            404: "Error",
        }

        return cls().api_client.call_api(
            '/dispute/{id}', 'PUT',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def upload_url(cls, id, **kwargs):  # noqa: E501
        """Get Upload URL  # noqa: E501


        :param id: Dispute ID (required)
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
                    " to method upload_url" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if cls().api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `upload_url`")  # noqa: E501


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
            '/dispute/{id}/upload_url', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)

