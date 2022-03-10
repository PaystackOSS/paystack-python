# paystack.PaymentRequest

All URIs are relative to *https://api.paystack.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive**](PaymentRequest.md#archive) | **POST** /paymentrequest/archive/{id} | Archive Payment Request
[**create**](PaymentRequest.md#create) | **POST** /paymentrequest | Create Payment Request
[**fetch**](PaymentRequest.md#fetch) | **GET** /paymentrequest/{id} | Fetch Payment Request
[**finalize**](PaymentRequest.md#finalize) | **POST** /paymentrequest/finalize/{id} | Finalize Payment Request
[**list**](PaymentRequest.md#list) | **GET** /paymentrequest | List Payment Request
[**notify**](PaymentRequest.md#notify) | **POST** /paymentrequest/notify/{id} | Send Notification
[**totals**](PaymentRequest.md#totals) | **GET** /paymentrequest/totals | Payment Request Total
[**update**](PaymentRequest.md#update) | **PUT** /paymentrequest/{id} | Update Payment Request
[**verify**](PaymentRequest.md#verify) | **GET** /paymentrequest/verify/{id} | Verify Payment Request


# **archive**
> Response archive(id)

Archive Payment Request

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
    api_instance = paystack.PaymentRequest(api_client)
    id = 'id_example' # str | 

    try:
        # Archive Payment Request
        api_response = api_instance.archive(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentRequest->archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**201** | Resource created |  -  |
**401** | Unauthorized operation |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> Response create(customer, amount=amount, currency=currency, due_date=due_date, description=description, line_items=line_items, tax=tax, send_notification=send_notification, draft=draft, has_invoice=has_invoice, invoice_number=invoice_number, split_code=split_code)

Create Payment Request

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
    api_instance = paystack.PaymentRequest(api_client)
    customer = 'customer_example' # str | Customer id or code
amount = 56 # int | Payment request amount. Only useful if line items and tax values are ignored.  The endpoint will throw a friendly warning if neither is available. (optional)
currency = 'currency_example' # str | Specify the currency of the invoice. Allowed values are NGN, GHS, ZAR and USD. Defaults to NGN (optional)
due_date = '2013-10-20T19:20:30+01:00' # datetime | ISO 8601 representation of request due date (optional)
description = 'description_example' # str | A short description of the payment request (optional)
line_items = None # list[object] | Array of line items (optional)
tax = None # list[object] | Array of taxes (optional)
send_notification = None # list[object] | Indicates whether Paystack sends an email notification to customer. Defaults to true (optional)
draft = None # list[object] | Indicate if request should be saved as draft. Defaults to false and overrides send_notification (optional)
has_invoice = None # list[object] | Set to true to create a draft invoice (adds an auto incrementing invoice number if none is provided)  even if there are no line_items or tax passed (optional)
invoice_number = 56 # int | Numeric value of invoice. Invoice will start from 1 and auto increment from there. This field is to help  override whatever value Paystack decides. Auto increment for subsequent invoices continue from this point. (optional)
split_code = 'split_code_example' # str | The split code of the transaction split. (optional)

    try:
        # Create Payment Request
        api_response = api_instance.create(customer, amount=amount, currency=currency, due_date=due_date, description=description, line_items=line_items, tax=tax, send_notification=send_notification, draft=draft, has_invoice=has_invoice, invoice_number=invoice_number, split_code=split_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentRequest->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer** | **str**| Customer id or code | 
 **amount** | **int**| Payment request amount. Only useful if line items and tax values are ignored.  The endpoint will throw a friendly warning if neither is available. | [optional] 
 **currency** | **str**| Specify the currency of the invoice. Allowed values are NGN, GHS, ZAR and USD. Defaults to NGN | [optional] 
 **due_date** | **datetime**| ISO 8601 representation of request due date | [optional] 
 **description** | **str**| A short description of the payment request | [optional] 
 **line_items** | [**list[object]**](object.md)| Array of line items | [optional] 
 **tax** | [**list[object]**](object.md)| Array of taxes | [optional] 
 **send_notification** | [**list[object]**](object.md)| Indicates whether Paystack sends an email notification to customer. Defaults to true | [optional] 
 **draft** | [**list[object]**](object.md)| Indicate if request should be saved as draft. Defaults to false and overrides send_notification | [optional] 
 **has_invoice** | [**list[object]**](object.md)| Set to true to create a draft invoice (adds an auto incrementing invoice number if none is provided)  even if there are no line_items or tax passed | [optional] 
 **invoice_number** | **int**| Numeric value of invoice. Invoice will start from 1 and auto increment from there. This field is to help  override whatever value Paystack decides. Auto increment for subsequent invoices continue from this point. | [optional] 
 **split_code** | **str**| The split code of the transaction split. | [optional] 

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
> Response fetch(id)

Fetch Payment Request

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
    api_instance = paystack.PaymentRequest(api_client)
    id = 'id_example' # str | 

    try:
        # Fetch Payment Request
        api_response = api_instance.fetch(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentRequest->fetch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **finalize**
> Response finalize(id)

Finalize Payment Request

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
    api_instance = paystack.PaymentRequest(api_client)
    id = 'id_example' # str | 

    try:
        # Finalize Payment Request
        api_response = api_instance.finalize(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentRequest->finalize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**201** | Resource created |  -  |
**401** | Unauthorized operation |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> Response list(per_page=per_page, page=page, customer=customer, status=status, currency=currency, _from=_from, to=to)

List Payment Request

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
    api_instance = paystack.PaymentRequest(api_client)
    per_page = 56 # int | Number of records to fetch per page (optional)
page = 56 # int | The section to retrieve (optional)
customer = 'customer_example' # str | Customer ID (optional)
status = 'status_example' # str | Invoice status to filter (optional)
currency = 'currency_example' # str | If your integration supports more than one currency, choose the one to filter (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | The start date (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | The end date (optional)

    try:
        # List Payment Request
        api_response = api_instance.list(per_page=per_page, page=page, customer=customer, status=status, currency=currency, _from=_from, to=to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentRequest->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Number of records to fetch per page | [optional] 
 **page** | **int**| The section to retrieve | [optional] 
 **customer** | **str**| Customer ID | [optional] 
 **status** | **str**| Invoice status to filter | [optional] 
 **currency** | **str**| If your integration supports more than one currency, choose the one to filter | [optional] 
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

# **notify**
> Response notify(id)

Send Notification

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
    api_instance = paystack.PaymentRequest(api_client)
    id = 'id_example' # str | 

    try:
        # Send Notification
        api_response = api_instance.notify(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentRequest->notify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**201** | Resource created |  -  |
**401** | Unauthorized operation |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **totals**
> Response totals()

Payment Request Total

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
    api_instance = paystack.PaymentRequest(api_client)
    
    try:
        # Payment Request Total
        api_response = api_instance.totals()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentRequest->totals: %s\n" % e)
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

# **update**
> Response update(id, customer=customer, amount=amount, currency=currency, due_date=due_date, description=description, line_items=line_items, tax=tax, send_notification=send_notification, draft=draft, has_invoice=has_invoice, invoice_number=invoice_number, split_code=split_code)

Update Payment Request

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
    api_instance = paystack.PaymentRequest(api_client)
    id = 'id_example' # str | 
customer = 'customer_example' # str | Customer id or code (optional)
amount = 56 # int | Payment request amount. Only useful if line items and tax values are ignored.  The endpoint will throw a friendly warning if neither is available. (optional)
currency = 'currency_example' # str | Specify the currency of the invoice. Allowed values are NGN, GHS, ZAR and USD. Defaults to NGN (optional)
due_date = '2013-10-20T19:20:30+01:00' # datetime | ISO 8601 representation of request due date (optional)
description = 'description_example' # str | A short description of the payment request (optional)
line_items = None # list[object] | Array of line items (optional)
tax = None # list[object] | Array of taxes (optional)
send_notification = None # list[object] | Indicates whether Paystack sends an email notification to customer. Defaults to true (optional)
draft = None # list[object] | Indicate if request should be saved as draft. Defaults to false and overrides send_notification (optional)
has_invoice = None # list[object] | Set to true to create a draft invoice (adds an auto incrementing invoice number if none is provided)  even if there are no line_items or tax passed (optional)
invoice_number = 56 # int | Numeric value of invoice. Invoice will start from 1 and auto increment from there. This field is to help  override whatever value Paystack decides. Auto increment for subsequent invoices continue from this point. (optional)
split_code = 'split_code_example' # str | The split code of the transaction split. (optional)

    try:
        # Update Payment Request
        api_response = api_instance.update(id, customer=customer, amount=amount, currency=currency, due_date=due_date, description=description, line_items=line_items, tax=tax, send_notification=send_notification, draft=draft, has_invoice=has_invoice, invoice_number=invoice_number, split_code=split_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentRequest->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **customer** | **str**| Customer id or code | [optional] 
 **amount** | **int**| Payment request amount. Only useful if line items and tax values are ignored.  The endpoint will throw a friendly warning if neither is available. | [optional] 
 **currency** | **str**| Specify the currency of the invoice. Allowed values are NGN, GHS, ZAR and USD. Defaults to NGN | [optional] 
 **due_date** | **datetime**| ISO 8601 representation of request due date | [optional] 
 **description** | **str**| A short description of the payment request | [optional] 
 **line_items** | [**list[object]**](object.md)| Array of line items | [optional] 
 **tax** | [**list[object]**](object.md)| Array of taxes | [optional] 
 **send_notification** | [**list[object]**](object.md)| Indicates whether Paystack sends an email notification to customer. Defaults to true | [optional] 
 **draft** | [**list[object]**](object.md)| Indicate if request should be saved as draft. Defaults to false and overrides send_notification | [optional] 
 **has_invoice** | [**list[object]**](object.md)| Set to true to create a draft invoice (adds an auto incrementing invoice number if none is provided)  even if there are no line_items or tax passed | [optional] 
 **invoice_number** | **int**| Numeric value of invoice. Invoice will start from 1 and auto increment from there. This field is to help  override whatever value Paystack decides. Auto increment for subsequent invoices continue from this point. | [optional] 
 **split_code** | **str**| The split code of the transaction split. | [optional] 

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

# **verify**
> Response verify(id)

Verify Payment Request

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
    api_instance = paystack.PaymentRequest(api_client)
    id = 'id_example' # str | 

    try:
        # Verify Payment Request
        api_response = api_instance.verify(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentRequest->verify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

