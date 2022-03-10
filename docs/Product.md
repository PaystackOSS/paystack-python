# paystack.Product

All URIs are relative to *https://api.paystack.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](Product.md#create) | **POST** /product | Create Product
[**delete**](Product.md#delete) | **DELETE** /product/{id} | Delete Product
[**fetch**](Product.md#fetch) | **GET** /product/{id} | Fetch Product
[**list**](Product.md#list) | **GET** /product | List Products
[**update**](Product.md#update) | **PUT** /product/{id} | Update product


# **create**
> Response create(name, description, price, currency, limited=limited, quantity=quantity)

Create Product

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
    api_instance = paystack.Product(api_client)
    name = 'name_example' # str | Name of product
description = 'description_example' # str | The description of the product
price = 56 # int | Price should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
currency = 'currency_example' # str | Currency in which price is set. Allowed values are: NGN, GHS, ZAR or USD
limited = True # bool | Set to true if the product has limited stock. Leave as false if the product has unlimited stock (optional)
quantity = 56 # int | Number of products in stock. Use if limited is true (optional)

    try:
        # Create Product
        api_response = api_instance.create(name, description, price, currency, limited=limited, quantity=quantity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Product->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of product | 
 **description** | **str**| The description of the product | 
 **price** | **int**| Price should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR | 
 **currency** | **str**| Currency in which price is set. Allowed values are: NGN, GHS, ZAR or USD | 
 **limited** | **bool**| Set to true if the product has limited stock. Leave as false if the product has unlimited stock | [optional] 
 **quantity** | **int**| Number of products in stock. Use if limited is true | [optional] 

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

# **delete**
> Response delete(id)

Delete Product

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
    api_instance = paystack.Product(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Product
        api_response = api_instance.delete(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Product->delete: %s\n" % e)
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

Fetch Product

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
    api_instance = paystack.Product(api_client)
    id = 'id_example' # str | 

    try:
        # Fetch Product
        api_response = api_instance.fetch(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Product->fetch: %s\n" % e)
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
> Response list(per_page=per_page, page=page, active=active, _from=_from, to=to)

List Products

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
    api_instance = paystack.Product(api_client)
    per_page = 56 # int |  (optional)
page = 56 # int |  (optional)
active = True # bool |  (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | The start date (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | The end date (optional)

    try:
        # List Products
        api_response = api_instance.list(per_page=per_page, page=page, active=active, _from=_from, to=to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Product->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**|  | [optional] 
 **page** | **int**|  | [optional] 
 **active** | **bool**|  | [optional] 
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
> Response update(id, name=name, description=description, price=price, currency=currency, limited=limited, quantity=quantity)

Update product

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
    api_instance = paystack.Product(api_client)
    id = 'id_example' # str | 
name = 'name_example' # str | Name of product (optional)
description = 'description_example' # str | The description of the product (optional)
price = 56 # int | Price should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR (optional)
currency = 'currency_example' # str | Currency in which price is set. Allowed values are: NGN, GHS, ZAR or USD (optional)
limited = True # bool | Set to true if the product has limited stock. Leave as false if the product has unlimited stock (optional)
quantity = 56 # int | Number of products in stock. Use if limited is true (optional)

    try:
        # Update product
        api_response = api_instance.update(id, name=name, description=description, price=price, currency=currency, limited=limited, quantity=quantity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Product->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **name** | **str**| Name of product | [optional] 
 **description** | **str**| The description of the product | [optional] 
 **price** | **int**| Price should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR | [optional] 
 **currency** | **str**| Currency in which price is set. Allowed values are: NGN, GHS, ZAR or USD | [optional] 
 **limited** | **bool**| Set to true if the product has limited stock. Leave as false if the product has unlimited stock | [optional] 
 **quantity** | **int**| Number of products in stock. Use if limited is true | [optional] 

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

