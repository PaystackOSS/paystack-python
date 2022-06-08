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


class Charge(object):
    """NOTE: This class is auto generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @classmethod
    def check(cls, reference, **kwargs):  # noqa: E501
        """Check pending charge  # noqa: E501


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
                    " to method check" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'reference' is set
        if cls().api_client.client_side_validation and ('reference' not in local_var_params or  # noqa: E501
                                                        local_var_params['reference'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `reference` when calling `check`")  # noqa: E501


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
            '/charge/{reference}', 'GET',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def create(cls, **kwargs):  # noqa: E501
        """Create Charge  # noqa: E501


        :param email: Customer's email address
        :type email: str
        :param amount: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
        :type amount: str
        :param authorization_code: An authorization code to charge.
        :type authorization_code: str
        :param pin: 4-digit PIN (send with a non-reusable authorization code)
        :type pin: str
        :param reference: Unique transaction reference. Only -, .`, = and alphanumeric characters allowed.
        :type reference: str
        :param birthday: The customer's birthday in the format YYYY-MM-DD e.g 2017-05-16
        :type birthday: datetime
        :param device_id: This is the unique identifier of the device a user uses in making payment.  Only -, .`, = and alphanumeric characters are allowed.
        :type device_id: str
        :param metadata: Stringified JSON object of custom data
        :type metadata: str
        :param bank:
        :type bank: Bank
        :param mobile_money:
        :type mobile_money: MobileMoney
        :param ussd:
        :type ussd: USSD
        :param eft:
        :type eft: EFT
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
            'pin',
            'reference',
            'birthday',
            'device_id',
            'metadata',
            'bank',
            'mobile_money',
            'ussd',
            'eft'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']


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
        if 'pin' in local_var_params:
            body_params['pin'] = local_var_params['pin']
        if 'reference' in local_var_params:
            body_params['reference'] = local_var_params['reference']
        if 'birthday' in local_var_params:
            body_params['birthday'] = local_var_params['birthday']
        if 'device_id' in local_var_params:
            body_params['device_id'] = local_var_params['device_id']
        if 'metadata' in local_var_params:
            body_params['metadata'] = local_var_params['metadata']
        if 'bank' in local_var_params:
            body_params['bank'] = local_var_params['bank']
        if 'mobile_money' in local_var_params:
            body_params['mobile_money'] = local_var_params['mobile_money']
        if 'ussd' in local_var_params:
            body_params['ussd'] = local_var_params['ussd']
        if 'eft' in local_var_params:
            body_params['eft'] = local_var_params['eft']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/charge', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def submit_address(cls, address, city, state, zipcode, reference, **kwargs):  # noqa: E501
        """Submit Address  # noqa: E501


        :param address: Customer's address (required)
        :type address: str
        :param city: Customer's city (required)
        :type city: str
        :param state: Customer's state (required)
        :type state: str
        :param zipcode: Customer's zipcode (required)
        :type zipcode: str
        :param reference: The reference of the ongoing transaction (required)
        :type reference: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'address',
            'city',
            'state',
            'zipcode',
            'reference'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method submit_address" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'address' is set
        if cls().api_client.client_side_validation and ('address' not in local_var_params or  # noqa: E501
                                                        local_var_params['address'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `address` when calling `submit_address`")  # noqa: E501
        # verify the required parameter 'city' is set
        if cls().api_client.client_side_validation and ('city' not in local_var_params or  # noqa: E501
                                                        local_var_params['city'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `city` when calling `submit_address`")  # noqa: E501
        # verify the required parameter 'state' is set
        if cls().api_client.client_side_validation and ('state' not in local_var_params or  # noqa: E501
                                                        local_var_params['state'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `state` when calling `submit_address`")  # noqa: E501
        # verify the required parameter 'zipcode' is set
        if cls().api_client.client_side_validation and ('zipcode' not in local_var_params or  # noqa: E501
                                                        local_var_params['zipcode'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `zipcode` when calling `submit_address`")  # noqa: E501
        # verify the required parameter 'reference' is set
        if cls().api_client.client_side_validation and ('reference' not in local_var_params or  # noqa: E501
                                                        local_var_params['reference'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `reference` when calling `submit_address`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'address' in local_var_params:
            body_params['address'] = local_var_params['address']
        if 'city' in local_var_params:
            body_params['city'] = local_var_params['city']
        if 'state' in local_var_params:
            body_params['state'] = local_var_params['state']
        if 'zipcode' in local_var_params:
            body_params['zipcode'] = local_var_params['zipcode']
        if 'reference' in local_var_params:
            body_params['reference'] = local_var_params['reference']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/charge/submit_address', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def submit_birthday(cls, birthday, reference, **kwargs):  # noqa: E501
        """Submit Birthday  # noqa: E501


        :param birthday: Customer's birthday in the format YYYY-MM-DD e.g 2016-09-21 (required)
        :type birthday: str
        :param reference: The reference of the ongoing transaction (required)
        :type reference: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'birthday',
            'reference'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method submit_birthday" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'birthday' is set
        if cls().api_client.client_side_validation and ('birthday' not in local_var_params or  # noqa: E501
                                                        local_var_params['birthday'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `birthday` when calling `submit_birthday`")  # noqa: E501
        # verify the required parameter 'reference' is set
        if cls().api_client.client_side_validation and ('reference' not in local_var_params or  # noqa: E501
                                                        local_var_params['reference'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `reference` when calling `submit_birthday`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'birthday' in local_var_params:
            body_params['birthday'] = local_var_params['birthday']
        if 'reference' in local_var_params:
            body_params['reference'] = local_var_params['reference']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/charge/submit_birthday', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def submit_otp(cls, otp, reference, **kwargs):  # noqa: E501
        """Submit OTP  # noqa: E501


        :param otp: Customer's OTP (required)
        :type otp: str
        :param reference: The reference of the ongoing transaction (required)
        :type reference: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'otp',
            'reference'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method submit_otp" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'otp' is set
        if cls().api_client.client_side_validation and ('otp' not in local_var_params or  # noqa: E501
                                                        local_var_params['otp'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `otp` when calling `submit_otp`")  # noqa: E501
        # verify the required parameter 'reference' is set
        if cls().api_client.client_side_validation and ('reference' not in local_var_params or  # noqa: E501
                                                        local_var_params['reference'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `reference` when calling `submit_otp`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'otp' in local_var_params:
            body_params['otp'] = local_var_params['otp']
        if 'reference' in local_var_params:
            body_params['reference'] = local_var_params['reference']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/charge/submit_otp', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def submit_phone(cls, phone, reference, **kwargs):  # noqa: E501
        """Submit Phone  # noqa: E501


        :param phone: Customer's mobile number (required)
        :type phone: str
        :param reference: The reference of the ongoing transaction (required)
        :type reference: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'phone',
            'reference'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method submit_phone" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'phone' is set
        if cls().api_client.client_side_validation and ('phone' not in local_var_params or  # noqa: E501
                                                        local_var_params['phone'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `phone` when calling `submit_phone`")  # noqa: E501
        # verify the required parameter 'reference' is set
        if cls().api_client.client_side_validation and ('reference' not in local_var_params or  # noqa: E501
                                                        local_var_params['reference'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `reference` when calling `submit_phone`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'phone' in local_var_params:
            body_params['phone'] = local_var_params['phone']
        if 'reference' in local_var_params:
            body_params['reference'] = local_var_params['reference']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/charge/submit_phone', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)


    @classmethod
    def submit_pin(cls, pin, reference, **kwargs):  # noqa: E501
        """Submit PIN  # noqa: E501


        :param pin: Customer's PIN (required)
        :type pin: str
        :param reference: Transaction reference that requires the PIN (required)
        :type reference: str
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        local_var_params = locals()

        all_params = [
            'pin',
            'reference'
        ]

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method submit_pin" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'pin' is set
        if cls().api_client.client_side_validation and ('pin' not in local_var_params or  # noqa: E501
                                                        local_var_params['pin'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pin` when calling `submit_pin`")  # noqa: E501
        # verify the required parameter 'reference' is set
        if cls().api_client.client_side_validation and ('reference' not in local_var_params or  # noqa: E501
                                                        local_var_params['reference'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `reference` when calling `submit_pin`")  # noqa: E501


        path_params = {}

        query_params = []

        form_params = []
        local_var_files = {}
        body_params = {}

        if 'pin' in local_var_params:
            body_params['pin'] = local_var_params['pin']
        if 'reference' in local_var_params:
            body_params['reference'] = local_var_params['reference']
        
        
        response_types_map = {
            200: "Response",
            401: "Error",
        }

        return cls().api_client.call_api(
            '/charge/submit_pin', 'POST',
            path_params,
            query_params,
            body=body_params,
            post_params=form_params,
            response_types_map=response_types_map)

