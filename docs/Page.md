# paystack.Page

All URIs are relative to *https://api.paystack.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_products**](Page.md#add_products) | **POST** /page/{id}/product | Add Products
[**check_slug_availability**](Page.md#check_slug_availability) | **GET** /page/check_slug_availability/{slug} | Check Slug Availability
[**create**](Page.md#create) | **POST** /page | Create Page
[**fetch**](Page.md#fetch) | **GET** /page/{id} | Fetch Page
[**list**](Page.md#list) | **GET** /page | List Pages
[**update**](Page.md#update) | **PUT** /page/{id} | Update Page


# **add_products**
> Response add_products(id, product)

Add Products

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from paystack.rest import ApiException
from pprint import pprint


id = 'id_example' # str | 
product = 'product_example' # list[str] | IDs of all products to add to a page

# Add Products

response = paystack.Page.add_products(id, product)
pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **product** | [**list[str]**](str.md)| IDs of all products to add to a page | 

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

# **check_slug_availability**
> Response check_slug_availability(slug)

Check Slug Availability

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from paystack.rest import ApiException
from pprint import pprint


slug = 'slug_example' # str | 

# Check Slug Availability

response = paystack.Page.check_slug_availability(slug)
pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

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
> Response create(name, description=description, amount=amount, slug=slug, metadata=metadata, redirect_url=redirect_url, custom_fields=custom_fields)

Create Page

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from paystack.rest import ApiException
from pprint import pprint


name = 'name_example' # str | Name of page
description = 'description_example' # str | The description of the page (optional)
amount = 56 # int | Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR (optional)
slug = 'slug_example' # str | URL slug you would like to be associated with this page. Page will be accessible at https://paystack.com/pay/[slug] (optional)
metadata = 'metadata_example' # str | Stringified JSON object of custom data (optional)
redirect_url = 'redirect_url_example' # str | If you would like Paystack to redirect to a URL upon successful payment, specify the URL here. (optional)
custom_fields = None # list[object] | If you would like to accept custom fields, specify them here. (optional)

# Create Page

response = paystack.Page.create(name, description=description, amount=amount, slug=slug, metadata=metadata, redirect_url=redirect_url, custom_fields=custom_fields)
pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of page | 
 **description** | **str**| The description of the page | [optional] 
 **amount** | **int**| Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR | [optional] 
 **slug** | **str**| URL slug you would like to be associated with this page. Page will be accessible at https://paystack.com/pay/[slug] | [optional] 
 **metadata** | **str**| Stringified JSON object of custom data | [optional] 
 **redirect_url** | **str**| If you would like Paystack to redirect to a URL upon successful payment, specify the URL here. | [optional] 
 **custom_fields** | [**list[object]**](object.md)| If you would like to accept custom fields, specify them here. | [optional] 

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

Fetch Page

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from paystack.rest import ApiException
from pprint import pprint


id = 'id_example' # str | 

# Fetch Page

response = paystack.Page.fetch(id)
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
> Response list(per_page=per_page, page=page, _from=_from, to=to)

List Pages

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from paystack.rest import ApiException
from pprint import pprint


per_page = 56 # int | Number of records to fetch per page (optional)
page = 56 # int | The section to retrieve (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | The start date (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | The end date (optional)

# List Pages

response = paystack.Page.list(per_page=per_page, page=page, _from=_from, to=to)
pprint(response)
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

# **update**
> Response update(id, name=name, description=description, amount=amount, active=active)

Update Page

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from paystack.rest import ApiException
from pprint import pprint


id = 'id_example' # str | 
name = 'name_example' # str | Name of page (optional)
description = 'description_example' # str | The description of the page (optional)
amount = 56 # int | Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR (optional)
active = True # bool | Set to false to deactivate page url (optional)

# Update Page

response = paystack.Page.update(id, name=name, description=description, amount=amount, active=active)
pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **name** | **str**| Name of page | [optional] 
 **description** | **str**| The description of the page | [optional] 
 **amount** | **int**| Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR | [optional] 
 **active** | **bool**| Set to false to deactivate page url | [optional] 

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

