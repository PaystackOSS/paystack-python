# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from __future__ import absolute_import

import unittest

import paystack
from paystack.api.transaction_ import Transaction  # noqa: E501
from paystack.rest import ApiException


class TestTransaction(unittest.TestCase):
    """Transaction unit test stubs"""

    def setUp(self):
        self.api = paystack.api.transaction_.Transaction()  # noqa: E501

    def tearDown(self):
        pass

    def test_charge_authorization(self):
        """Test case for charge_authorization

        Charge Authorization  # noqa: E501
        """
        pass

    def test_check_authorization(self):
        """Test case for check_authorization

        Check Authorization  # noqa: E501
        """
        pass

    def test_download(self):
        """Test case for download

        Export Transactions  # noqa: E501
        """
        pass

    def test_event(self):
        """Test case for event

        Get Transaction Event  # noqa: E501
        """
        pass

    def test_fetch(self):
        """Test case for fetch

        Fetch Transaction  # noqa: E501
        """
        pass

    def test_initialize(self):
        """Test case for initialize

        Initialize Transaction  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List Transactions  # noqa: E501
        """
        pass

    def test_partial_debit(self):
        """Test case for partial_debit

        Partial Debit  # noqa: E501
        """
        pass

    def test_session(self):
        """Test case for session

        Get Transaction Session  # noqa: E501
        """
        pass

    def test_timeline(self):
        """Test case for timeline

        Fetch Transaction Timeline  # noqa: E501
        """
        pass

    def test_totals(self):
        """Test case for totals

        Transaction Totals  # noqa: E501
        """
        pass

    def test_verify(self):
        """Test case for verify

        Verify Transaction  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
