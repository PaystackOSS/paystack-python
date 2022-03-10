# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from __future__ import absolute_import

import unittest

import paystack
from paystack.api.subscription_ import Subscription  # noqa: E501
from paystack.rest import ApiException


class TestSubscription(unittest.TestCase):
    """Subscription unit test stubs"""

    def setUp(self):
        self.api = paystack.api.subscription_.Subscription()  # noqa: E501

    def tearDown(self):
        pass

    def test_create(self):
        """Test case for create

        Create Subscription  # noqa: E501
        """
        pass

    def test_disable(self):
        """Test case for disable

        Disable Subscription  # noqa: E501
        """
        pass

    def test_enable(self):
        """Test case for enable

        Enable Subscription  # noqa: E501
        """
        pass

    def test_fetch(self):
        """Test case for fetch

        Fetch Subscription  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List Subscriptions  # noqa: E501
        """
        pass

    def test_manage_email(self):
        """Test case for manage_email

        Send Update Subscription Link  # noqa: E501
        """
        pass

    def test_manage_link(self):
        """Test case for manage_link

        Generate Update Subscription Link  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
