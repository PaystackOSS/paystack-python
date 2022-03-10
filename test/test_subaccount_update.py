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
from paystack.models.subaccount_update import SubaccountUpdate  # noqa: E501
from paystack.rest import ApiException

class TestSubaccountUpdate(unittest.TestCase):
    """SubaccountUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SubaccountUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = paystack.models.subaccount_update.SubaccountUpdate()  # noqa: E501
        if include_optional :
            return SubaccountUpdate(
                business_name = '', 
                settlement_bank = '', 
                account_number = '', 
                active = True, 
                percentage_charge = 1.337, 
                description = '', 
                primary_contact_email = '', 
                primary_contact_name = '', 
                primary_contact_phone = '', 
                metadata = ''
            )
        else :
            return SubaccountUpdate(
        )

    def testSubaccountUpdate(self):
        """Test SubaccountUpdate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
