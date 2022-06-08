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


class Transaction(object):
    """NOTE: This class is auto generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @classmethod
    def charge_authorization(cls, email, amount, authorization_code, **kwargs):  # noqa: E501
        """Charge Authorization  # noqa: E501


        :param email: Customer's email address (required)
        :type email: str
        :param amount: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR (required)
        :type amount: int
        :param authorization_code: Valid authorization code to charge (required)
        :type authorization_code: str
        :param reference: Unique transaction reference. Only -, ., = and alphanumeric characters allowed.
        :type reference: str
        :param currency: The transaction currency
        :type currency: str
        :param metadata: Stringified JSON object of custom data
        :type metadata: str
        :param split_code: The split code of the transaction split
        :type split_code: str
        :param subaccount: The code for the subaccount that owns the payment
        :type subaccount: str
        :param transaction_charge: A flat fee to charge the subaccount for a transaction.  This overrides the split percentage set when the subaccount was created
        :type transaction_charge: str
        :param bearer: The beare of the transaction charge
        :type bearer: str
        :param queue: If you are making a scheduled charge call, it is a good idea to queue them so the processing system does not get overloaded causing transaction processing errors.
        :type queue: bool
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'email',
            'amount',
            'authorization_code',
            'reference',
            'currency',
            'metadata',
            'split_code',
            'subaccount',
            'transaction_charge',
            'bearer',
            'queue'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method charge_authorization" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'email' is set
        if cls().api_client.client_side_validation and ('email' not in local_var_params or  # noqa: E501
                                                        local_var_params['email'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `email` when calling `charge_authorization`")  # noqa: E501
        # verify the required parameter 'amount' is set
        if cls().api_client.client_side_validation and ('amount' not in local_var_params or  # noqa: E501
                                                        local_var_params['amount'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `amount` when calling `charge_authorization`")  # noqa: E501
        # verify the required parameter 'authorization_code' is set
        if cls().api_client.client_side_validation and ('authorization_code' not in local_var_params or  # noqa: E501
                                                        local_var_params['authorization_code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `authorization_code` when calling `charge_authorization`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'email' in local_var_params:
            body_params['email'] = local_var_params['email']
        if 'amount' in local_var_params:
            body_params['amount'] = local_var_params['amount']
        if 'authorization_code' in local_var_params:
            body_params['authorization_code'] = local_var_params['authorization_code']
        if 'reference' in local_var_params:
            body_params['reference'] = local_var_params['reference']
        if 'currency' in local_var_params:
            body_params['currency'] = local_var_params['currency']
        if 'metadata' in local_var_params:
            body_params['metadata'] = local_var_params['metadata']
        if 'split_code' in local_var_params:
            body_params['split_code'] = local_var_params['split_code']
        if 'subaccount' in local_var_params:
            body_params['subaccount'] = local_var_params['subaccount']
        if 'transaction_charge' in local_var_params:
            body_params['transaction_charge'] = local_var_params['transaction_charge']
        if 'bearer' in local_var_params:
            body_params['bearer'] = local_var_params['bearer']
        if 'queue' in local_var_params:
            body_params['queue'] = local_var_params['queue']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/transaction/charge_authorization', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def check_authorization(cls, email, amount, **kwargs):  # noqa: E501
        """Check Authorization  # noqa: E501


        :param email: Customer's email address (required)
        :type email: str
        :param amount: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR (required)
        :type amount: int
        :param authorization_code: Valid authorization code to charge
        :type authorization_code: str
        :param currency: The transaction currency
        :type currency: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'email',
            'amount',
            'authorization_code',
            'currency'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_authorization" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'email' is set
        if cls().api_client.client_side_validation and ('email' not in local_var_params or  # noqa: E501
                                                        local_var_params['email'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `email` when calling `check_authorization`")  # noqa: E501
        # verify the required parameter 'amount' is set
        if cls().api_client.client_side_validation and ('amount' not in local_var_params or  # noqa: E501
                                                        local_var_params['amount'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `amount` when calling `check_authorization`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'email' in local_var_params:
            body_params['email'] = local_var_params['email']
        if 'amount' in local_var_params:
            body_params['amount'] = local_var_params['amount']
        if 'authorization_code' in local_var_params:
            body_params['authorization_code'] = local_var_params['authorization_code']
        if 'currency' in local_var_params:
            body_params['currency'] = local_var_params['currency']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/transaction/check_authorization', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def download(cls, **kwargs):  # noqa: E501
        """Export Transactions  # noqa: E501


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
            '/transaction/export', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def event(cls, id, **kwargs):  # noqa: E501
        """Get Transaction Event  # noqa: E501


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
                    " to method event" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if cls().api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `event`")  # noqa: E501


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
            '/transaction/{id}/event', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def fetch(cls, id, **kwargs):  # noqa: E501
        """Fetch Transaction  # noqa: E501


        :param id: The ID of the transaction to fetch (required)
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
            '/transaction/{id}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def initialize(cls, email, amount, **kwargs):  # noqa: E501
        """Initialize Transaction  # noqa: E501

        Create a new transaction  # noqa: E501

        :param email: Customer's email address (required)
        :type email: str
        :param amount: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR (required)
        :type amount: int
        :param currency: The transaction currency
        :type currency: str
        :param reference: Unique transaction reference. Only -, ., = and alphanumeric characters allowed.
        :type reference: str
        :param callback_url: Fully qualified url, e.g. https://example.com/ . Use this to override the callback url provided on the dashboard for this transaction
        :type callback_url: str
        :param plan: If transaction is to create a subscription to a predefined plan, provide plan code here.  This would invalidate the value provided in amount
        :type plan: str
        :param invoice_limit: Number of times to charge customer during subscription to plan
        :type invoice_limit: int
        :param metadata: Stringified JSON object of custom data
        :type metadata: str
        :param channels: An array of payment channels to control what channels you want to make available to the user to make a payment with
        :type channels: list[str]
        :param split_code: The split code of the transaction split
        :type split_code: str
        :param subaccount: The code for the subaccount that owns the payment
        :type subaccount: str
        :param transaction_charge: A flat fee to charge the subaccount for a transaction.  This overrides the split percentage set when the subaccount was created
        :type transaction_charge: str
        :param bearer: The beare of the transaction charge
        :type bearer: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'email',
            'amount',
            'currency',
            'reference',
            'callback_url',
            'plan',
            'invoice_limit',
            'metadata',
            'channels',
            'split_code',
            'subaccount',
            'transaction_charge',
            'bearer'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method initialize" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'email' is set
        if cls().api_client.client_side_validation and ('email' not in local_var_params or  # noqa: E501
                                                        local_var_params['email'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `email` when calling `initialize`")  # noqa: E501
        # verify the required parameter 'amount' is set
        if cls().api_client.client_side_validation and ('amount' not in local_var_params or  # noqa: E501
                                                        local_var_params['amount'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `amount` when calling `initialize`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'email' in local_var_params:
            body_params['email'] = local_var_params['email']
        if 'amount' in local_var_params:
            body_params['amount'] = local_var_params['amount']
        if 'currency' in local_var_params:
            body_params['currency'] = local_var_params['currency']
        if 'reference' in local_var_params:
            body_params['reference'] = local_var_params['reference']
        if 'callback_url' in local_var_params:
            body_params['callback_url'] = local_var_params['callback_url']
        if 'plan' in local_var_params:
            body_params['plan'] = local_var_params['plan']
        if 'invoice_limit' in local_var_params:
            body_params['invoice_limit'] = local_var_params['invoice_limit']
        if 'metadata' in local_var_params:
            body_params['metadata'] = local_var_params['metadata']
        if 'channels' in local_var_params:
            body_params['channels'] = local_var_params['channels']
        if 'split_code' in local_var_params:
            body_params['split_code'] = local_var_params['split_code']
        if 'subaccount' in local_var_params:
            body_params['subaccount'] = local_var_params['subaccount']
        if 'transaction_charge' in local_var_params:
            body_params['transaction_charge'] = local_var_params['transaction_charge']
        if 'bearer' in local_var_params:
            body_params['bearer'] = local_var_params['bearer']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/transaction/initialize', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def list(cls, **kwargs):  # noqa: E501
        """List Transactions  # noqa: E501


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
            '/transaction', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def partial_debit(cls, email, amount, authorization_code, currency, **kwargs):  # noqa: E501
        """Partial Debit  # noqa: E501


        :param email: Customer's email address (required)
        :type email: str
        :param amount: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR (required)
        :type amount: int
        :param authorization_code: Valid authorization code to charge (required)
        :type authorization_code: str
        :param currency: The transaction currency (required)
        :type currency: str
        :param reference: Unique transaction reference. Only -, ., = and alphanumeric characters allowed.
        :type reference: str
        :param at_least: Minimum amount to charge
        :type at_least: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'email',
            'amount',
            'authorization_code',
            'currency',
            'reference',
            'at_least'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method partial_debit" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'email' is set
        if cls().api_client.client_side_validation and ('email' not in local_var_params or  # noqa: E501
                                                        local_var_params['email'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `email` when calling `partial_debit`")  # noqa: E501
        # verify the required parameter 'amount' is set
        if cls().api_client.client_side_validation and ('amount' not in local_var_params or  # noqa: E501
                                                        local_var_params['amount'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `amount` when calling `partial_debit`")  # noqa: E501
        # verify the required parameter 'authorization_code' is set
        if cls().api_client.client_side_validation and ('authorization_code' not in local_var_params or  # noqa: E501
                                                        local_var_params['authorization_code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `authorization_code` when calling `partial_debit`")  # noqa: E501
        # verify the required parameter 'currency' is set
        if cls().api_client.client_side_validation and ('currency' not in local_var_params or  # noqa: E501
                                                        local_var_params['currency'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `currency` when calling `partial_debit`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'email' in local_var_params:
            body_params['email'] = local_var_params['email']
        if 'amount' in local_var_params:
            body_params['amount'] = local_var_params['amount']
        if 'authorization_code' in local_var_params:
            body_params['authorization_code'] = local_var_params['authorization_code']
        if 'currency' in local_var_params:
            body_params['currency'] = local_var_params['currency']
        if 'reference' in local_var_params:
            body_params['reference'] = local_var_params['reference']
        if 'at_least' in local_var_params:
            body_params['at_least'] = local_var_params['at_least']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/transaction/partial_debit', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def session(cls, id, **kwargs):  # noqa: E501
        """Get Transaction Session  # noqa: E501


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
                    " to method session" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if cls().api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `session`")  # noqa: E501


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
            '/transaction/{id}/session', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def timeline(cls, id_or_reference, **kwargs):  # noqa: E501
        """Fetch Transaction Timeline  # noqa: E501


        :param id_or_reference: (required)
        :type id_or_reference: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'id_or_reference'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method timeline" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id_or_reference' is set
        if cls().api_client.client_side_validation and ('id_or_reference' not in local_var_params or  # noqa: E501
                                                        local_var_params['id_or_reference'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id_or_reference` when calling `timeline`")  # noqa: E501


        path_params = {}
        if 'id_or_reference' in local_var_params:
            path_params['id_or_reference'] = local_var_params['id_or_reference'] # noqa: E501

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
            '/transaction/timeline/{id_or_reference}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def totals(cls, **kwargs):  # noqa: E501
        """Transaction Totals  # noqa: E501


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
                    " to method totals" % key
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
            '/transaction/totals', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def verify(cls, reference, **kwargs):  # noqa: E501
        """Verify Transaction  # noqa: E501


        :param reference: The transaction reference to verify (required)
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
            '/transaction/verify/{reference}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)

