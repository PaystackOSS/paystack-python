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
from paystack.models.plan_create import PlanCreate  # noqa: E501
from paystack.rest import ApiException

class TestPlanCreate(unittest.TestCase):
    """PlanCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PlanCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = paystack.models.plan_create.PlanCreate()  # noqa: E501
        if include_optional :
            return PlanCreate(
                name = '', 
                amount = 56, 
                interval = '', 
                description = True, 
                send_invoices = True, 
                send_sms = True, 
                currency = '', 
                invoice_limit = 56
            )
        else :
            return PlanCreate(
                name = '',
                amount = 56,
                interval = '',
        )

    def testPlanCreate(self):
        """Test PlanCreate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
