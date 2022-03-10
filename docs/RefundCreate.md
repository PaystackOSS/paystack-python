# RefundCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | **str** | Transaction reference or id | 
**amount** | **int** | Amount ( in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR ) to be refunded to the customer.  Amount cannot be more than the original transaction amount | [optional] 
**currency** | **str** | Three-letter ISO currency. Allowed values are NGN, GHS, ZAR or USD | [optional] 
**customer_note** | **str** | Customer reason | [optional] 
**merchant_note** | **str** | Merchant reason | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


