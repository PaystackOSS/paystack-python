# paystack.Dispute

All URIs are relative to *https://api.paystack.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download**](Dispute.md#download) | **GET** /dispute/export | Export Disputes
[**evidence**](Dispute.md#evidence) | **POST** /dispute/{id}/evidence | Add Evidence
[**fetch**](Dispute.md#fetch) | **GET** /dispute/{id} | Fetch Dispute
[**list**](Dispute.md#list) | **GET** /dispute | List Disputes
[**resolve**](Dispute.md#resolve) | **PUT** /dispute/{id}/resolve | Resolve a Dispute
[**transaction**](Dispute.md#transaction) | **GET** /dispute/transaction/{id} | List Transaction Disputes
[**update**](Dispute.md#update) | **PUT** /dispute/{id} | Update Dispute
[**upload_url**](Dispute.md#upload_url) | **GET** /dispute/{id}/upload_url | Get Upload URL


# **download**
> Response download(per_page=per_page, page=page, status=status, _from=_from, to=to)

Export Disputes

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import paystack
from paystack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.paystack.co
# See configuration.py for a list of all supported configuration parameters.
configuration = paystack.Configuration(
    host = "https://api.paystack.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = paystack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with paystack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paystack.Dispute(api_client)
    per_page = 56 # int | Number of records to fetch per page (optional)
page = 56 # int | The section to retrieve (optional)
status = 'status_example' # str |  (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | The start date (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | The end date (optional)

    try:
        # Export Disputes
        api_response = api_instance.download(per_page=per_page, page=page, status=status, _from=_from, to=to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Dispute->download: %s\n" % e)
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
**200** | Successful operation |  -  |
**401** | Unauthorized operation |  -  |
**404** | Entity not found |  -  |
**0** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evidence**
> Response evidence(id, customer_email, customer_name, customer_phone, service_details, delivery_address=delivery_address, delivery_date=delivery_date)

Add Evidence

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import paystack
from paystack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.paystack.co
# See configuration.py for a list of all supported configuration parameters.
configuration = paystack.Configuration(
    host = "https://api.paystack.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = paystack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with paystack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paystack.Dispute(api_client)
    id = 'id_example' # str | Dispute ID
customer_email = 'customer_email_example' # str | Customer email
customer_name = 'customer_name_example' # str | Customer name
customer_phone = 'customer_phone_example' # str | Customer mobile number
service_details = 'service_details_example' # str | Details of service offered
delivery_address = 'delivery_address_example' # str | Delivery address (optional)
delivery_date = '2013-10-20T19:20:30+01:00' # datetime | ISO 8601 representation of delivery date (YYYY-MM-DD) (optional)

    try:
        # Add Evidence
        api_response = api_instance.evidence(id, customer_email, customer_name, customer_phone, service_details, delivery_address=delivery_address, delivery_date=delivery_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Dispute->evidence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Dispute ID | 
 **customer_email** | **str**| Customer email | 
 **customer_name** | **str**| Customer name | 
 **customer_phone** | **str**| Customer mobile number | 
 **service_details** | **str**| Details of service offered | 
 **delivery_address** | **str**| Delivery address | [optional] 
 **delivery_date** | **datetime**| ISO 8601 representation of delivery date (YYYY-MM-DD) | [optional] 

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

Fetch Dispute

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import paystack
from paystack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.paystack.co
# See configuration.py for a list of all supported configuration parameters.
configuration = paystack.Configuration(
    host = "https://api.paystack.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = paystack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with paystack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paystack.Dispute(api_client)
    id = 'id_example' # str | Dispute ID

    try:
        # Fetch Dispute
        api_response = api_instance.fetch(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Dispute->fetch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Dispute ID | 

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
> Response list(per_page=per_page, page=page, status=status, transaction=transaction, _from=_from, to=to)

List Disputes

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import paystack
from paystack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.paystack.co
# See configuration.py for a list of all supported configuration parameters.
configuration = paystack.Configuration(
    host = "https://api.paystack.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = paystack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with paystack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paystack.Dispute(api_client)
    per_page = 56 # int | Number of records to fetch per page (optional)
page = 56 # int | The section to retrieve (optional)
status = 'status_example' # str | Dispute Status. Acceptable values are awaiting-merchant-feedback, awaiting-bank-feedback, pending, resolved (optional)
transaction = 'transaction_example' # str | Transaction ID (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | The start date (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | The end date (optional)

    try:
        # List Disputes
        api_response = api_instance.list(per_page=per_page, page=page, status=status, transaction=transaction, _from=_from, to=to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Dispute->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Number of records to fetch per page | [optional] 
 **page** | **int**| The section to retrieve | [optional] 
 **status** | **str**| Dispute Status. Acceptable values are awaiting-merchant-feedback, awaiting-bank-feedback, pending, resolved | [optional] 
 **transaction** | **str**| Transaction ID | [optional] 
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

# **resolve**
> Response resolve(id, resolution, message, refund_amount, uploaded_filename, evidence=evidence)

Resolve a Dispute

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import paystack
from paystack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.paystack.co
# See configuration.py for a list of all supported configuration parameters.
configuration = paystack.Configuration(
    host = "https://api.paystack.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = paystack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with paystack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paystack.Dispute(api_client)
    id = 'id_example' # str | Dispute ID
resolution = 'resolution_example' # str | Dispute resolution. Accepted values, merchant-accepted, declined
message = 'message_example' # str | Reason for resolving
refund_amount = 'refund_amount_example' # str | The amount to refund, in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
uploaded_filename = 'uploaded_filename_example' # str | Filename of attachment returned via response from the Dispute upload URL
evidence = 56 # int | Evidence Id for fraud claims (optional)

    try:
        # Resolve a Dispute
        api_response = api_instance.resolve(id, resolution, message, refund_amount, uploaded_filename, evidence=evidence)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Dispute->resolve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Dispute ID | 
 **resolution** | **str**| Dispute resolution. Accepted values, merchant-accepted, declined | 
 **message** | **str**| Reason for resolving | 
 **refund_amount** | **str**| The amount to refund, in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR | 
 **uploaded_filename** | **str**| Filename of attachment returned via response from the Dispute upload URL | 
 **evidence** | **int**| Evidence Id for fraud claims | [optional] 

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

# **transaction**
> Response transaction(id)

List Transaction Disputes

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import paystack
from paystack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.paystack.co
# See configuration.py for a list of all supported configuration parameters.
configuration = paystack.Configuration(
    host = "https://api.paystack.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = paystack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with paystack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paystack.Dispute(api_client)
    id = 'id_example' # str | Transaction ID

    try:
        # List Transaction Disputes
        api_response = api_instance.transaction(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Dispute->transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Transaction ID | 

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
> Response update(id, refund_amount, uploaded_filename=uploaded_filename)

Update Dispute

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import paystack
from paystack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.paystack.co
# See configuration.py for a list of all supported configuration parameters.
configuration = paystack.Configuration(
    host = "https://api.paystack.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = paystack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with paystack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paystack.Dispute(api_client)
    id = 'id_example' # str | Dispute ID
refund_amount = 'refund_amount_example' # str | The amount to refund, in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
uploaded_filename = 'uploaded_filename_example' # str | Filename of attachment returned via response from the Dispute upload URL (optional)

    try:
        # Update Dispute
        api_response = api_instance.update(id, refund_amount, uploaded_filename=uploaded_filename)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Dispute->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Dispute ID | 
 **refund_amount** | **str**| The amount to refund, in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR | 
 **uploaded_filename** | **str**| Filename of attachment returned via response from the Dispute upload URL | [optional] 

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

# **upload_url**
> Response upload_url(id)

Get Upload URL

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import paystack
from paystack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.paystack.co
# See configuration.py for a list of all supported configuration parameters.
configuration = paystack.Configuration(
    host = "https://api.paystack.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = paystack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with paystack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paystack.Dispute(api_client)
    id = 'id_example' # str | Dispute ID

    try:
        # Get Upload URL
        api_response = api_instance.upload_url(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Dispute->upload_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Dispute ID | 

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

