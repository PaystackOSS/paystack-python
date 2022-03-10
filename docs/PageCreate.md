# PageCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of page | 
**description** | **str** | The description of the page | [optional] 
**amount** | **int** | Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR | [optional] 
**slug** | **str** | URL slug you would like to be associated with this page. Page will be accessible at https://paystack.com/pay/[slug] | [optional] 
**metadata** | **str** | Stringified JSON object of custom data | [optional] 
**redirect_url** | **str** | If you would like Paystack to redirect to a URL upon successful payment, specify the URL here. | [optional] 
**custom_fields** | **list[object]** | If you would like to accept custom fields, specify them here. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


