# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from __future__ import absolute_import

import unittest

import paystack
from paystack.api.page_ import Page  # noqa: E501
from paystack.rest import ApiException


class TestPage(unittest.TestCase):
    """Page unit test stubs"""

    def setUp(self):
        self.api = paystack.api.page_.Page()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_products(self):
        """Test case for add_products

        Add Products  # noqa: E501
        """
        pass

    def test_check_slug_availability(self):
        """Test case for check_slug_availability

        Check Slug Availability  # noqa: E501
        """
        pass

    def test_create(self):
        """Test case for create

        Create Page  # noqa: E501
        """
        pass

    def test_fetch(self):
        """Test case for fetch

        Fetch Page  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List Pages  # noqa: E501
        """
        pass

    def test_update(self):
        """Test case for update

        Update Page  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
