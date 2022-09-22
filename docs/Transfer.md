# paystack.Transfer

All URIs are relative to *https://api.paystack.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk**](Transfer.md#bulk) | **POST** /transfer/bulk | Initiate Bulk Transfer
[**disable_otp**](Transfer.md#disable_otp) | **POST** /transfer/disable_otp | Disable OTP requirement for Transfers
[**disable_otp_finalize**](Transfer.md#disable_otp_finalize) | **POST** /transfer/disable_otp_finalize | Finalize Disabling of OTP requirement for Transfers
[**download**](Transfer.md#download) | **GET** /transfer/export | Export Transfers
[**enable_otp**](Transfer.md#enable_otp) | **POST** /transfer/enable_otp | Enable OTP requirement for Transfers
[**fetch**](Transfer.md#fetch) | **GET** /transfer/{code} | Fetch Transfer
[**finalize**](Transfer.md#finalize) | **POST** /transfer/finalize_transfer | Finalize Transfer
[**initiate**](Transfer.md#initiate) | **POST** /transfer | Initiate Transfer
[**list**](Transfer.md#list) | **GET** /transfer | List Transfers
[**resend_otp**](Transfer.md#resend_otp) | **POST** /transfer/resend_otp | Resend OTP for Transfer
[**verify**](Transfer.md#verify) | **GET** /transfer/verify/{reference} | Verify Transfer


# **bulk**
> Response bulk(source=source, transfers=transfers)

Initiate Bulk Transfer

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'


# Initiate Bulk Transfer

response = paystack.Transfer.bulk(
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| Where should we transfer from? Only balance is allowed for now | [optional] 
 **transfers** | [**list[TransferInitiate]**](TransferInitiate.md)| A list of transfer object. Each object should contain amount, recipient, and reference | [optional] 

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

# **disable_otp**
> Response disable_otp()

Disable OTP requirement for Transfers

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'


# Disable OTP requirement for Transfers

response = paystack.Transfer.disable_otp()


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
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_otp_finalize**
> Response disable_otp_finalize(otp)

Finalize Disabling of OTP requirement for Transfers

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

otp = 'otp_example' # str | OTP sent to business phone to verify disabling OTP requirement

# Finalize Disabling of OTP requirement for Transfers

response = paystack.Transfer.disable_otp_finalize(
    otp,
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otp** | **str**| OTP sent to business phone to verify disabling OTP requirement | 

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

# **download**
> Response download(per_page=per_page, page=page, status=status, _from=_from, to=to)

Export Transfers

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'


# Export Transfers

response = paystack.Transfer.download(
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Number of records to fetch per page | [optional] 
 **page** | **int**| The section to retrieve | [optional] 
 **status** | **str**|  | [optional] 
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

# **enable_otp**
> Response enable_otp()

Enable OTP requirement for Transfers

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'


# Enable OTP requirement for Transfers

response = paystack.Transfer.enable_otp()


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
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch**
> Response fetch(code)

Fetch Transfer

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

code = 'code_example' # str | Transfer code

# Fetch Transfer

response = paystack.Transfer.fetch(
    code,
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Transfer code | 

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
> Response finalize(transfer_code, otp)

Finalize Transfer

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

transfer_code = 'transfer_code_example' # str | The transfer code you want to finalize
otp = 'otp_example' # str | OTP sent to business phone to verify transfer

# Finalize Transfer

response = paystack.Transfer.finalize(
    transfer_code,
    otp,
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_code** | **str**| The transfer code you want to finalize | 
 **otp** | **str**| OTP sent to business phone to verify transfer | 

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

# **initiate**
> Response initiate(source, amount, recipient, reason=reason, currency=currency, reference=reference)

Initiate Transfer

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

source = 'source_example' # str | Where should we transfer from? Only balance is allowed for now
amount = 'amount_example' # str | Amount to transfer in kobo if currency is NGN and pesewas if currency is GHS.
recipient = 'recipient_example' # str | The transfer recipient's code

# Initiate Transfer

response = paystack.Transfer.initiate(
    source,
    amount,
    recipient,
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| Where should we transfer from? Only balance is allowed for now | 
 **amount** | **str**| Amount to transfer in kobo if currency is NGN and pesewas if currency is GHS. | 
 **recipient** | **str**| The transfer recipient&#39;s code | 
 **reason** | **str**| The reason or narration for the transfer. | [optional] 
 **currency** | **str**| Specify the currency of the transfer. Defaults to NGN. | [optional] 
 **reference** | **str**| If specified, the field should be a unique identifier (in lowercase) for the object.  Only -,_ and alphanumeric characters are allowed. | [optional] 

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

# **list**
> Response list(per_page=per_page, page=page, status=status, _from=_from, to=to)

List Transfers

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'


# List Transfers

response = paystack.Transfer.list(
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Number of records to fetch per page | [optional] 
 **page** | **int**| The section to retrieve | [optional] 
 **status** | **str**|  | [optional] 
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

# **resend_otp**
> Response resend_otp(transfer_code, reason)

Resend OTP for Transfer

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

transfer_code = 'transfer_code_example' # str | The transfer code that requires an OTP validation
reason = 'reason_example' # str | Either resend_otp or transfer

# Resend OTP for Transfer

response = paystack.Transfer.resend_otp(
    transfer_code,
    reason,
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_code** | **str**| The transfer code that requires an OTP validation | 
 **reason** | **str**| Either resend_otp or transfer | 

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

# **verify**
> Response verify(reference)

Verify Transfer

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

reference = 'reference_example' # str | 

# Verify Transfer

response = paystack.Transfer.verify(
    reference,
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference** | **str**|  | 

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

