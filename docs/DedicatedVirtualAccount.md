# paystack.DedicatedVirtualAccount

All URIs are relative to *https://api.paystack.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_split**](DedicatedVirtualAccount.md#add_split) | **POST** /dedicated_account/split | Split Dedicated Account Transaction
[**available_providers**](DedicatedVirtualAccount.md#available_providers) | **GET** /dedicated_account/available_providers | Fetch Bank Providers
[**create**](DedicatedVirtualAccount.md#create) | **POST** /dedicated_account | Create Dedicated Account
[**deactivate**](DedicatedVirtualAccount.md#deactivate) | **DELETE** /dedicated_account/{account_id} | Deactivate Dedicated Account
[**fetch**](DedicatedVirtualAccount.md#fetch) | **GET** /dedicated_account/{account_id} | Fetch Dedicated Account
[**list**](DedicatedVirtualAccount.md#list) | **GET** /dedicated_account | List Dedicated Accounts
[**remove_split**](DedicatedVirtualAccount.md#remove_split) | **DELETE** /dedicated_account/split | Remove Split from Dedicated Account


# **add_split**
> Response add_split(account_number, subaccount=subaccount, split_code=split_code)

Split Dedicated Account Transaction

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

account_number = 'account_number_example' # str | Valid Dedicated virtual account

# Split Dedicated Account Transaction

response = paystack.DedicatedVirtualAccount.add_split(
    account_number,
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| Valid Dedicated virtual account | 
 **subaccount** | **str**| Subaccount code of the account you want to split the transaction with | [optional] 
 **split_code** | **str**| Split code consisting of the lists of accounts you want to split the transaction with | [optional] 

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

# **available_providers**
> Response available_providers()

Fetch Bank Providers

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'


# Fetch Bank Providers

response = paystack.DedicatedVirtualAccount.available_providers()


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

# **create**
> Response create(customer, preferred_bank=preferred_bank, subaccount=subaccount, split_code=split_code)

Create Dedicated Account

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

customer = 'customer_example' # str | Customer ID or code

# Create Dedicated Account

response = paystack.DedicatedVirtualAccount.create(
    customer,
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer** | **str**| Customer ID or code | 
 **preferred_bank** | **str**| The bank slug for preferred bank. To get a list of available banks, use the List Providers endpoint | [optional] 
 **subaccount** | **str**| Subaccount code of the account you want to split the transaction with | [optional] 
 **split_code** | **str**| Split code consisting of the lists of accounts you want to split the transaction with | [optional] 

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

# **deactivate**
> Response deactivate(account_id)

Deactivate Dedicated Account

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

account_id = 'account_id_example' # str | 

# Deactivate Dedicated Account

response = paystack.DedicatedVirtualAccount.deactivate(
    account_id,
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

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

# **fetch**
> Response fetch(account_id)

Fetch Dedicated Account

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

account_id = 'account_id_example' # str | 

# Fetch Dedicated Account

response = paystack.DedicatedVirtualAccount.fetch(
    account_id,
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

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
> Response list(account_number=account_number, customer=customer, active=active, currency=currency, provider_slug=provider_slug, bank_id=bank_id, per_page=per_page, page=page)

List Dedicated Accounts

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'


# List Dedicated Accounts

response = paystack.DedicatedVirtualAccount.list(
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**|  | [optional] 
 **customer** | **str**|  | [optional] 
 **active** | **bool**|  | [optional] 
 **currency** | **str**|  | [optional] 
 **provider_slug** | **str**|  | [optional] 
 **bank_id** | **str**|  | [optional] 
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
**200** | Request successful |  -  |
**401** | Unauthorized operation |  -  |
**404** | Entity not found |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_split**
> Response remove_split(account_number, subaccount=subaccount, split_code=split_code)

Remove Split from Dedicated Account

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

account_number = 'account_number_example' # str | Valid Dedicated virtual account

# Remove Split from Dedicated Account

response = paystack.DedicatedVirtualAccount.remove_split(
    account_number,
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| Valid Dedicated virtual account | 
 **subaccount** | **str**| Subaccount code of the account you want to split the transaction with | [optional] 
 **split_code** | **str**| Split code consisting of the lists of accounts you want to split the transaction with | [optional] 

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

