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
from paystack.models.page_product import PageProduct  # noqa: E501
from paystack.rest import ApiException

class TestPageProduct(unittest.TestCase):
    """PageProduct unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PageProduct
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = paystack.models.page_product.PageProduct()  # noqa: E501
        if include_optional :
            return PageProduct(
                product = [
                    ''
                    ]
            )
        else :
            return PageProduct(
                product = [
                    ''
                    ],
        )

    def testPageProduct(self):
        """Test PageProduct"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
