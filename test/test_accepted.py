# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: techsupport@paystack.com
"""


from __future__ import absolute_import

import unittest
import datetime

import paystack
from paystack.models.accepted import Accepted  # noqa: E501
from paystack.rest import ApiException

class TestAccepted(unittest.TestCase):
    """Accepted unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Accepted
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = paystack.models.accepted.Accepted()  # noqa: E501
        if include_optional :
            return Accepted(
                status = True, 
                message = ''
            )
        else :
            return Accepted(
        )

    def testAccepted(self):
        """Test Accepted"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
