# paystack.Charge

All URIs are relative to *https://api.paystack.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check**](Charge.md#check) | **GET** /charge/{reference} | Check pending charge
[**create**](Charge.md#create) | **POST** /charge | Create Charge
[**submit_address**](Charge.md#submit_address) | **POST** /charge/submit_address | Submit Address
[**submit_birthday**](Charge.md#submit_birthday) | **POST** /charge/submit_birthday | Submit Birthday
[**submit_otp**](Charge.md#submit_otp) | **POST** /charge/submit_otp | Submit OTP
[**submit_phone**](Charge.md#submit_phone) | **POST** /charge/submit_phone | Submit Phone
[**submit_pin**](Charge.md#submit_pin) | **POST** /charge/submit_pin | Submit PIN


# **check**
> Response check(reference)

Check pending charge

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import paystack
from paystack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.paystack.co
# See configuration.py for a list of all supported configuration parameters.
configuration = paystack.Configuration(
    host = "https://api.paystack.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = paystack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with paystack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paystack.Charge(api_client)
    reference = 'reference_example' # str | 

    try:
        # Check pending charge
        api_response = api_instance.check(reference)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Charge->check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference** | **str**|  | 

### Return type

[**Response**](Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Unauthorized operation |  -  |
**404** | Entity not found |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> Response create(email=email, amount=amount, authorization_code=authorization_code, pin=pin, reference=reference, birthday=birthday, device_id=device_id, metadata=metadata, bank=bank, mobile_money=mobile_money, ussd=ussd, eft=eft)

Create Charge

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import paystack
from paystack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.paystack.co
# See configuration.py for a list of all supported configuration parameters.
configuration = paystack.Configuration(
    host = "https://api.paystack.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = paystack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with paystack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paystack.Charge(api_client)
    email = 'email_example' # str | Customer's email address (optional)
amount = 'amount_example' # str | Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR (optional)
authorization_code = 'authorization_code_example' # str | An authorization code to charge. (optional)
pin = 'pin_example' # str | 4-digit PIN (send with a non-reusable authorization code) (optional)
reference = 'reference_example' # str | Unique transaction reference. Only -, .`, = and alphanumeric characters allowed. (optional)
birthday = '2013-10-20T19:20:30+01:00' # datetime | The customer's birthday in the format YYYY-MM-DD e.g 2017-05-16 (optional)
device_id = 'device_id_example' # str | This is the unique identifier of the device a user uses in making payment.  Only -, .`, = and alphanumeric characters are allowed. (optional)
metadata = 'metadata_example' # str | Stringified JSON object of custom data (optional)
bank = paystack.Bank() # Bank |  (optional)
mobile_money = paystack.MobileMoney() # MobileMoney |  (optional)
ussd = paystack.USSD() # USSD |  (optional)
eft = paystack.EFT() # EFT |  (optional)

    try:
        # Create Charge
        api_response = api_instance.create(email=email, amount=amount, authorization_code=authorization_code, pin=pin, reference=reference, birthday=birthday, device_id=device_id, metadata=metadata, bank=bank, mobile_money=mobile_money, ussd=ussd, eft=eft)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Charge->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Customer&#39;s email address | [optional] 
 **amount** | **str**| Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR | [optional] 
 **authorization_code** | **str**| An authorization code to charge. | [optional] 
 **pin** | **str**| 4-digit PIN (send with a non-reusable authorization code) | [optional] 
 **reference** | **str**| Unique transaction reference. Only -, .&#x60;, &#x3D; and alphanumeric characters allowed. | [optional] 
 **birthday** | **datetime**| The customer&#39;s birthday in the format YYYY-MM-DD e.g 2017-05-16 | [optional] 
 **device_id** | **str**| This is the unique identifier of the device a user uses in making payment.  Only -, .&#x60;, &#x3D; and alphanumeric characters are allowed. | [optional] 
 **metadata** | **str**| Stringified JSON object of custom data | [optional] 
 **bank** | [**Bank**](Bank.md)|  | [optional] 
 **mobile_money** | [**MobileMoney**](MobileMoney.md)|  | [optional] 
 **ussd** | [**USSD**](USSD.md)|  | [optional] 
 **eft** | [**EFT**](EFT.md)|  | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created |  -  |
**401** | Unauthorized operation |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_address**
> Response submit_address(address, city, state, zipcode, reference)

Submit Address

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import paystack
from paystack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.paystack.co
# See configuration.py for a list of all supported configuration parameters.
configuration = paystack.Configuration(
    host = "https://api.paystack.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = paystack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with paystack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paystack.Charge(api_client)
    address = 'address_example' # str | Customer's address
city = 'city_example' # str | Customer's city
state = 'state_example' # str | Customer's state
zipcode = 'zipcode_example' # str | Customer's zipcode
reference = 'reference_example' # str | The reference of the ongoing transaction

    try:
        # Submit Address
        api_response = api_instance.submit_address(address, city, state, zipcode, reference)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Charge->submit_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Customer&#39;s address | 
 **city** | **str**| Customer&#39;s city | 
 **state** | **str**| Customer&#39;s state | 
 **zipcode** | **str**| Customer&#39;s zipcode | 
 **reference** | **str**| The reference of the ongoing transaction | 

### Return type

[**Response**](Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created |  -  |
**401** | Unauthorized operation |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_birthday**
> Response submit_birthday(birthday, reference)

Submit Birthday

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import paystack
from paystack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.paystack.co
# See configuration.py for a list of all supported configuration parameters.
configuration = paystack.Configuration(
    host = "https://api.paystack.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = paystack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with paystack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paystack.Charge(api_client)
    birthday = 'birthday_example' # str | Customer's birthday in the format YYYY-MM-DD e.g 2016-09-21
reference = 'reference_example' # str | The reference of the ongoing transaction

    try:
        # Submit Birthday
        api_response = api_instance.submit_birthday(birthday, reference)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Charge->submit_birthday: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **birthday** | **str**| Customer&#39;s birthday in the format YYYY-MM-DD e.g 2016-09-21 | 
 **reference** | **str**| The reference of the ongoing transaction | 

### Return type

[**Response**](Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created |  -  |
**401** | Unauthorized operation |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_otp**
> Response submit_otp(otp, reference)

Submit OTP

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import paystack
from paystack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.paystack.co
# See configuration.py for a list of all supported configuration parameters.
configuration = paystack.Configuration(
    host = "https://api.paystack.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = paystack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with paystack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paystack.Charge(api_client)
    otp = 'otp_example' # str | Customer's OTP
reference = 'reference_example' # str | The reference of the ongoing transaction

    try:
        # Submit OTP
        api_response = api_instance.submit_otp(otp, reference)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Charge->submit_otp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otp** | **str**| Customer&#39;s OTP | 
 **reference** | **str**| The reference of the ongoing transaction | 

### Return type

[**Response**](Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created |  -  |
**401** | Unauthorized operation |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_phone**
> Response submit_phone(phone, reference)

Submit Phone

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import paystack
from paystack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.paystack.co
# See configuration.py for a list of all supported configuration parameters.
configuration = paystack.Configuration(
    host = "https://api.paystack.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = paystack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with paystack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paystack.Charge(api_client)
    phone = 'phone_example' # str | Customer's mobile number
reference = 'reference_example' # str | The reference of the ongoing transaction

    try:
        # Submit Phone
        api_response = api_instance.submit_phone(phone, reference)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Charge->submit_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**| Customer&#39;s mobile number | 
 **reference** | **str**| The reference of the ongoing transaction | 

### Return type

[**Response**](Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created |  -  |
**401** | Unauthorized operation |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_pin**
> Response submit_pin(pin, reference)

Submit PIN

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import paystack
from paystack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.paystack.co
# See configuration.py for a list of all supported configuration parameters.
configuration = paystack.Configuration(
    host = "https://api.paystack.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = paystack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with paystack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paystack.Charge(api_client)
    pin = 'pin_example' # str | Customer's PIN
reference = 'reference_example' # str | Transaction reference that requires the PIN

    try:
        # Submit PIN
        api_response = api_instance.submit_pin(pin, reference)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Charge->submit_pin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pin** | **str**| Customer&#39;s PIN | 
 **reference** | **str**| Transaction reference that requires the PIN | 

### Return type

[**Response**](Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created |  -  |
**401** | Unauthorized operation |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

