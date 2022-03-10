# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from __future__ import absolute_import

import unittest

import paystack
from paystack.api.dispute_ import Dispute  # noqa: E501
from paystack.rest import ApiException


class TestDispute(unittest.TestCase):
    """Dispute unit test stubs"""

    def setUp(self):
        self.api = paystack.api.dispute_.Dispute()  # noqa: E501

    def tearDown(self):
        pass

    def test_download(self):
        """Test case for download

        Export Disputes  # noqa: E501
        """
        pass

    def test_evidence(self):
        """Test case for evidence

        Add Evidence  # noqa: E501
        """
        pass

    def test_fetch(self):
        """Test case for fetch

        Fetch Dispute  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List Disputes  # noqa: E501
        """
        pass

    def test_resolve(self):
        """Test case for resolve

        Resolve a Dispute  # noqa: E501
        """
        pass

    def test_transaction(self):
        """Test case for transaction

        List Transaction Disputes  # noqa: E501
        """
        pass

    def test_update(self):
        """Test case for update

        Update Dispute  # noqa: E501
        """
        pass

    def test_upload_url(self):
        """Test case for upload_url

        Get Upload URL  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
