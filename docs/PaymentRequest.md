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
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

id = 'id_example' # str | 

# Archive Payment Request

response = paystack.PaymentRequest.archive(
    id,
)

pprint(response)
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
**200** | Request successful |  -  |
**401** | Unauthorized operation |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> Response create(customer, amount=amount, currency=currency, due_date=due_date, description=description, line_items=line_items, tax=tax, send_notification=send_notification, draft=draft, has_invoice=has_invoice, invoice_number=invoice_number, split_code=split_code)

Create Payment Request

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

customer = 'customer_example' # str | Customer id or code

# Create Payment Request

response = paystack.PaymentRequest.create(
    customer,
)

pprint(response)
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
**200** | Request successful |  -  |
**401** | Unauthorized operation |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch**
> Response fetch(id)

Fetch Payment Request

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

id = 'id_example' # str | 

# Fetch Payment Request

response = paystack.PaymentRequest.fetch(
    id,
)

pprint(response)
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
**200** | Request successful |  -  |
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
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

id = 'id_example' # str | 

# Finalize Payment Request

response = paystack.PaymentRequest.finalize(
    id,
)

pprint(response)
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
**200** | Request successful |  -  |
**401** | Unauthorized operation |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> Response list(per_page=per_page, page=page, customer=customer, status=status, currency=currency, _from=_from, to=to)

List Payment Request

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'


# List Payment Request

response = paystack.PaymentRequest.list(
)

pprint(response)
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
**200** | Request successful |  -  |
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
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

id = 'id_example' # str | 

# Send Notification

response = paystack.PaymentRequest.notify(
    id,
)

pprint(response)
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
**200** | Request successful |  -  |
**401** | Unauthorized operation |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **totals**
> Response totals()

Payment Request Total

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'


# Payment Request Total

response = paystack.PaymentRequest.totals()


pprint(response)
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
**200** | Request successful |  -  |
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
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

id = 'id_example' # str | 

# Update Payment Request

response = paystack.PaymentRequest.update(
    id,
)

pprint(response)
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
**200** | Request successful |  -  |
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
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

id = 'id_example' # str | 

# Verify Payment Request

response = paystack.PaymentRequest.verify(
    id,
)

pprint(response)
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
**200** | Request successful |  -  |
**401** | Unauthorized operation |  -  |
**404** | Entity not found |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

