# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from __future__ import absolute_import

import unittest

import paystack
from paystack.api.bulk_charge_ import BulkCharge  # noqa: E501
from paystack.rest import ApiException


class TestBulkCharge(unittest.TestCase):
    """BulkCharge unit test stubs"""

    def setUp(self):
        self.api = paystack.api.bulk_charge_.BulkCharge()  # noqa: E501

    def tearDown(self):
        pass

    def test_charges(self):
        """Test case for charges

        Fetch Charges in a Batch  # noqa: E501
        """
        pass

    def test_fetch(self):
        """Test case for fetch

        Fetch Bulk Charge Batch  # noqa: E501
        """
        pass

    def test_initiate(self):
        """Test case for initiate

        Initiate Bulk Charge  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List Bulk Charge Batches  # noqa: E501
        """
        pass

    def test_pause(self):
        """Test case for pause

        Pause Bulk Charge Batch  # noqa: E501
        """
        pass

    def test_resume(self):
        """Test case for resume

        Resume Bulk Charge Batch  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
