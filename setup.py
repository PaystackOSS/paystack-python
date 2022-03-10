# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "paystack"
VERSION = "0.1.0"
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
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Paystack"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501
    """
)
