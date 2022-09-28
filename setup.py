# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: techsupport@paystack.com
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "paystack-sdk"
VERSION = "1.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.25.3", "six >= 1.10", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Paystack",
    author="Paystack Integration",
    author_email="techsupport@paystack.com",
    url="https://github.com/PaystackOSS/paystack-python",
    keywords=["Paystack", "Transaction", "Split Payment", "Customer", "Dedicated Virtual Account", "Subaccount",
    "Plan", "Subscription", "Product", "Page", "Payment Request", "Settlement", "Transfer Recipient", "Transfer",
    "Balance", "Charge", "Bulk Charge", "Integration", "Refund", "Dispute", "Verification"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501
    """
)
