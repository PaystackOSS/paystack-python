# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from __future__ import absolute_import

import unittest

import paystack
from paystack.api.refund_ import Refund  # noqa: E501
from paystack.rest import ApiException


class TestRefund(unittest.TestCase):
    """Refund unit test stubs"""

    def setUp(self):
        self.api = paystack.api.refund_.Refund()  # noqa: E501

    def tearDown(self):
        pass

    def test_create(self):
        """Test case for create

        Create Refund  # noqa: E501
        """
        pass

    def test_fetch(self):
        """Test case for fetch

        Fetch Refund  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List Refunds  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
