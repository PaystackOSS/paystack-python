# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from __future__ import absolute_import

import unittest

import paystack
from paystack.api.charge_ import Charge  # noqa: E501
from paystack.rest import ApiException


class TestCharge(unittest.TestCase):
    """Charge unit test stubs"""

    def setUp(self):
        self.api = paystack.api.charge_.Charge()  # noqa: E501

    def tearDown(self):
        pass

    def test_check(self):
        """Test case for check

        Check pending charge  # noqa: E501
        """
        pass

    def test_create(self):
        """Test case for create

        Create Charge  # noqa: E501
        """
        pass

    def test_submit_address(self):
        """Test case for submit_address

        Submit Address  # noqa: E501
        """
        pass

    def test_submit_birthday(self):
        """Test case for submit_birthday

        Submit Birthday  # noqa: E501
        """
        pass

    def test_submit_otp(self):
        """Test case for submit_otp

        Submit OTP  # noqa: E501
        """
        pass

    def test_submit_phone(self):
        """Test case for submit_phone

        Submit Phone  # noqa: E501
        """
        pass

    def test_submit_pin(self):
        """Test case for submit_pin

        Submit PIN  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
