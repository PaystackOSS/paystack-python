# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from __future__ import absolute_import

import unittest

import paystack
from paystack.api.split_ import Split  # noqa: E501
from paystack.rest import ApiException


class TestSplit(unittest.TestCase):
    """Split unit test stubs"""

    def setUp(self):
        self.api = paystack.api.split_.Split()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_subaccount(self):
        """Test case for add_subaccount

        Add Subaccount to Split  # noqa: E501
        """
        pass

    def test_create(self):
        """Test case for create

        Create Split  # noqa: E501
        """
        pass

    def test_fetch(self):
        """Test case for fetch

        Fetch Split  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List/Search Splits  # noqa: E501
        """
        pass

    def test_remove_subaccount(self):
        """Test case for remove_subaccount

        Remove Subaccount from split  # noqa: E501
        """
        pass

    def test_update(self):
        """Test case for update

        Update Split  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
