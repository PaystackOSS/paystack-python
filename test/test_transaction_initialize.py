# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from __future__ import absolute_import

import unittest
import datetime

import paystack
from paystack.models.transaction_initialize import TransactionInitialize  # noqa: E501
from paystack.rest import ApiException

class TestTransactionInitialize(unittest.TestCase):
    """TransactionInitialize unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TransactionInitialize
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = paystack.models.transaction_initialize.TransactionInitialize()  # noqa: E501
        if include_optional :
            return TransactionInitialize(
                email = '', 
                amount = 56, 
                currency = '', 
                reference = '', 
                callback_url = '', 
                plan = '', 
                invoice_limit = 56, 
                metadata = '', 
                channels = [
                    ''
                    ], 
                split_code = '', 
                subaccount = '', 
                transaction_charge = '', 
                bearer = ''
            )
        else :
            return TransactionInitialize(
                email = '',
                amount = 56,
        )

    def testTransactionInitialize(self):
        """Test TransactionInitialize"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
