# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from __future__ import absolute_import

import unittest

import paystack
from paystack.api.settlement_ import Settlement  # noqa: E501
from paystack.rest import ApiException


class TestSettlement(unittest.TestCase):
    """Settlement unit test stubs"""

    def setUp(self):
        self.api = paystack.api.settlement_.Settlement()  # noqa: E501

    def tearDown(self):
        pass

    def test_fetch(self):
        """Test case for fetch

        Fetch Settlements  # noqa: E501
        """
        pass

    def test_transaction(self):
        """Test case for transaction

        Settlement Transactions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
