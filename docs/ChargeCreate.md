# ChargeCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Customer&#39;s email address | 
**amount** | **str** | Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR | 
**authorization_code** | **str** | An authorization code to charge. | [optional] 
**pin** | **str** | 4-digit PIN (send with a non-reusable authorization code) | [optional] 
**reference** | **str** | Unique transaction reference. Only -, .&#x60;, &#x3D; and alphanumeric characters allowed. | [optional] 
**birthday** | **datetime** | The customer&#39;s birthday in the format YYYY-MM-DD e.g 2017-05-16 | [optional] 
**device_id** | **str** | This is the unique identifier of the device a user uses in making payment.  Only -, .&#x60;, &#x3D; and alphanumeric characters are allowed. | [optional] 
**metadata** | **str** | Stringified JSON object of custom data | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


