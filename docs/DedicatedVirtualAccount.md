# paystack.DedicatedVirtualAccount

All URIs are relative to *https://api.paystack.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_split**](DedicatedVirtualAccount.md#add_split) | **POST** /dedicated_account/split | Split Dedicated Account Transaction
[**available_providers**](DedicatedVirtualAccount.md#available_providers) | **GET** /dedicated_account/available_providers | Fetch Bank Providers
[**create**](DedicatedVirtualAccount.md#create) | **POST** /dedicated_account | Create Dedicated Account
[**deactivate**](DedicatedVirtualAccount.md#deactivate) | **DELETE** /dedicated_account/{account_id} | Deactivate Dedicated Account
[**fetch**](DedicatedVirtualAccount.md#fetch) | **GET** /dedicated_account/{account_id} | Fetch Dedicated Account
[**list**](DedicatedVirtualAccount.md#list) | **GET** /dedicated_account | List Dedicated Accounts
[**remove_split**](DedicatedVirtualAccount.md#remove_split) | **DELETE** /dedicated_account/split | Remove Split from Dedicated Account


# **add_split**
> Response add_split(account_number, subaccount=subaccount, split_code=split_code)

Split Dedicated Account Transaction

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
    api_instance = paystack.DedicatedVirtualAccount(api_client)
    account_number = 'account_number_example' # str | Valid Dedicated virtual account
subaccount = 'subaccount_example' # str | Subaccount code of the account you want to split the transaction with (optional)
split_code = 'split_code_example' # str | Split code consisting of the lists of accounts you want to split the transaction with (optional)

    try:
        # Split Dedicated Account Transaction
        api_response = api_instance.add_split(account_number, subaccount=subaccount, split_code=split_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DedicatedVirtualAccount->add_split: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| Valid Dedicated virtual account | 
 **subaccount** | **str**| Subaccount code of the account you want to split the transaction with | [optional] 
 **split_code** | **str**| Split code consisting of the lists of accounts you want to split the transaction with | [optional] 

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

# **available_providers**
> Response available_providers()

Fetch Bank Providers

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
    api_instance = paystack.DedicatedVirtualAccount(api_client)
    
    try:
        # Fetch Bank Providers
        api_response = api_instance.available_providers()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DedicatedVirtualAccount->available_providers: %s\n" % e)
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

# **create**
> Response create(customer, preferred_bank=preferred_bank, subaccount=subaccount, split_code=split_code)

Create Dedicated Account

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
    api_instance = paystack.DedicatedVirtualAccount(api_client)
    customer = 'customer_example' # str | Customer ID or code
preferred_bank = 'preferred_bank_example' # str | The bank slug for preferred bank. To get a list of available banks, use the List Providers endpoint (optional)
subaccount = 'subaccount_example' # str | Subaccount code of the account you want to split the transaction with (optional)
split_code = 'split_code_example' # str | Split code consisting of the lists of accounts you want to split the transaction with (optional)

    try:
        # Create Dedicated Account
        api_response = api_instance.create(customer, preferred_bank=preferred_bank, subaccount=subaccount, split_code=split_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DedicatedVirtualAccount->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer** | **str**| Customer ID or code | 
 **preferred_bank** | **str**| The bank slug for preferred bank. To get a list of available banks, use the List Providers endpoint | [optional] 
 **subaccount** | **str**| Subaccount code of the account you want to split the transaction with | [optional] 
 **split_code** | **str**| Split code consisting of the lists of accounts you want to split the transaction with | [optional] 

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

# **deactivate**
> Response deactivate(account_id)

Deactivate Dedicated Account

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
    api_instance = paystack.DedicatedVirtualAccount(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # Deactivate Dedicated Account
        api_response = api_instance.deactivate(account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DedicatedVirtualAccount->deactivate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

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

# **fetch**
> Response fetch(account_id)

Fetch Dedicated Account

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
    api_instance = paystack.DedicatedVirtualAccount(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # Fetch Dedicated Account
        api_response = api_instance.fetch(account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DedicatedVirtualAccount->fetch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

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

# **list**
> Response list(account_number=account_number, customer=customer, active=active, currency=currency, provider_slug=provider_slug, bank_id=bank_id, per_page=per_page, page=page)

List Dedicated Accounts

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
    api_instance = paystack.DedicatedVirtualAccount(api_client)
    account_number = 'account_number_example' # str |  (optional)
customer = 'customer_example' # str |  (optional)
active = True # bool |  (optional)
currency = 'currency_example' # str |  (optional)
provider_slug = 'provider_slug_example' # str |  (optional)
bank_id = 'bank_id_example' # str |  (optional)
per_page = 'per_page_example' # str |  (optional)
page = 'page_example' # str |  (optional)

    try:
        # List Dedicated Accounts
        api_response = api_instance.list(account_number=account_number, customer=customer, active=active, currency=currency, provider_slug=provider_slug, bank_id=bank_id, per_page=per_page, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DedicatedVirtualAccount->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**|  | [optional] 
 **customer** | **str**|  | [optional] 
 **active** | **bool**|  | [optional] 
 **currency** | **str**|  | [optional] 
 **provider_slug** | **str**|  | [optional] 
 **bank_id** | **str**|  | [optional] 
 **per_page** | **str**|  | [optional] 
 **page** | **str**|  | [optional] 

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

# **remove_split**
> Response remove_split(account_number, subaccount=subaccount, split_code=split_code)

Remove Split from Dedicated Account

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
    api_instance = paystack.DedicatedVirtualAccount(api_client)
    account_number = 'account_number_example' # str | Valid Dedicated virtual account
subaccount = 'subaccount_example' # str | Subaccount code of the account you want to split the transaction with (optional)
split_code = 'split_code_example' # str | Split code consisting of the lists of accounts you want to split the transaction with (optional)

    try:
        # Remove Split from Dedicated Account
        api_response = api_instance.remove_split(account_number, subaccount=subaccount, split_code=split_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DedicatedVirtualAccount->remove_split: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| Valid Dedicated virtual account | 
 **subaccount** | **str**| Subaccount code of the account you want to split the transaction with | [optional] 
 **split_code** | **str**| Split code consisting of the lists of accounts you want to split the transaction with | [optional] 

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
**200** | Successful operation |  -  |
**401** | Unauthorized operation |  -  |
**404** | Entity not found |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

