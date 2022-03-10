# ProductUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of product | [optional] 
**description** | **str** | The description of the product | [optional] 
**price** | **int** | Price should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR | [optional] 
**currency** | **str** | Currency in which price is set. Allowed values are: NGN, GHS, ZAR or USD | [optional] 
**limited** | **bool** | Set to true if the product has limited stock. Leave as false if the product has unlimited stock | [optional] 
**quantity** | **int** | Number of products in stock. Use if limited is true | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


