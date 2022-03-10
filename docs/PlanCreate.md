# PlanCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of plan | 
**amount** | **int** | Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR | 
**interval** | **str** | Interval in words. Valid intervals are daily, weekly, monthly,biannually, annually | 
**description** | **bool** | A description for this plan | [optional] 
**send_invoices** | **bool** | Set to false if you don&#39;t want invoices to be sent to your customers | [optional] 
**send_sms** | **bool** | Set to false if you don&#39;t want text messages to be sent to your customers | [optional] 
**currency** | **str** | Currency in which amount is set. Allowed values are NGN, GHS, ZAR or USD | [optional] 
**invoice_limit** | **int** | Number of invoices to raise during subscription to this plan.  Can be overridden by specifying an invoice_limit while subscribing. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


