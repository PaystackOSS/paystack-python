# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from __future__ import absolute_import

import unittest

import paystack
from paystack.api.verification_ import Verification  # noqa: E501
from paystack.rest import ApiException


class TestVerification(unittest.TestCase):
    """Verification unit test stubs"""

    def setUp(self):
        self.api = paystack.api.verification_.Verification()  # noqa: E501

    def tearDown(self):
        pass

    def test_avs(self):
        """Test case for avs

        List States (AVS)  # noqa: E501
        """
        pass

    def test_bvn_match(self):
        """Test case for bvn_match

        Match Service  # noqa: E501
        """
        pass

    def test_fetch_banks(self):
        """Test case for fetch_banks

        Fetch Banks  # noqa: E501
        """
        pass

    def test_list_countries(self):
        """Test case for list_countries

        List Countries  # noqa: E501
        """
        pass

    def test_resolve_account_number(self):
        """Test case for resolve_account_number

        Resolve Account Number  # noqa: E501
        """
        pass

    def test_resolve_bvn(self):
        """Test case for resolve_bvn

        Resolve BVN  # noqa: E501
        """
        pass

    def test_resolve_card_bin(self):
        """Test case for resolve_card_bin

        Resolve Card BIN  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
