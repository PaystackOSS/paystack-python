# paystack.Plan

All URIs are relative to *https://api.paystack.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](Plan.md#create) | **POST** /plan | Create Plan
[**fetch**](Plan.md#fetch) | **GET** /plan/{code} | Fetch Plan
[**list**](Plan.md#list) | **GET** /plan | List Plans
[**update**](Plan.md#update) | **PUT** /plan/{code} | Update Plan


# **create**
> Response create(name, amount, interval, description=description, send_invoices=send_invoices, send_sms=send_sms, currency=currency, invoice_limit=invoice_limit)

Create Plan

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
    api_instance = paystack.Plan(api_client)
    name = 'name_example' # str | Name of plan
amount = 56 # int | Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
interval = 'interval_example' # str | Interval in words. Valid intervals are daily, weekly, monthly,biannually, annually
description = True # bool | A description for this plan (optional)
send_invoices = True # bool | Set to false if you don't want invoices to be sent to your customers (optional)
send_sms = True # bool | Set to false if you don't want text messages to be sent to your customers (optional)
currency = 'currency_example' # str | Currency in which amount is set. Allowed values are NGN, GHS, ZAR or USD (optional)
invoice_limit = 56 # int | Number of invoices to raise during subscription to this plan.  Can be overridden by specifying an invoice_limit while subscribing. (optional)

    try:
        # Create Plan
        api_response = api_instance.create(name, amount, interval, description=description, send_invoices=send_invoices, send_sms=send_sms, currency=currency, invoice_limit=invoice_limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Plan->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of plan | 
 **amount** | **int**| Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR | 
 **interval** | **str**| Interval in words. Valid intervals are daily, weekly, monthly,biannually, annually | 
 **description** | **bool**| A description for this plan | [optional] 
 **send_invoices** | **bool**| Set to false if you don&#39;t want invoices to be sent to your customers | [optional] 
 **send_sms** | **bool**| Set to false if you don&#39;t want text messages to be sent to your customers | [optional] 
 **currency** | **str**| Currency in which amount is set. Allowed values are NGN, GHS, ZAR or USD | [optional] 
 **invoice_limit** | **int**| Number of invoices to raise during subscription to this plan.  Can be overridden by specifying an invoice_limit while subscribing. | [optional] 

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

Fetch Plan

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
    api_instance = paystack.Plan(api_client)
    code = 'code_example' # str | 

    try:
        # Fetch Plan
        api_response = api_instance.fetch(code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Plan->fetch: %s\n" % e)
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
> Response list(per_page=per_page, page=page, interval=interval, amount=amount, _from=_from, to=to)

List Plans

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
    api_instance = paystack.Plan(api_client)
    per_page = 56 # int | Number of records to fetch per page (optional)
page = 56 # int | The section to retrieve (optional)
interval = 'interval_example' # str | Specify interval of the plan (optional)
amount = 56 # int | The amount on the plans to retrieve (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | The start date (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | The end date (optional)

    try:
        # List Plans
        api_response = api_instance.list(per_page=per_page, page=page, interval=interval, amount=amount, _from=_from, to=to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Plan->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Number of records to fetch per page | [optional] 
 **page** | **int**| The section to retrieve | [optional] 
 **interval** | **str**| Specify interval of the plan | [optional] 
 **amount** | **int**| The amount on the plans to retrieve | [optional] 
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

# **update**
> Response update(code, name=name, amount=amount, interval=interval, description=description, send_invoices=send_invoices, send_sms=send_sms, currency=currency, invoice_limit=invoice_limit)

Update Plan

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
    api_instance = paystack.Plan(api_client)
    code = 'code_example' # str | 
name = 'name_example' # str | Name of plan (optional)
amount = 56 # int | Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR (optional)
interval = 'interval_example' # str | Interval in words. Valid intervals are daily, weekly, monthly,biannually, annually (optional)
description = True # bool | A description for this plan (optional)
send_invoices = True # bool | Set to false if you don't want invoices to be sent to your customers (optional)
send_sms = True # bool | Set to false if you don't want text messages to be sent to your customers (optional)
currency = 'currency_example' # str | Currency in which amount is set. Allowed values are NGN, GHS, ZAR or USD (optional)
invoice_limit = 56 # int | Number of invoices to raise during subscription to this plan.  Can be overridden by specifying an invoice_limit while subscribing. (optional)

    try:
        # Update Plan
        api_response = api_instance.update(code, name=name, amount=amount, interval=interval, description=description, send_invoices=send_invoices, send_sms=send_sms, currency=currency, invoice_limit=invoice_limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Plan->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **name** | **str**| Name of plan | [optional] 
 **amount** | **int**| Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR | [optional] 
 **interval** | **str**| Interval in words. Valid intervals are daily, weekly, monthly,biannually, annually | [optional] 
 **description** | **bool**| A description for this plan | [optional] 
 **send_invoices** | **bool**| Set to false if you don&#39;t want invoices to be sent to your customers | [optional] 
 **send_sms** | **bool**| Set to false if you don&#39;t want text messages to be sent to your customers | [optional] 
 **currency** | **str**| Currency in which amount is set. Allowed values are NGN, GHS, ZAR or USD | [optional] 
 **invoice_limit** | **int**| Number of invoices to raise during subscription to this plan.  Can be overridden by specifying an invoice_limit while subscribing. | [optional] 

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

