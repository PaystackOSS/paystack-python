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
from paystack.rest import ApiException
from pprint import pprint


business_name = 'business_name_example' # str | Name of business for subaccount
settlement_bank = 'settlement_bank_example' # str | Bank code for the bank. You can get the list of Bank Codes by calling the List Banks endpoint.
account_number = 'account_number_example' # str | Bank account number
percentage_charge = 3.4 # float | Customer's phone number
description = 'description_example' # str | A description for this subaccount (optional)
primary_contact_email = 'primary_contact_email_example' # str | A contact email for the subaccount (optional)
primary_contact_name = 'primary_contact_name_example' # str | The name of the contact person for this subaccount (optional)
primary_contact_phone = 'primary_contact_phone_example' # str | A phone number to call for this subaccount (optional)
metadata = 'metadata_example' # str | Stringified JSON object of custom data (optional)

# Create Subaccount

response = paystack.Subaccount.create(business_name, settlement_bank, account_number, percentage_charge, description=description, primary_contact_email=primary_contact_email, primary_contact_name=primary_contact_name, primary_contact_phone=primary_contact_phone, metadata=metadata)
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
from paystack.rest import ApiException
from pprint import pprint


code = 'code_example' # str | 

# Fetch Subaccount

response = paystack.Subaccount.fetch(code)
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
from paystack.rest import ApiException
from pprint import pprint


per_page = 56 # int | Number of records to fetch per page (optional)
page = 56 # int | The section to retrieve (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | The start date (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | The end date (optional)

# List Subaccounts

response = paystack.Subaccount.list(per_page=per_page, page=page, _from=_from, to=to)
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
from paystack.rest import ApiException
from pprint import pprint


code = 'code_example' # str | 
business_name = 'business_name_example' # str | Name of business for subaccount (optional)
settlement_bank = 'settlement_bank_example' # str | Bank code for the bank. You can get the list of Bank Codes by calling the List Banks endpoint. (optional)
account_number = 'account_number_example' # str | Bank account number (optional)
active = True # bool | Activate or deactivate a subaccount (optional)
percentage_charge = 3.4 # float | Customer's phone number (optional)
description = 'description_example' # str | A description for this subaccount (optional)
primary_contact_email = 'primary_contact_email_example' # str | A contact email for the subaccount (optional)
primary_contact_name = 'primary_contact_name_example' # str | The name of the contact person for this subaccount (optional)
primary_contact_phone = 'primary_contact_phone_example' # str | A phone number to call for this subaccount (optional)
metadata = 'metadata_example' # str | Stringified JSON object of custom data (optional)

# Update Subaccount

response = paystack.Subaccount.update(code, business_name=business_name, settlement_bank=settlement_bank, account_number=account_number, active=active, percentage_charge=percentage_charge, description=description, primary_contact_email=primary_contact_email, primary_contact_name=primary_contact_name, primary_contact_phone=primary_contact_phone, metadata=metadata)
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

