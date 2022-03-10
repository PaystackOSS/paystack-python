# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from __future__ import absolute_import

import unittest

import paystack
from paystack.api.transfer_recipient_ import TransferRecipient  # noqa: E501
from paystack.rest import ApiException


class TestTransferRecipient(unittest.TestCase):
    """TransferRecipient unit test stubs"""

    def setUp(self):
        self.api = paystack.api.transfer_recipient_.TransferRecipient()  # noqa: E501

    def tearDown(self):
        pass

    def test_bulk(self):
        """Test case for bulk

        Bulk Create Transfer Recipient  # noqa: E501
        """
        pass

    def test_create(self):
        """Test case for create

        Create Transfer Recipient  # noqa: E501
        """
        pass

    def test_fetch(self):
        """Test case for fetch

        Fetch Transfer recipient  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List Transfer Recipients  # noqa: E501
        """
        pass

    def test_transferrecipient_code_delete(self):
        """Test case for transferrecipient_code_delete

        Delete Transfer Recipient  # noqa: E501
        """
        pass

    def test_transferrecipient_code_put(self):
        """Test case for transferrecipient_code_put

        Update Transfer recipient  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
