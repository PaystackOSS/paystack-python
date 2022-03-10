# paystack.Verification

All URIs are relative to *https://api.paystack.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**avs**](Verification.md#avs) | **GET** /address_verification/states | List States (AVS)
[**bvn_match**](Verification.md#bvn_match) | **POST** /bvn/match | Match Service
[**fetch_banks**](Verification.md#fetch_banks) | **GET** /bank | Fetch Banks
[**list_countries**](Verification.md#list_countries) | **GET** /country | List Countries
[**resolve_account_number**](Verification.md#resolve_account_number) | **GET** /bank/resolve | Resolve Account Number
[**resolve_bvn**](Verification.md#resolve_bvn) | **GET** /bank/resolve_bvn/{bvn} | Resolve BVN
[**resolve_card_bin**](Verification.md#resolve_card_bin) | **GET** /decision/bin/{bin} | Resolve Card BIN


# **avs**
> Response avs(type=type, country=country, currency=currency)

List States (AVS)

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
    api_instance = paystack.Verification(api_client)
    type = 'type_example' # str |  (optional)
country = 'country_example' # str |  (optional)
currency = 'currency_example' # str |  (optional)

    try:
        # List States (AVS)
        api_response = api_instance.avs(type=type, country=country, currency=currency)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Verification->avs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 
 **country** | **str**|  | [optional] 
 **currency** | **str**|  | [optional] 

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

# **bvn_match**
> Response bvn_match(account_number, bank_code, bvn, first_name=first_name, middle_name=middle_name, last_name=last_name)

Match Service

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
    api_instance = paystack.Verification(api_client)
    account_number = 'account_number_example' # str | Bank Account Number
bank_code = 56 # int | You can get the list of banks codes by calling the List Bank endpoint
bvn = 'bvn_example' # str | 11 digits Bank Verification Number
first_name = 'first_name_example' # str | Customer's first name (optional)
middle_name = 'middle_name_example' # str | Customer's middle name (optional)
last_name = 'last_name_example' # str | Customer's last name (optional)

    try:
        # Match Service
        api_response = api_instance.bvn_match(account_number, bank_code, bvn, first_name=first_name, middle_name=middle_name, last_name=last_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Verification->bvn_match: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| Bank Account Number | 
 **bank_code** | **int**| You can get the list of banks codes by calling the List Bank endpoint | 
 **bvn** | **str**| 11 digits Bank Verification Number | 
 **first_name** | **str**| Customer&#39;s first name | [optional] 
 **middle_name** | **str**| Customer&#39;s middle name | [optional] 
 **last_name** | **str**| Customer&#39;s last name | [optional] 

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

# **fetch_banks**
> Response fetch_banks(country=country, pay_with_bank_transfer=pay_with_bank_transfer, use_cursor=use_cursor, per_page=per_page, next=next, previous=previous, gateway=gateway)

Fetch Banks

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
    api_instance = paystack.Verification(api_client)
    country = 'country_example' # str |  (optional)
pay_with_bank_transfer = True # bool |  (optional)
use_cursor = True # bool |  (optional)
per_page = 56 # int |  (optional)
next = 'next_example' # str |  (optional)
previous = 'previous_example' # str |  (optional)
gateway = 'gateway_example' # str |  (optional)

    try:
        # Fetch Banks
        api_response = api_instance.fetch_banks(country=country, pay_with_bank_transfer=pay_with_bank_transfer, use_cursor=use_cursor, per_page=per_page, next=next, previous=previous, gateway=gateway)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Verification->fetch_banks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**|  | [optional] 
 **pay_with_bank_transfer** | **bool**|  | [optional] 
 **use_cursor** | **bool**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **next** | **str**|  | [optional] 
 **previous** | **str**|  | [optional] 
 **gateway** | **str**|  | [optional] 

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

# **list_countries**
> Response list_countries()

List Countries

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
    api_instance = paystack.Verification(api_client)
    
    try:
        # List Countries
        api_response = api_instance.list_countries()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Verification->list_countries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **resolve_account_number**
> Response resolve_account_number(account_number=account_number, bank_code=bank_code)

Resolve Account Number

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
    api_instance = paystack.Verification(api_client)
    account_number = 0022728151 # int |  (optional)
bank_code = 063 # int |  (optional)

    try:
        # Resolve Account Number
        api_response = api_instance.resolve_account_number(account_number=account_number, bank_code=bank_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Verification->resolve_account_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **int**|  | [optional] 
 **bank_code** | **int**|  | [optional] 

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

# **resolve_bvn**
> Response resolve_bvn(bvn)

Resolve BVN

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
    api_instance = paystack.Verification(api_client)
    bvn = 'bvn_example' # str | 

    try:
        # Resolve BVN
        api_response = api_instance.resolve_bvn(bvn)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Verification->resolve_bvn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bvn** | **str**|  | 

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

# **resolve_card_bin**
> Response resolve_card_bin(bin)

Resolve Card BIN

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
    api_instance = paystack.Verification(api_client)
    bin = 'bin_example' # str | 

    try:
        # Resolve Card BIN
        api_response = api_instance.resolve_card_bin(bin)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Verification->resolve_card_bin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bin** | **str**|  | 

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

