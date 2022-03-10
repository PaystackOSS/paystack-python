# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from __future__ import absolute_import

import unittest

import paystack
from paystack.api.transfer_ import Transfer  # noqa: E501
from paystack.rest import ApiException


class TestTransfer(unittest.TestCase):
    """Transfer unit test stubs"""

    def setUp(self):
        self.api = paystack.api.transfer_.Transfer()  # noqa: E501

    def tearDown(self):
        pass

    def test_bulk(self):
        """Test case for bulk

        Initiate Bulk Transfer  # noqa: E501
        """
        pass

    def test_disable_otp(self):
        """Test case for disable_otp

        Disable OTP requirement for Transfers  # noqa: E501
        """
        pass

    def test_disable_otp_finalize(self):
        """Test case for disable_otp_finalize

        Finalize Disabling of OTP requirement for Transfers  # noqa: E501
        """
        pass

    def test_download(self):
        """Test case for download

        Export Transfers  # noqa: E501
        """
        pass

    def test_enable_otp(self):
        """Test case for enable_otp

        Enable OTP requirement for Transfers  # noqa: E501
        """
        pass

    def test_fetch(self):
        """Test case for fetch

        Fetch Transfer  # noqa: E501
        """
        pass

    def test_finalize(self):
        """Test case for finalize

        Finalize Transfer  # noqa: E501
        """
        pass

    def test_initiate(self):
        """Test case for initiate

        Initiate Transfer  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List Transfers  # noqa: E501
        """
        pass

    def test_resend_otp(self):
        """Test case for resend_otp

        Resend OTP for Transfer  # noqa: E501
        """
        pass

    def test_verify(self):
        """Test case for verify

        Verify Transfer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
