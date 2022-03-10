# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from __future__ import absolute_import

import unittest

import paystack
from paystack.api.payment_request_ import PaymentRequest  # noqa: E501
from paystack.rest import ApiException


class TestPaymentRequest(unittest.TestCase):
    """PaymentRequest unit test stubs"""

    def setUp(self):
        self.api = paystack.api.payment_request_.PaymentRequest()  # noqa: E501

    def tearDown(self):
        pass

    def test_archive(self):
        """Test case for archive

        Archive Payment Request  # noqa: E501
        """
        pass

    def test_create(self):
        """Test case for create

        Create Payment Request  # noqa: E501
        """
        pass

    def test_fetch(self):
        """Test case for fetch

        Fetch Payment Request  # noqa: E501
        """
        pass

    def test_finalize(self):
        """Test case for finalize

        Finalize Payment Request  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List Payment Request  # noqa: E501
        """
        pass

    def test_notify(self):
        """Test case for notify

        Send Notification  # noqa: E501
        """
        pass

    def test_totals(self):
        """Test case for totals

        Payment Request Total  # noqa: E501
        """
        pass

    def test_update(self):
        """Test case for update

        Update Payment Request  # noqa: E501
        """
        pass

    def test_verify(self):
        """Test case for verify

        Verify Payment Request  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
