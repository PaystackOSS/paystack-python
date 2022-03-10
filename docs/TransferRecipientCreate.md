# TransferRecipientCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Recipient Type (Only nuban at this time) | 
**name** | **str** | Recipient&#39;s name | 
**account_number** | **str** | Recipient&#39;s bank account number | 
**bank_code** | **str** | Recipient&#39;s bank code. You can get the list of Bank Codes by calling the List Banks endpoint | 
**description** | **str** | A description for this recipient | [optional] 
**currency** | **str** | Currency for the account receiving the transfer | [optional] 
**authorization_code** | **str** | An authorization code from a previous transaction | [optional] 
**metadata** | **str** | Stringified JSON object of custom data | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


