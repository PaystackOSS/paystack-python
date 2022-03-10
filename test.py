from __future__ import print_function
import paystack
from paystack.rest import ApiException
from pprint import pprint

paystack.api_key = 'sk_test_xxxx'


code='CUS_xxxx'
email="confirm@test.com"
first_name="Confirm"
last_name = "Test"

try:
    # List all customers
    response = paystack.Customer.fetch(code)
    # response = paystack.Customer.create(
    #         email=email,
    #         first_name=first_name,
    #         last_name=last_name
    #     )
    pprint(response)
except ApiException as e:
    print("Exception when calling Customer->list: %s\n" % e)
