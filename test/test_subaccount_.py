# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from __future__ import absolute_import

import unittest

import paystack
from paystack.api.subaccount_ import Subaccount  # noqa: E501
from paystack.rest import ApiException


class TestSubaccount(unittest.TestCase):
    """Subaccount unit test stubs"""

    def setUp(self):
        self.api = paystack.api.subaccount_.Subaccount()  # noqa: E501

    def tearDown(self):
        pass

    def test_create(self):
        """Test case for create

        Create Subaccount  # noqa: E501
        """
        pass

    def test_fetch(self):
        """Test case for fetch

        Fetch Subaccount  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List Subaccounts  # noqa: E501
        """
        pass

    def test_update(self):
        """Test case for update

        Update Subaccount  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
