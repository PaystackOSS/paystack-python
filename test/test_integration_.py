# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from __future__ import absolute_import

import unittest

import paystack
from paystack.api.integration_ import Integration  # noqa: E501
from paystack.rest import ApiException


class TestIntegration(unittest.TestCase):
    """Integration unit test stubs"""

    def setUp(self):
        self.api = paystack.api.integration_.Integration()  # noqa: E501

    def tearDown(self):
        pass

    def test_fetch_payment_session_timeout(self):
        """Test case for fetch_payment_session_timeout

        Fetch Payment Session Timeout  # noqa: E501
        """
        pass

    def test_update_payment_session_timeout(self):
        """Test case for update_payment_session_timeout

        Update Payment Session Timeout  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
