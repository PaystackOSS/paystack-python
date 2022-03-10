# paystack.Balance

All URIs are relative to *https://api.paystack.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch**](Balance.md#fetch) | **GET** /balance | Fetch Balance
[**ledger**](Balance.md#ledger) | **GET** /balance/ledger | Balance Ledger


# **fetch**
> Response fetch()

Fetch Balance

You can only transfer from what you have

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
    api_instance = paystack.Balance(api_client)
    
    try:
        # Fetch Balance
        api_response = api_instance.fetch()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Balance->fetch: %s\n" % e)
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

# **ledger**
> Response ledger(per_page=per_page, page=page, _from=_from, to=to)

Balance Ledger

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
    api_instance = paystack.Balance(api_client)
    per_page = 56 # int | Number of records to fetch per page (optional)
page = 56 # int | The section to retrieve (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | The start date (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | The end date (optional)

    try:
        # Balance Ledger
        api_response = api_instance.ledger(per_page=per_page, page=page, _from=_from, to=to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Balance->ledger: %s\n" % e)
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

