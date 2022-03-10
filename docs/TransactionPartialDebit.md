# TransactionPartialDebit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Customer&#39;s email address | 
**amount** | **int** | Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR | 
**authorization_code** | **str** | Valid authorization code to charge | 
**currency** | **str** | The transaction currency | 
**reference** | **str** | Unique transaction reference. Only -, ., &#x3D; and alphanumeric characters allowed. | [optional] 
**at_least** | **str** | Minimum amount to charge | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


