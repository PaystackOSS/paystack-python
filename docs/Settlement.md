# paystack.Settlement

All URIs are relative to *https://api.paystack.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch**](Settlement.md#fetch) | **GET** /settlement | Fetch Settlements
[**transaction**](Settlement.md#transaction) | **GET** /settlement/{id}/transaction | Settlement Transactions


# **fetch**
> Response fetch(per_page=per_page, page=page)

Fetch Settlements

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from paystack.rest import ApiException
from pprint import pprint


per_page = 50 # int |  (optional)
page = 2 # int |  (optional)

# Fetch Settlements

response = paystack.Settlement.fetch(per_page=per_page, page=page)
pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**|  | [optional] 
 **page** | **int**|  | [optional] 

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

# **transaction**
> Response transaction(id)

Settlement Transactions

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from paystack.rest import ApiException
from pprint import pprint


id = 'id_example' # str | 

# Settlement Transactions

response = paystack.Settlement.transaction(id)
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
**200** | Successful operation |  -  |
**401** | Unauthorized operation |  -  |
**404** | Entity not found |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

