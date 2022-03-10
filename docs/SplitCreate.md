# SplitCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the transaction split | 
**type** | **str** | The type of transaction split you want to create. | 
**subaccounts** | [**list[SplitSubaccounts]**](SplitSubaccounts.md) | A list of object containing subaccount code and number of shares | 
**currency** | **str** | The transaction currency | 
**bearer_type** | **str** | This allows you specify how the transaction charge should be processed | [optional] 
**bearer_subaccount** | **str** | This is the subaccount code of the customer or partner that would bear the transaction charge if you specified subaccount as the bearer type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


