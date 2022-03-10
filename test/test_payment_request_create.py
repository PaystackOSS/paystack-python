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
from paystack.models.payment_request_create import PaymentRequestCreate  # noqa: E501
from paystack.rest import ApiException

class TestPaymentRequestCreate(unittest.TestCase):
    """PaymentRequestCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentRequestCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = paystack.models.payment_request_create.PaymentRequestCreate()  # noqa: E501
        if include_optional :
            return PaymentRequestCreate(
                customer = '', 
                amount = 56, 
                currency = '', 
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                description = '', 
                line_items = [
                    None
                    ], 
                tax = [
                    None
                    ], 
                send_notification = [
                    None
                    ], 
                draft = [
                    None
                    ], 
                has_invoice = [
                    None
                    ], 
                invoice_number = 56, 
                split_code = ''
            )
        else :
            return PaymentRequestCreate(
                customer = '',
        )

    def testPaymentRequestCreate(self):
        """Test PaymentRequestCreate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
