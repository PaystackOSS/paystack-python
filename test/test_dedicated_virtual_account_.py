# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from __future__ import absolute_import

import unittest

import paystack
from paystack.api.dedicated_virtual_account_ import DedicatedVirtualAccount  # noqa: E501
from paystack.rest import ApiException


class TestDedicatedVirtualAccount(unittest.TestCase):
    """DedicatedVirtualAccount unit test stubs"""

    def setUp(self):
        self.api = paystack.api.dedicated_virtual_account_.DedicatedVirtualAccount()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_split(self):
        """Test case for add_split

        Split Dedicated Account Transaction  # noqa: E501
        """
        pass

    def test_available_providers(self):
        """Test case for available_providers

        Fetch Bank Providers  # noqa: E501
        """
        pass

    def test_create(self):
        """Test case for create

        Create Dedicated Account  # noqa: E501
        """
        pass

    def test_deactivate(self):
        """Test case for deactivate

        Deactivate Dedicated Account  # noqa: E501
        """
        pass

    def test_fetch(self):
        """Test case for fetch

        Fetch Dedicated Account  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List Dedicated Accounts  # noqa: E501
        """
        pass

    def test_remove_split(self):
        """Test case for remove_split

        Remove Split from Dedicated Account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
