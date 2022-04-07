# paystack.Split

All URIs are relative to *https://api.paystack.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_subaccount**](Split.md#add_subaccount) | **POST** /split/{id}/subaccount/add | Add Subaccount to Split
[**create**](Split.md#create) | **POST** /split | Create Split
[**fetch**](Split.md#fetch) | **GET** /split/{id} | Fetch Split
[**list**](Split.md#list) | **GET** /split | List/Search Splits
[**remove_subaccount**](Split.md#remove_subaccount) | **POST** /split/{id}/subaccount/remove | Remove Subaccount from split
[**update**](Split.md#update) | **PUT** /split/{id} | Update Split


# **add_subaccount**
> Response add_subaccount(id, subaccount=subaccount, share=share)

Add Subaccount to Split

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from paystack.rest import ApiException
from pprint import pprint


id = 'application/json' # str | 
subaccount = 'subaccount_example' # str | Subaccount code of the customer or partner (optional)
share = 'share_example' # str | The percentage or flat quota of the customer or partner (optional)

# Add Subaccount to Split

response = paystack.Split.add_subaccount(id, subaccount=subaccount, share=share)
pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **subaccount** | **str**| Subaccount code of the customer or partner | [optional] 
 **share** | **str**| The percentage or flat quota of the customer or partner | [optional] 

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
> Response create(name, type, subaccounts, currency, bearer_type=bearer_type, bearer_subaccount=bearer_subaccount)

Create Split

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from paystack.rest import ApiException
from pprint import pprint


name = 'name_example' # str | Name of the transaction split
type = 'type_example' # str | The type of transaction split you want to create.
subaccounts = paystack.SplitSubaccounts() # list[SplitSubaccounts] | A list of object containing subaccount code and number of shares
currency = 'currency_example' # str | The transaction currency
bearer_type = 'bearer_type_example' # str | This allows you specify how the transaction charge should be processed (optional)
bearer_subaccount = 'bearer_subaccount_example' # str | This is the subaccount code of the customer or partner that would bear the transaction charge if you specified subaccount as the bearer type (optional)

# Create Split

response = paystack.Split.create(name, type, subaccounts, currency, bearer_type=bearer_type, bearer_subaccount=bearer_subaccount)
pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the transaction split | 
 **type** | **str**| The type of transaction split you want to create. | 
 **subaccounts** | [**list[SplitSubaccounts]**](SplitSubaccounts.md)| A list of object containing subaccount code and number of shares | 
 **currency** | **str**| The transaction currency | 
 **bearer_type** | **str**| This allows you specify how the transaction charge should be processed | [optional] 
 **bearer_subaccount** | **str**| This is the subaccount code of the customer or partner that would bear the transaction charge if you specified subaccount as the bearer type | [optional] 

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

Fetch Split

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from paystack.rest import ApiException
from pprint import pprint


id = 'id_example' # str | 

# Fetch Split

response = paystack.Split.fetch(id)
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

# **list**
> Response list(name=name, active=active, sort_by=sort_by, _from=_from, to=to, per_page=per_page, page=page)

List/Search Splits

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from paystack.rest import ApiException
from pprint import pprint


name = 'name_example' # str |  (optional)
active = 'active_example' # str |  (optional)
sort_by = 'sort_by_example' # str |  (optional)
_from = '_from_example' # str |  (optional)
to = 'to_example' # str |  (optional)
per_page = 'per_page_example' # str |  (optional)
page = 'page_example' # str |  (optional)

# List/Search Splits

response = paystack.Split.list(name=name, active=active, sort_by=sort_by, _from=_from, to=to, per_page=per_page, page=page)
pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **active** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
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

# **remove_subaccount**
> Response remove_subaccount(id, subaccount=subaccount, share=share)

Remove Subaccount from split

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from paystack.rest import ApiException
from pprint import pprint


id = 'id_example' # str | 
subaccount = 'subaccount_example' # str | Subaccount code of the customer or partner (optional)
share = 'share_example' # str | The percentage or flat quota of the customer or partner (optional)

# Remove Subaccount from split

response = paystack.Split.remove_subaccount(id, subaccount=subaccount, share=share)
pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **subaccount** | **str**| Subaccount code of the customer or partner | [optional] 
 **share** | **str**| The percentage or flat quota of the customer or partner | [optional] 

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
> Response update(id, name=name, active=active, bearer_type=bearer_type, bearer_subaccount=bearer_subaccount)

Update Split

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from paystack.rest import ApiException
from pprint import pprint


id = 'id_example' # str | 
name = 'name_example' # str | Name of the transaction split (optional)
active = True # bool | Toggle status of split. When true, the split is active, else it's inactive (optional)
bearer_type = 'bearer_type_example' # str | This allows you specify how the transaction charge should be processed (optional)
bearer_subaccount = 'bearer_subaccount_example' # str | This is the subaccount code of the customer or partner that would bear the transaction charge if you specified subaccount as the bearer type (optional)

# Update Split

response = paystack.Split.update(id, name=name, active=active, bearer_type=bearer_type, bearer_subaccount=bearer_subaccount)
pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **name** | **str**| Name of the transaction split | [optional] 
 **active** | **bool**| Toggle status of split. When true, the split is active, else it&#39;s inactive | [optional] 
 **bearer_type** | **str**| This allows you specify how the transaction charge should be processed | [optional] 
 **bearer_subaccount** | **str**| This is the subaccount code of the customer or partner that would bear the transaction charge if you specified subaccount as the bearer type | [optional] 

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

