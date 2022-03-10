# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from __future__ import absolute_import

import unittest

import paystack
from paystack.api.customer_ import Customer  # noqa: E501
from paystack.rest import ApiException


class TestCustomer(unittest.TestCase):
    """Customer unit test stubs"""

    def setUp(self):
        self.api = paystack.api.customer_.Customer()  # noqa: E501

    def tearDown(self):
        pass

    def test_create(self):
        """Test case for create

        Create Customer  # noqa: E501
        """
        pass

    def test_deactivate_authorization(self):
        """Test case for deactivate_authorization

        Deactivate Authorization  # noqa: E501
        """
        pass

    def test_fetch(self):
        """Test case for fetch

        Fetch Customer  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List Customers  # noqa: E501
        """
        pass

    def test_risk_action(self):
        """Test case for risk_action

        White/blacklist Customer  # noqa: E501
        """
        pass

    def test_update(self):
        """Test case for update

        Update Customer  # noqa: E501
        """
        pass

    def test_validatte(self):
        """Test case for validatte

        Validate Customer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
