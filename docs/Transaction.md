# paystack.Transaction

All URIs are relative to *https://api.paystack.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**charge_authorization**](Transaction.md#charge_authorization) | **POST** /transaction/charge_authorization | Charge Authorization
[**check_authorization**](Transaction.md#check_authorization) | **POST** /transaction/check_authorization | Check Authorization
[**download**](Transaction.md#download) | **GET** /transaction/export | Export Transactions
[**event**](Transaction.md#event) | **GET** /transaction/{id}/event | Get Transaction Event
[**fetch**](Transaction.md#fetch) | **GET** /transaction/{id} | Fetch Transaction
[**initialize**](Transaction.md#initialize) | **POST** /transaction/initialize | Initialize Transaction
[**list**](Transaction.md#list) | **GET** /transaction | List Transactions
[**partial_debit**](Transaction.md#partial_debit) | **POST** /transaction/partial_debit | Partial Debit
[**session**](Transaction.md#session) | **GET** /transaction/{id}/session | Get Transaction Session
[**timeline**](Transaction.md#timeline) | **GET** /transaction/timeline/{id_or_reference} | Fetch Transaction Timeline
[**totals**](Transaction.md#totals) | **GET** /transaction/totals | Transaction Totals
[**verify**](Transaction.md#verify) | **GET** /transaction/verify/{reference} | Verify Transaction


# **charge_authorization**
> Response charge_authorization(email, amount, authorization_code, reference=reference, currency=currency, metadata=metadata, split_code=split_code, subaccount=subaccount, transaction_charge=transaction_charge, bearer=bearer, queue=queue)

Charge Authorization

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
    api_instance = paystack.Transaction(api_client)
    email = 'email_example' # str | Customer's email address
amount = 56 # int | Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
authorization_code = 'authorization_code_example' # str | Valid authorization code to charge
reference = 'reference_example' # str | Unique transaction reference. Only -, ., = and alphanumeric characters allowed. (optional)
currency = 'currency_example' # str | The transaction currency (optional)
metadata = 'metadata_example' # str | Stringified JSON object of custom data (optional)
split_code = 'split_code_example' # str | The split code of the transaction split (optional)
subaccount = 'subaccount_example' # str | The code for the subaccount that owns the payment (optional)
transaction_charge = 'transaction_charge_example' # str | A flat fee to charge the subaccount for a transaction.  This overrides the split percentage set when the subaccount was created (optional)
bearer = 'bearer_example' # str | The beare of the transaction charge (optional)
queue = True # bool | If you are making a scheduled charge call, it is a good idea to queue them so the processing system does not get overloaded causing transaction processing errors. (optional)

    try:
        # Charge Authorization
        api_response = api_instance.charge_authorization(email, amount, authorization_code, reference=reference, currency=currency, metadata=metadata, split_code=split_code, subaccount=subaccount, transaction_charge=transaction_charge, bearer=bearer, queue=queue)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Transaction->charge_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Customer&#39;s email address | 
 **amount** | **int**| Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR | 
 **authorization_code** | **str**| Valid authorization code to charge | 
 **reference** | **str**| Unique transaction reference. Only -, ., &#x3D; and alphanumeric characters allowed. | [optional] 
 **currency** | **str**| The transaction currency | [optional] 
 **metadata** | **str**| Stringified JSON object of custom data | [optional] 
 **split_code** | **str**| The split code of the transaction split | [optional] 
 **subaccount** | **str**| The code for the subaccount that owns the payment | [optional] 
 **transaction_charge** | **str**| A flat fee to charge the subaccount for a transaction.  This overrides the split percentage set when the subaccount was created | [optional] 
 **bearer** | **str**| The beare of the transaction charge | [optional] 
 **queue** | **bool**| If you are making a scheduled charge call, it is a good idea to queue them so the processing system does not get overloaded causing transaction processing errors. | [optional] 

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

# **check_authorization**
> Response check_authorization(email, amount, authorization_code=authorization_code, currency=currency)

Check Authorization

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
    api_instance = paystack.Transaction(api_client)
    email = 'email_example' # str | Customer's email address
amount = 56 # int | Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
authorization_code = 'authorization_code_example' # str | Valid authorization code to charge (optional)
currency = 'currency_example' # str | The transaction currency (optional)

    try:
        # Check Authorization
        api_response = api_instance.check_authorization(email, amount, authorization_code=authorization_code, currency=currency)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Transaction->check_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Customer&#39;s email address | 
 **amount** | **int**| Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR | 
 **authorization_code** | **str**| Valid authorization code to charge | [optional] 
 **currency** | **str**| The transaction currency | [optional] 

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

# **download**
> Response download(per_page=per_page, page=page, _from=_from, to=to)

Export Transactions

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
    api_instance = paystack.Transaction(api_client)
    per_page = 56 # int | Number of records to fetch per page (optional)
page = 56 # int | The section to retrieve (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | The start date (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | The end date (optional)

    try:
        # Export Transactions
        api_response = api_instance.download(per_page=per_page, page=page, _from=_from, to=to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Transaction->download: %s\n" % e)
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

# **event**
> Response event(id)

Get Transaction Event

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
    api_instance = paystack.Transaction(api_client)
    id = 'id_example' # str | 

    try:
        # Get Transaction Event
        api_response = api_instance.event(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Transaction->event: %s\n" % e)
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

# **fetch**
> Response fetch(id)

Fetch Transaction

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
    api_instance = paystack.Transaction(api_client)
    id = 'id_example' # str | The ID of the transaction to fetch

    try:
        # Fetch Transaction
        api_response = api_instance.fetch(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Transaction->fetch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the transaction to fetch | 

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

# **initialize**
> Response initialize(email, amount, currency=currency, reference=reference, callback_url=callback_url, plan=plan, invoice_limit=invoice_limit, metadata=metadata, channels=channels, split_code=split_code, subaccount=subaccount, transaction_charge=transaction_charge, bearer=bearer)

Initialize Transaction

Create a new transaction

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
    api_instance = paystack.Transaction(api_client)
    email = 'email_example' # str | Customer's email address
amount = 56 # int | Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
currency = 'currency_example' # str | The transaction currency (optional)
reference = 'reference_example' # str | Unique transaction reference. Only -, ., = and alphanumeric characters allowed. (optional)
callback_url = 'callback_url_example' # str | Fully qualified url, e.g. https://example.com/ . Use this to override the callback url provided on the dashboard for this transaction (optional)
plan = 'plan_example' # str | If transaction is to create a subscription to a predefined plan, provide plan code here.  This would invalidate the value provided in amount (optional)
invoice_limit = 56 # int | Number of times to charge customer during subscription to plan (optional)
metadata = 'metadata_example' # str | Stringified JSON object of custom data (optional)
channels = 'channels_example' # list[str] | An array of payment channels to control what channels you want to make available to the user to make a payment with (optional)
split_code = 'split_code_example' # str | The split code of the transaction split (optional)
subaccount = 'subaccount_example' # str | The code for the subaccount that owns the payment (optional)
transaction_charge = 'transaction_charge_example' # str | A flat fee to charge the subaccount for a transaction.  This overrides the split percentage set when the subaccount was created (optional)
bearer = 'bearer_example' # str | The beare of the transaction charge (optional)

    try:
        # Initialize Transaction
        api_response = api_instance.initialize(email, amount, currency=currency, reference=reference, callback_url=callback_url, plan=plan, invoice_limit=invoice_limit, metadata=metadata, channels=channels, split_code=split_code, subaccount=subaccount, transaction_charge=transaction_charge, bearer=bearer)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Transaction->initialize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Customer&#39;s email address | 
 **amount** | **int**| Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR | 
 **currency** | **str**| The transaction currency | [optional] 
 **reference** | **str**| Unique transaction reference. Only -, ., &#x3D; and alphanumeric characters allowed. | [optional] 
 **callback_url** | **str**| Fully qualified url, e.g. https://example.com/ . Use this to override the callback url provided on the dashboard for this transaction | [optional] 
 **plan** | **str**| If transaction is to create a subscription to a predefined plan, provide plan code here.  This would invalidate the value provided in amount | [optional] 
 **invoice_limit** | **int**| Number of times to charge customer during subscription to plan | [optional] 
 **metadata** | **str**| Stringified JSON object of custom data | [optional] 
 **channels** | [**list[str]**](str.md)| An array of payment channels to control what channels you want to make available to the user to make a payment with | [optional] 
 **split_code** | **str**| The split code of the transaction split | [optional] 
 **subaccount** | **str**| The code for the subaccount that owns the payment | [optional] 
 **transaction_charge** | **str**| A flat fee to charge the subaccount for a transaction.  This overrides the split percentage set when the subaccount was created | [optional] 
 **bearer** | **str**| The beare of the transaction charge | [optional] 

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

# **list**
> Response list(per_page=per_page, page=page, _from=_from, to=to)

List Transactions

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
    api_instance = paystack.Transaction(api_client)
    per_page = 56 # int | Number of records to fetch per page (optional)
page = 56 # int | The section to retrieve (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | The start date (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | The end date (optional)

    try:
        # List Transactions
        api_response = api_instance.list(per_page=per_page, page=page, _from=_from, to=to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Transaction->list: %s\n" % e)
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

# **partial_debit**
> Response partial_debit(email, amount, authorization_code, currency, reference=reference, at_least=at_least)

Partial Debit

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
    api_instance = paystack.Transaction(api_client)
    email = 'email_example' # str | Customer's email address
amount = 56 # int | Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
authorization_code = 'authorization_code_example' # str | Valid authorization code to charge
currency = 'currency_example' # str | The transaction currency
reference = 'reference_example' # str | Unique transaction reference. Only -, ., = and alphanumeric characters allowed. (optional)
at_least = 'at_least_example' # str | Minimum amount to charge (optional)

    try:
        # Partial Debit
        api_response = api_instance.partial_debit(email, amount, authorization_code, currency, reference=reference, at_least=at_least)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Transaction->partial_debit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Customer&#39;s email address | 
 **amount** | **int**| Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR | 
 **authorization_code** | **str**| Valid authorization code to charge | 
 **currency** | **str**| The transaction currency | 
 **reference** | **str**| Unique transaction reference. Only -, ., &#x3D; and alphanumeric characters allowed. | [optional] 
 **at_least** | **str**| Minimum amount to charge | [optional] 

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

# **session**
> Response session(id)

Get Transaction Session

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
    api_instance = paystack.Transaction(api_client)
    id = 'id_example' # str | 

    try:
        # Get Transaction Session
        api_response = api_instance.session(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Transaction->session: %s\n" % e)
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

# **timeline**
> Response timeline(id_or_reference)

Fetch Transaction Timeline

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
    api_instance = paystack.Transaction(api_client)
    id_or_reference = 'id_or_reference_example' # str | 

    try:
        # Fetch Transaction Timeline
        api_response = api_instance.timeline(id_or_reference)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Transaction->timeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_reference** | **str**|  | 

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

# **totals**
> Response totals(per_page=per_page, page=page, _from=_from, to=to)

Transaction Totals

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
    api_instance = paystack.Transaction(api_client)
    per_page = 56 # int | Number of records to fetch per page (optional)
page = 56 # int | The section to retrieve (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | The start date (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | The end date (optional)

    try:
        # Transaction Totals
        api_response = api_instance.totals(per_page=per_page, page=page, _from=_from, to=to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Transaction->totals: %s\n" % e)
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

# **verify**
> Response verify(reference)

Verify Transaction

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
    api_instance = paystack.Transaction(api_client)
    reference = 'reference_example' # str | The transaction reference to verify

    try:
        # Verify Transaction
        api_response = api_instance.verify(reference)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Transaction->verify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference** | **str**| The transaction reference to verify | 

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

