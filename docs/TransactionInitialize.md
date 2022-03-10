# TransactionInitialize


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Customer&#39;s email address | 
**amount** | **int** | Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR | 
**currency** | **str** | The transaction currency | [optional] 
**reference** | **str** | Unique transaction reference. Only -, ., &#x3D; and alphanumeric characters allowed. | [optional] 
**callback_url** | **str** | Fully qualified url, e.g. https://example.com/ . Use this to override the callback url provided on the dashboard for this transaction | [optional] 
**plan** | **str** | If transaction is to create a subscription to a predefined plan, provide plan code here.  This would invalidate the value provided in amount | [optional] 
**invoice_limit** | **int** | Number of times to charge customer during subscription to plan | [optional] 
**metadata** | **str** | Stringified JSON object of custom data | [optional] 
**channels** | **list[str]** | An array of payment channels to control what channels you want to make available to the user to make a payment with | [optional] 
**split_code** | **str** | The split code of the transaction split | [optional] 
**subaccount** | **str** | The code for the subaccount that owns the payment | [optional] 
**transaction_charge** | **str** | A flat fee to charge the subaccount for a transaction.  This overrides the split percentage set when the subaccount was created | [optional] 
**bearer** | **str** | The beare of the transaction charge | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


