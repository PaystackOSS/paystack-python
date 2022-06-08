# paystack.Verification

All URIs are relative to *https://api.paystack.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**avs**](Verification.md#avs) | **GET** /address_verification/states | List States (AVS)
[**fetch_banks**](Verification.md#fetch_banks) | **GET** /bank | Fetch Banks
[**list_countries**](Verification.md#list_countries) | **GET** /country | List Countries
[**resolve_account_number**](Verification.md#resolve_account_number) | **GET** /bank/resolve | Resolve Account Number
[**resolve_card_bin**](Verification.md#resolve_card_bin) | **GET** /decision/bin/{bin} | Resolve Card BIN


# **avs**
> Response avs(type=type, country=country, currency=currency)

List States (AVS)

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from paystack.rest import ApiException
from pprint import pprint


type = 'type_example' # str |  (optional)
country = 'country_example' # str |  (optional)
currency = 'currency_example' # str |  (optional)

# List States (AVS)

response = paystack.Verification.avs(type=type, country=country, currency=currency)
pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 
 **country** | **str**|  | [optional] 
 **currency** | **str**|  | [optional] 

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

# **fetch_banks**
> Response fetch_banks(country=country, pay_with_bank_transfer=pay_with_bank_transfer, use_cursor=use_cursor, per_page=per_page, next=next, previous=previous, gateway=gateway)

Fetch Banks

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from paystack.rest import ApiException
from pprint import pprint


country = 'country_example' # str |  (optional)
pay_with_bank_transfer = True # bool |  (optional)
use_cursor = True # bool |  (optional)
per_page = 56 # int |  (optional)
next = 'next_example' # str |  (optional)
previous = 'previous_example' # str |  (optional)
gateway = 'gateway_example' # str |  (optional)

# Fetch Banks

response = paystack.Verification.fetch_banks(country=country, pay_with_bank_transfer=pay_with_bank_transfer, use_cursor=use_cursor, per_page=per_page, next=next, previous=previous, gateway=gateway)
pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**|  | [optional] 
 **pay_with_bank_transfer** | **bool**|  | [optional] 
 **use_cursor** | **bool**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **next** | **str**|  | [optional] 
 **previous** | **str**|  | [optional] 
 **gateway** | **str**|  | [optional] 

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

# **list_countries**
> Response list_countries()

List Countries

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from paystack.rest import ApiException
from pprint import pprint



# List Countries

response = paystack.Verification.list_countries()
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

# **resolve_account_number**
> Response resolve_account_number(account_number=account_number, bank_code=bank_code)

Resolve Account Number

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from paystack.rest import ApiException
from pprint import pprint


account_number = 0022728151 # int |  (optional)
bank_code = 063 # int |  (optional)

# Resolve Account Number

response = paystack.Verification.resolve_account_number(account_number=account_number, bank_code=bank_code)
pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **int**|  | [optional] 
 **bank_code** | **int**|  | [optional] 

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

# **resolve_card_bin**
> Response resolve_card_bin(bin)

Resolve Card BIN

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from paystack.rest import ApiException
from pprint import pprint


bin = 'bin_example' # str | 

# Resolve Card BIN

response = paystack.Verification.resolve_card_bin(bin)
pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bin** | **str**|  | 

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

