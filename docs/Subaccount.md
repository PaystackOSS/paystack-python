# paystack.Subaccount

All URIs are relative to *https://api.paystack.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](Subaccount.md#create) | **POST** /subaccount | Create Subaccount
[**fetch**](Subaccount.md#fetch) | **GET** /subaccount/{code} | Fetch Subaccount
[**list**](Subaccount.md#list) | **GET** /subaccount | List Subaccounts
[**update**](Subaccount.md#update) | **PUT** /subaccount/{code} | Update Subaccount


# **create**
> Response create(business_name, settlement_bank, account_number, percentage_charge, description=description, primary_contact_email=primary_contact_email, primary_contact_name=primary_contact_name, primary_contact_phone=primary_contact_phone, metadata=metadata)

Create Subaccount

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

business_name = 'business_name_example' # str | Name of business for subaccount
settlement_bank = 'settlement_bank_example' # str | Bank code for the bank. You can get the list of Bank Codes by calling the List Banks endpoint.
account_number = 'account_number_example' # str | Bank account number
percentage_charge = 3.4 # float | Customer's phone number

# Create Subaccount

response = paystack.Subaccount.create(
    business_name,
    settlement_bank,
    account_number,
    percentage_charge,
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_name** | **str**| Name of business for subaccount | 
 **settlement_bank** | **str**| Bank code for the bank. You can get the list of Bank Codes by calling the List Banks endpoint. | 
 **account_number** | **str**| Bank account number | 
 **percentage_charge** | **float**| Customer&#39;s phone number | 
 **description** | **str**| A description for this subaccount | [optional] 
 **primary_contact_email** | **str**| A contact email for the subaccount | [optional] 
 **primary_contact_name** | **str**| The name of the contact person for this subaccount | [optional] 
 **primary_contact_phone** | **str**| A phone number to call for this subaccount | [optional] 
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
**200** | Request successful |  -  |
**401** | Unauthorized operation |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch**
> Response fetch(code)

Fetch Subaccount

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

code = 'code_example' # str | 

# Fetch Subaccount

response = paystack.Subaccount.fetch(
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
> Response list(per_page=per_page, page=page, _from=_from, to=to)

List Subaccounts

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'


# List Subaccounts

response = paystack.Subaccount.list(
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

# **update**
> Response update(code, business_name=business_name, settlement_bank=settlement_bank, account_number=account_number, active=active, percentage_charge=percentage_charge, description=description, primary_contact_email=primary_contact_email, primary_contact_name=primary_contact_name, primary_contact_phone=primary_contact_phone, metadata=metadata)

Update Subaccount

### Example

* Bearer Authentication (bearerAuth):
```python
import paystack
from pprint import pprint

# Set your API key based on domain (test or live mode)
paystack.api_key = 'sk_domain_xxxxxxxx'

code = 'code_example' # str | 

# Update Subaccount

response = paystack.Subaccount.update(
    code,
)

pprint(response)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **business_name** | **str**| Name of business for subaccount | [optional] 
 **settlement_bank** | **str**| Bank code for the bank. You can get the list of Bank Codes by calling the List Banks endpoint. | [optional] 
 **account_number** | **str**| Bank account number | [optional] 
 **active** | **bool**| Activate or deactivate a subaccount | [optional] 
 **percentage_charge** | **float**| Customer&#39;s phone number | [optional] 
 **description** | **str**| A description for this subaccount | [optional] 
 **primary_contact_email** | **str**| A contact email for the subaccount | [optional] 
 **primary_contact_name** | **str**| The name of the contact person for this subaccount | [optional] 
 **primary_contact_phone** | **str**| A phone number to call for this subaccount | [optional] 
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
**200** | Request successful |  -  |
**401** | Unauthorized operation |  -  |
**404** | Entity not found |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

