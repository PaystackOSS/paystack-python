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
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

name = 'name_example' # str | Name of plan
amount = 56 # int | Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
interval = 'interval_example' # str | Interval in words. Valid intervals are daily, weekly, monthly,biannually, annually

# Create Plan

response = paystack.Plan.create(
    name,
    amount,
    interval,
)

pprint(response)
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
**200** | Request successful |  -  |
**401** | Unauthorized operation |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch**
> Response fetch(code)

Fetch Plan

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

code = 'code_example' # str | 

# Fetch Plan

response = paystack.Plan.fetch(
    code,
)

pprint(response)
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
**200** | Request successful |  -  |
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
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'


# List Plans

response = paystack.Plan.list(
)

pprint(response)
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
**200** | Request successful |  -  |
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
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

code = 'code_example' # str | 

# Update Plan

response = paystack.Plan.update(
    code,
)

pprint(response)
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
**200** | Request successful |  -  |
**401** | Unauthorized operation |  -  |
**404** | Entity not found |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

