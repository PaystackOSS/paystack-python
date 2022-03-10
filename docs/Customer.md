# paystack.Customer

All URIs are relative to *https://api.paystack.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](Customer.md#create) | **POST** /customer | Create Customer
[**deactivate_authorization**](Customer.md#deactivate_authorization) | **POST** /customer/deactivate_authorization | Deactivate Authorization
[**fetch**](Customer.md#fetch) | **GET** /customer/{code} | Fetch Customer
[**list**](Customer.md#list) | **GET** /customer | List Customers
[**risk_action**](Customer.md#risk_action) | **POST** /customer/set_risk_action | White/blacklist Customer
[**update**](Customer.md#update) | **PUT** /customer/{code} | Update Customer
[**validatte**](Customer.md#validatte) | **POST** /customer/{code}/identification | Validate Customer


# **create**
> Response create(email, first_name=first_name, last_name=last_name, phone=phone, metadata=metadata)

Create Customer

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
    api_instance = paystack.Customer(api_client)
    email = 'email_example' # str | Customer's email address
first_name = 'first_name_example' # str | Customer's first name (optional)
last_name = 'last_name_example' # str | Customer's last name (optional)
phone = 'phone_example' # str | Customer's phone number (optional)
metadata = 'metadata_example' # str | Stringified JSON object of custom data (optional)

    try:
        # Create Customer
        api_response = api_instance.create(email, first_name=first_name, last_name=last_name, phone=phone, metadata=metadata)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Customer->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Customer&#39;s email address | 
 **first_name** | **str**| Customer&#39;s first name | [optional] 
 **last_name** | **str**| Customer&#39;s last name | [optional] 
 **phone** | **str**| Customer&#39;s phone number | [optional] 
 **metadata** | **str**| Stringified JSON object of custom data | [optional] 

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

# **deactivate_authorization**
> Response deactivate_authorization(authorization_code)

Deactivate Authorization

Deactivate a customer's card

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
    api_instance = paystack.Customer(api_client)
    authorization_code = 'authorization_code_example' # str | Authorization code to be deactivated

    try:
        # Deactivate Authorization
        api_response = api_instance.deactivate_authorization(authorization_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Customer->deactivate_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_code** | **str**| Authorization code to be deactivated | 

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

# **fetch**
> Response fetch(code)

Fetch Customer

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
    api_instance = paystack.Customer(api_client)
    code = 'code_example' # str | 

    try:
        # Fetch Customer
        api_response = api_instance.fetch(code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Customer->fetch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

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
> Response list(use_cursor=use_cursor, next=next, previous=previous, _from=_from, to=to, per_page=per_page, page=page)

List Customers

List customers on your integration

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
    api_instance = paystack.Customer(api_client)
    use_cursor = True # bool |  (optional)
next = 'next_example' # str |  (optional)
previous = 'previous_example' # str |  (optional)
_from = '_from_example' # str |  (optional)
to = 'to_example' # str |  (optional)
per_page = 'per_page_example' # str |  (optional)
page = 'page_example' # str |  (optional)

    try:
        # List Customers
        api_response = api_instance.list(use_cursor=use_cursor, next=next, previous=previous, _from=_from, to=to, per_page=per_page, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Customer->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use_cursor** | **bool**|  | [optional] 
 **next** | **str**|  | [optional] 
 **previous** | **str**|  | [optional] 
 **_from** | **str**|  | [optional] 
 **to** | **str**|  | [optional] 
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

# **risk_action**
> Response risk_action(customer, risk_action=risk_action)

White/blacklist Customer

Set customer's risk action by whitelisting or blacklisting the customer

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
    api_instance = paystack.Customer(api_client)
    customer = 'customer_example' # str | Customer's code, or email address
risk_action = 'risk_action_example' # str | One of the possible risk actions [ default, allow, deny ]. allow to whitelist.  deny to blacklist. Customers start with a default risk action.  (optional)

    try:
        # White/blacklist Customer
        api_response = api_instance.risk_action(customer, risk_action=risk_action)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Customer->risk_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer** | **str**| Customer&#39;s code, or email address | 
 **risk_action** | **str**| One of the possible risk actions [ default, allow, deny ]. allow to whitelist.  deny to blacklist. Customers start with a default risk action.  | [optional] 

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

# **update**
> Response update(code, first_name=first_name, last_name=last_name, phone=phone, metadata=metadata)

Update Customer

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
    api_instance = paystack.Customer(api_client)
    code = 'code_example' # str | 
first_name = 'first_name_example' # str | Customer's first name (optional)
last_name = 'last_name_example' # str | Customer's last name (optional)
phone = 'phone_example' # str | Customer's phone number (optional)
metadata = 'metadata_example' # str | Stringified JSON object of custom data (optional)

    try:
        # Update Customer
        api_response = api_instance.update(code, first_name=first_name, last_name=last_name, phone=phone, metadata=metadata)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Customer->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **first_name** | **str**| Customer&#39;s first name | [optional] 
 **last_name** | **str**| Customer&#39;s last name | [optional] 
 **phone** | **str**| Customer&#39;s phone number | [optional] 
 **metadata** | **str**| Stringified JSON object of custom data | [optional] 

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

# **validatte**
> Response validatte(code, first_name, last_name, type, country, bvn, bank_code, account_number, value=value)

Validate Customer

Validate a customer's identity

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
    api_instance = paystack.Customer(api_client)
    code = 'code_example' # str | 
first_name = 'first_name_example' # str | Customer's first name
last_name = 'last_name_example' # str | Customer's last name
type = 'type_example' # str | Predefined types of identification.
country = 'country_example' # str | Two-letter country code of identification issuer
bvn = 'bvn_example' # str | Customer's Bank Verification Number
bank_code = 'bank_code_example' # str | You can get the list of bank codes by calling the List Banks endpoint (https://api.paystack.co/bank).
account_number = 'account_number_example' # str | Customer's bank account number.
value = 'value_example' # str | Customer's identification number. Required if type is bvn (optional)

    try:
        # Validate Customer
        api_response = api_instance.validatte(code, first_name, last_name, type, country, bvn, bank_code, account_number, value=value)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Customer->validatte: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **first_name** | **str**| Customer&#39;s first name | 
 **last_name** | **str**| Customer&#39;s last name | 
 **type** | **str**| Predefined types of identification. | 
 **country** | **str**| Two-letter country code of identification issuer | 
 **bvn** | **str**| Customer&#39;s Bank Verification Number | 
 **bank_code** | **str**| You can get the list of bank codes by calling the List Banks endpoint (https://api.paystack.co/bank). | 
 **account_number** | **str**| Customer&#39;s bank account number. | 
 **value** | **str**| Customer&#39;s identification number. Required if type is bvn | [optional] 

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

