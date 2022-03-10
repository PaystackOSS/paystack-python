# paystack.TransferRecipient

All URIs are relative to *https://api.paystack.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk**](TransferRecipient.md#bulk) | **POST** /transferrecipient/bulk | Bulk Create Transfer Recipient
[**create**](TransferRecipient.md#create) | **POST** /transferrecipient | Create Transfer Recipient
[**fetch**](TransferRecipient.md#fetch) | **GET** /transferrecipient/{code} | Fetch Transfer recipient
[**list**](TransferRecipient.md#list) | **GET** /transferrecipient | List Transfer Recipients
[**transferrecipient_code_delete**](TransferRecipient.md#transferrecipient_code_delete) | **DELETE** /transferrecipient/{code} | Delete Transfer Recipient
[**transferrecipient_code_put**](TransferRecipient.md#transferrecipient_code_put) | **PUT** /transferrecipient/{code} | Update Transfer recipient


# **bulk**
> Response bulk(batch)

Bulk Create Transfer Recipient

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
    api_instance = paystack.TransferRecipient(api_client)
    batch = paystack.TransferRecipientCreate() # list[TransferRecipientCreate] | A list of transfer recipient object. Each object should contain type, name, and bank_code.  Any Create Transfer Recipient param can also be passed.

    try:
        # Bulk Create Transfer Recipient
        api_response = api_instance.bulk(batch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransferRecipient->bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch** | [**list[TransferRecipientCreate]**](TransferRecipientCreate.md)| A list of transfer recipient object. Each object should contain type, name, and bank_code.  Any Create Transfer Recipient param can also be passed. | 

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

# **create**
> Response create(type, name, account_number, bank_code, description=description, currency=currency, authorization_code=authorization_code, metadata=metadata)

Create Transfer Recipient

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
    api_instance = paystack.TransferRecipient(api_client)
    type = 'type_example' # str | Recipient Type (Only nuban at this time)
name = 'name_example' # str | Recipient's name
account_number = 'account_number_example' # str | Recipient's bank account number
bank_code = 'bank_code_example' # str | Recipient's bank code. You can get the list of Bank Codes by calling the List Banks endpoint
description = 'description_example' # str | A description for this recipient (optional)
currency = 'currency_example' # str | Currency for the account receiving the transfer (optional)
authorization_code = 'authorization_code_example' # str | An authorization code from a previous transaction (optional)
metadata = 'metadata_example' # str | Stringified JSON object of custom data (optional)

    try:
        # Create Transfer Recipient
        api_response = api_instance.create(type, name, account_number, bank_code, description=description, currency=currency, authorization_code=authorization_code, metadata=metadata)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransferRecipient->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Recipient Type (Only nuban at this time) | 
 **name** | **str**| Recipient&#39;s name | 
 **account_number** | **str**| Recipient&#39;s bank account number | 
 **bank_code** | **str**| Recipient&#39;s bank code. You can get the list of Bank Codes by calling the List Banks endpoint | 
 **description** | **str**| A description for this recipient | [optional] 
 **currency** | **str**| Currency for the account receiving the transfer | [optional] 
 **authorization_code** | **str**| An authorization code from a previous transaction | [optional] 
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

# **fetch**
> Response fetch(code)

Fetch Transfer recipient

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
    api_instance = paystack.TransferRecipient(api_client)
    code = 'code_example' # str | Transfer recipient code

    try:
        # Fetch Transfer recipient
        api_response = api_instance.fetch(code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransferRecipient->fetch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Transfer recipient code | 

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
> Response list(per_page=per_page, page=page, _from=_from, to=to)

List Transfer Recipients

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
    api_instance = paystack.TransferRecipient(api_client)
    per_page = 56 # int | Number of records to fetch per page (optional)
page = 56 # int | The section to retrieve (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | The start date (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | The end date (optional)

    try:
        # List Transfer Recipients
        api_response = api_instance.list(per_page=per_page, page=page, _from=_from, to=to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransferRecipient->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Number of records to fetch per page | [optional] 
 **page** | **int**| The section to retrieve | [optional] 
 **_from** | **datetime**| The start date | [optional] 
 **to** | **datetime**| The end date | [optional] 

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

# **transferrecipient_code_delete**
> Response transferrecipient_code_delete(code)

Delete Transfer Recipient

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
    api_instance = paystack.TransferRecipient(api_client)
    code = 'code_example' # str | Transfer recipient code

    try:
        # Delete Transfer Recipient
        api_response = api_instance.transferrecipient_code_delete(code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransferRecipient->transferrecipient_code_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Transfer recipient code | 

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

# **transferrecipient_code_put**
> Response transferrecipient_code_put(code, name=name, email=email)

Update Transfer recipient

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
    api_instance = paystack.TransferRecipient(api_client)
    code = 'code_example' # str | Transfer recipient code
name = 'name_example' # str | Recipient's name (optional)
email = 'email_example' # str | Recipient's email address (optional)

    try:
        # Update Transfer recipient
        api_response = api_instance.transferrecipient_code_put(code, name=name, email=email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransferRecipient->transferrecipient_code_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Transfer recipient code | 
 **name** | **str**| Recipient&#39;s name | [optional] 
 **email** | **str**| Recipient&#39;s email address | [optional] 

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

