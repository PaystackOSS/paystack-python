# paystack.TransferRecipient

All URIs are relative to *https://api.paystack.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk**](TransferRecipient.md#bulk) | **POST** /transferrecipient/bulk | Bulk Create Transfer Recipient
[**create**](TransferRecipient.md#create) | **POST** /transferrecipient | Create Transfer Recipient
[**fetch**](TransferRecipient.md#fetch) | **GET** /transferrecipient/{code} | Fetch Transfer recipient
[**list**](TransferRecipient.md#list) | **GET** /transferrecipient | List Transfer Recipients
[**transferrecipient_code_delete**](TransferRecipient.md#transferrecipient_code_delete) | **DELETE** /transferrecipient/{code} | Delete Transfer Recipient
[**transferrecipient_code_put**](TransferRecipient.md#transferrecipient_code_put) | **PUT** /transferrecipient/{code} | Update Transfer recipient


# **bulk**
> Response bulk(batch)

Bulk Create Transfer Recipient

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

batch = paystack.TransferRecipientCreate() # list[TransferRecipientCreate] | A list of transfer recipient object. Each object should contain type, name, and bank_code.  Any Create Transfer Recipient param can also be passed.

# Bulk Create Transfer Recipient

response = paystack.TransferRecipient.bulk(
    batch,
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch** | [**list[TransferRecipientCreate]**](TransferRecipientCreate.md)| A list of transfer recipient object. Each object should contain type, name, and bank_code.  Any Create Transfer Recipient param can also be passed. | 

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

# **create**
> Response create(type, name, account_number, bank_code, description=description, currency=currency, authorization_code=authorization_code, metadata=metadata)

Create Transfer Recipient

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

type = 'type_example' # str | Recipient Type (Only nuban at this time)
name = 'name_example' # str | Recipient's name
account_number = 'account_number_example' # str | Recipient's bank account number
bank_code = 'bank_code_example' # str | Recipient's bank code. You can get the list of Bank Codes by calling the List Banks endpoint

# Create Transfer Recipient

response = paystack.TransferRecipient.create(
    type,
    name,
    account_number,
    bank_code,
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Recipient Type (Only nuban at this time) | 
 **name** | **str**| Recipient&#39;s name | 
 **account_number** | **str**| Recipient&#39;s bank account number | 
 **bank_code** | **str**| Recipient&#39;s bank code. You can get the list of Bank Codes by calling the List Banks endpoint | 
 **description** | **str**| A description for this recipient | [optional] 
 **currency** | **str**| Currency for the account receiving the transfer | [optional] 
 **authorization_code** | **str**| An authorization code from a previous transaction | [optional] 
 **metadata** | **str**| Stringified JSON object of custom data | [optional] 

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

Fetch Transfer recipient

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

code = 'code_example' # str | Transfer recipient code

# Fetch Transfer recipient

response = paystack.TransferRecipient.fetch(
    code,
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Transfer recipient code | 

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
> Response list(per_page=per_page, page=page, _from=_from, to=to)

List Transfer Recipients

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'


# List Transfer Recipients

response = paystack.TransferRecipient.list(
)

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
**200** | Request successful |  -  |
**401** | Unauthorized operation |  -  |
**404** | Entity not found |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transferrecipient_code_delete**
> Response transferrecipient_code_delete(code)

Delete Transfer Recipient

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

code = 'code_example' # str | Transfer recipient code

# Delete Transfer Recipient

response = paystack.TransferRecipient.transferrecipient_code_delete(
    code,
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Transfer recipient code | 

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

# **transferrecipient_code_put**
> Response transferrecipient_code_put(code, name=name, email=email)

Update Transfer recipient

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

code = 'code_example' # str | Transfer recipient code

# Update Transfer recipient

response = paystack.TransferRecipient.transferrecipient_code_put(
    code,
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Transfer recipient code | 
 **name** | **str**| Recipient&#39;s name | [optional] 
 **email** | **str**| Recipient&#39;s email address | [optional] 

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

