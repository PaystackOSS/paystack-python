# TransactionChargeAuthorization


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Customer&#39;s email address | 
**amount** | **int** | Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR | 
**authorization_code** | **str** | Valid authorization code to charge | 
**reference** | **str** | Unique transaction reference. Only -, ., &#x3D; and alphanumeric characters allowed. | [optional] 
**currency** | **str** | The transaction currency | [optional] 
**metadata** | **str** | Stringified JSON object of custom data | [optional] 
**split_code** | **str** | The split code of the transaction split | [optional] 
**subaccount** | **str** | The code for the subaccount that owns the payment | [optional] 
**transaction_charge** | **str** | A flat fee to charge the subaccount for a transaction.  This overrides the split percentage set when the subaccount was created | [optional] 
**bearer** | **str** | The beare of the transaction charge | [optional] 
**queue** | **bool** | If you are making a scheduled charge call, it is a good idea to queue them so the processing system does not get overloaded causing transaction processing errors. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


