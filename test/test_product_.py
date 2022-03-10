# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from __future__ import absolute_import

import unittest

import paystack
from paystack.api.product_ import Product  # noqa: E501
from paystack.rest import ApiException


class TestProduct(unittest.TestCase):
    """Product unit test stubs"""

    def setUp(self):
        self.api = paystack.api.product_.Product()  # noqa: E501

    def tearDown(self):
        pass

    def test_create(self):
        """Test case for create

        Create Product  # noqa: E501
        """
        pass

    def test_delete(self):
        """Test case for delete

        Delete Product  # noqa: E501
        """
        pass

    def test_fetch(self):
        """Test case for fetch

        Fetch Product  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List Products  # noqa: E501
        """
        pass

    def test_update(self):
        """Test case for update

        Update product  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
