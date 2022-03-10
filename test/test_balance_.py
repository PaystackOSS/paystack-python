# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from __future__ import absolute_import

import unittest

import paystack
from paystack.api.balance_ import Balance  # noqa: E501
from paystack.rest import ApiException


class TestBalance(unittest.TestCase):
    """Balance unit test stubs"""

    def setUp(self):
        self.api = paystack.api.balance_.Balance()  # noqa: E501

    def tearDown(self):
        pass

    def test_fetch(self):
        """Test case for fetch

        Fetch Balance  # noqa: E501
        """
        pass

    def test_ledger(self):
        """Test case for ledger

        Balance Ledger  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
