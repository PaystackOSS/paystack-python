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


class Transfer(object):
    """NOTE: This class is auto generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @classmethod
    def bulk(cls, **kwargs):  # noqa: E501
        """Initiate Bulk Transfer  # noqa: E501


        :param source: Where should we transfer from? Only balance is allowed for now
        :type source: str
        :param transfers: A list of transfer object. Each object should contain amount, recipient, and reference
        :type transfers: list[TransferInitiate]
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'source',
            'transfers'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bulk" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'source' in local_var_params:
            body_params['source'] = local_var_params['source']
        if 'transfers' in local_var_params:
            body_params['transfers'] = local_var_params['transfers']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/transfer/bulk', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def disable_otp(cls, **kwargs):  # noqa: E501
        """Disable OTP requirement for Transfers  # noqa: E501


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
                    " to method disable_otp" % key
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
        }

        return cls().api_client.call_api(
            '/transfer/disable_otp', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def disable_otp_finalize(cls, otp, **kwargs):  # noqa: E501
        """Finalize Disabling of OTP requirement for Transfers  # noqa: E501


        :param otp: OTP sent to business phone to verify disabling OTP requirement (required)
        :type otp: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'otp'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method disable_otp_finalize" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'otp' is set
        if cls().api_client.client_side_validation and ('otp' not in local_var_params or  # noqa: E501
                                                        local_var_params['otp'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `otp` when calling `disable_otp_finalize`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'otp' in local_var_params:
            body_params['otp'] = local_var_params['otp']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/transfer/disable_otp_finalize', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def download(cls, **kwargs):  # noqa: E501
        """Export Transfers  # noqa: E501


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
            '/transfer/export', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def enable_otp(cls, **kwargs):  # noqa: E501
        """Enable OTP requirement for Transfers  # noqa: E501


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
                    " to method enable_otp" % key
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
        }

        return cls().api_client.call_api(
            '/transfer/enable_otp', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def fetch(cls, code, **kwargs):  # noqa: E501
        """Fetch Transfer  # noqa: E501


        :param code: Transfer code (required)
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
            '/transfer/{code}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def finalize(cls, transfer_code, otp, **kwargs):  # noqa: E501
        """Finalize Transfer  # noqa: E501


        :param transfer_code: The transfer code you want to finalize (required)
        :type transfer_code: str
        :param otp: OTP sent to business phone to verify transfer (required)
        :type otp: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'transfer_code',
            'otp'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method finalize" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'transfer_code' is set
        if cls().api_client.client_side_validation and ('transfer_code' not in local_var_params or  # noqa: E501
                                                        local_var_params['transfer_code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `transfer_code` when calling `finalize`")  # noqa: E501
        # verify the required parameter 'otp' is set
        if cls().api_client.client_side_validation and ('otp' not in local_var_params or  # noqa: E501
                                                        local_var_params['otp'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `otp` when calling `finalize`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'transfer_code' in local_var_params:
            body_params['transfer_code'] = local_var_params['transfer_code']
        if 'otp' in local_var_params:
            body_params['otp'] = local_var_params['otp']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/transfer/finalize_transfer', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def initiate(cls, source, amount, recipient, **kwargs):  # noqa: E501
        """Initiate Transfer  # noqa: E501


        :param source: Where should we transfer from? Only balance is allowed for now (required)
        :type source: str
        :param amount: Amount to transfer in kobo if currency is NGN and pesewas if currency is GHS. (required)
        :type amount: str
        :param recipient: The transfer recipient's code (required)
        :type recipient: str
        :param reason: The reason or narration for the transfer.
        :type reason: str
        :param currency: Specify the currency of the transfer. Defaults to NGN.
        :type currency: str
        :param reference: If specified, the field should be a unique identifier (in lowercase) for the object.  Only -,_ and alphanumeric characters are allowed.
        :type reference: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'source',
            'amount',
            'recipient',
            'reason',
            'currency',
            'reference'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method initiate" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'source' is set
        if cls().api_client.client_side_validation and ('source' not in local_var_params or  # noqa: E501
                                                        local_var_params['source'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `source` when calling `initiate`")  # noqa: E501
        # verify the required parameter 'amount' is set
        if cls().api_client.client_side_validation and ('amount' not in local_var_params or  # noqa: E501
                                                        local_var_params['amount'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `amount` when calling `initiate`")  # noqa: E501
        # verify the required parameter 'recipient' is set
        if cls().api_client.client_side_validation and ('recipient' not in local_var_params or  # noqa: E501
                                                        local_var_params['recipient'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `recipient` when calling `initiate`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'source' in local_var_params:
            body_params['source'] = local_var_params['source']
        if 'amount' in local_var_params:
            body_params['amount'] = local_var_params['amount']
        if 'recipient' in local_var_params:
            body_params['recipient'] = local_var_params['recipient']
        if 'reason' in local_var_params:
            body_params['reason'] = local_var_params['reason']
        if 'currency' in local_var_params:
            body_params['currency'] = local_var_params['currency']
        if 'reference' in local_var_params:
            body_params['reference'] = local_var_params['reference']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/transfer', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def list(cls, **kwargs):  # noqa: E501
        """List Transfers  # noqa: E501


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
            '/transfer', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def resend_otp(cls, transfer_code, reason, **kwargs):  # noqa: E501
        """Resend OTP for Transfer  # noqa: E501


        :param transfer_code: The transfer code that requires an OTP validation (required)
        :type transfer_code: str
        :param reason: Either resend_otp or transfer (required)
        :type reason: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'transfer_code',
            'reason'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resend_otp" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'transfer_code' is set
        if cls().api_client.client_side_validation and ('transfer_code' not in local_var_params or  # noqa: E501
                                                        local_var_params['transfer_code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `transfer_code` when calling `resend_otp`")  # noqa: E501
        # verify the required parameter 'reason' is set
        if cls().api_client.client_side_validation and ('reason' not in local_var_params or  # noqa: E501
                                                        local_var_params['reason'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `reason` when calling `resend_otp`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'transfer_code' in local_var_params:
            body_params['transfer_code'] = local_var_params['transfer_code']
        if 'reason' in local_var_params:
            body_params['reason'] = local_var_params['reason']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/transfer/resend_otp', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def verify(cls, reference, **kwargs):  # noqa: E501
        """Verify Transfer  # noqa: E501


        :param reference: (required)
        :type reference: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'reference'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method verify" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'reference' is set
        if cls().api_client.client_side_validation and ('reference' not in local_var_params or  # noqa: E501
                                                        local_var_params['reference'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `reference` when calling `verify`")  # noqa: E501


        path_params = {}
        if 'reference' in local_var_params:
            path_params['reference'] = local_var_params['reference'] # noqa: E501

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
            '/transfer/verify/{reference}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)

