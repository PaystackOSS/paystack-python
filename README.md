# paystack

A Python client library for consuming the Paystack API.

## Prerequisite
This library is supported on Python 2.7 and 3.4+. Also, you need to [create a Paystack account](https://dashboard.paystack.com/#/signup), if you don't have one already, to get your test and 
live secret keys.

## Installation
```
pip install paystack-sdk
```
You may need to run `pip` with root permission: `sudo pip install` 

## Getting Started

```python
import paystack
from pprint import pprint

paystack.api_key = 'sk_domain_xxxxx'

response = paystack.Customer.create(
        email="larry@james.com",
        first_name="Larry",
        last_name="James"
    )
pprint(response)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.paystack.co*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*Balance* | [**fetch**](docs/Balance.md#fetch) | **GET** /balance | Fetch Balance
*Balance* | [**ledger**](docs/Balance.md#ledger) | **GET** /balance/ledger | Balance Ledger
*BulkCharge* | [**charges**](docs/BulkCharge.md#charges) | **GET** /bulkcharge/{code}/charges | Fetch Charges in a Batch
*BulkCharge* | [**fetch**](docs/BulkCharge.md#fetch) | **GET** /bulkcharge/{code} | Fetch Bulk Charge Batch
*BulkCharge* | [**initiate**](docs/BulkCharge.md#initiate) | **POST** /bulkcharge | Initiate Bulk Charge
*BulkCharge* | [**list**](docs/BulkCharge.md#list) | **GET** /bulkcharge | List Bulk Charge Batches
*BulkCharge* | [**pause**](docs/BulkCharge.md#pause) | **GET** /bulkcharge/pause/{code} | Pause Bulk Charge Batch
*BulkCharge* | [**resume**](docs/BulkCharge.md#resume) | **GET** /bulkcharge/resume/{code} | Resume Bulk Charge Batch
*Charge* | [**check**](docs/Charge.md#check) | **GET** /charge/{reference} | Check pending charge
*Charge* | [**create**](docs/Charge.md#create) | **POST** /charge | Create Charge
*Charge* | [**submit_address**](docs/Charge.md#submit_address) | **POST** /charge/submit_address | Submit Address
*Charge* | [**submit_birthday**](docs/Charge.md#submit_birthday) | **POST** /charge/submit_birthday | Submit Birthday
*Charge* | [**submit_otp**](docs/Charge.md#submit_otp) | **POST** /charge/submit_otp | Submit OTP
*Charge* | [**submit_phone**](docs/Charge.md#submit_phone) | **POST** /charge/submit_phone | Submit Phone
*Charge* | [**submit_pin**](docs/Charge.md#submit_pin) | **POST** /charge/submit_pin | Submit PIN
*Customer* | [**create**](docs/Customer.md#create) | **POST** /customer | Create Customer
*Customer* | [**deactivate_authorization**](docs/Customer.md#deactivate_authorization) | **POST** /customer/deactivate_authorization | Deactivate Authorization
*Customer* | [**fetch**](docs/Customer.md#fetch) | **GET** /customer/{code} | Fetch Customer
*Customer* | [**list**](docs/Customer.md#list) | **GET** /customer | List Customers
*Customer* | [**risk_action**](docs/Customer.md#risk_action) | **POST** /customer/set_risk_action | White/blacklist Customer
*Customer* | [**update**](docs/Customer.md#update) | **PUT** /customer/{code} | Update Customer
*Customer* | [**validate**](docs/Customer.md#validate) | **POST** /customer/{code}/identification | Validate Customer
*DedicatedVirtualAccount* | [**add_split**](docs/DedicatedVirtualAccount.md#add_split) | **POST** /dedicated_account/split | Split Dedicated Account Transaction
*DedicatedVirtualAccount* | [**available_providers**](docs/DedicatedVirtualAccount.md#available_providers) | **GET** /dedicated_account/available_providers | Fetch Bank Providers
*DedicatedVirtualAccount* | [**create**](docs/DedicatedVirtualAccount.md#create) | **POST** /dedicated_account | Create Dedicated Account
*DedicatedVirtualAccount* | [**deactivate**](docs/DedicatedVirtualAccount.md#deactivate) | **DELETE** /dedicated_account/{account_id} | Deactivate Dedicated Account
*DedicatedVirtualAccount* | [**fetch**](docs/DedicatedVirtualAccount.md#fetch) | **GET** /dedicated_account/{account_id} | Fetch Dedicated Account
*DedicatedVirtualAccount* | [**list**](docs/DedicatedVirtualAccount.md#list) | **GET** /dedicated_account | List Dedicated Accounts
*DedicatedVirtualAccount* | [**remove_split**](docs/DedicatedVirtualAccount.md#remove_split) | **DELETE** /dedicated_account/split | Remove Split from Dedicated Account
*Dispute* | [**download**](docs/Dispute.md#download) | **GET** /dispute/export | Export Disputes
*Dispute* | [**evidence**](docs/Dispute.md#evidence) | **POST** /dispute/{id}/evidence | Add Evidence
*Dispute* | [**fetch**](docs/Dispute.md#fetch) | **GET** /dispute/{id} | Fetch Dispute
*Dispute* | [**list**](docs/Dispute.md#list) | **GET** /dispute | List Disputes
*Dispute* | [**resolve**](docs/Dispute.md#resolve) | **PUT** /dispute/{id}/resolve | Resolve a Dispute
*Dispute* | [**transaction**](docs/Dispute.md#transaction) | **GET** /dispute/transaction/{id} | List Transaction Disputes
*Dispute* | [**update**](docs/Dispute.md#update) | **PUT** /dispute/{id} | Update Dispute
*Dispute* | [**upload_url**](docs/Dispute.md#upload_url) | **GET** /dispute/{id}/upload_url | Get Upload URL
*Integration* | [**fetch_payment_session_timeout**](docs/Integration.md#fetch_payment_session_timeout) | **GET** /integration/payment_session_timeout | Fetch Payment Session Timeout
*Integration* | [**update_payment_session_timeout**](docs/Integration.md#update_payment_session_timeout) | **PUT** /integration/payment_session_timeout | Update Payment Session Timeout
*Page* | [**add_products**](docs/Page.md#add_products) | **POST** /page/{id}/product | Add Products
*Page* | [**check_slug_availability**](docs/Page.md#check_slug_availability) | **GET** /page/check_slug_availability/{slug} | Check Slug Availability
*Page* | [**create**](docs/Page.md#create) | **POST** /page | Create Page
*Page* | [**fetch**](docs/Page.md#fetch) | **GET** /page/{id} | Fetch Page
*Page* | [**list**](docs/Page.md#list) | **GET** /page | List Pages
*Page* | [**update**](docs/Page.md#update) | **PUT** /page/{id} | Update Page
*PaymentRequest* | [**archive**](docs/PaymentRequest.md#archive) | **POST** /paymentrequest/archive/{id} | Archive Payment Request
*PaymentRequest* | [**create**](docs/PaymentRequest.md#create) | **POST** /paymentrequest | Create Payment Request
*PaymentRequest* | [**fetch**](docs/PaymentRequest.md#fetch) | **GET** /paymentrequest/{id} | Fetch Payment Request
*PaymentRequest* | [**finalize**](docs/PaymentRequest.md#finalize) | **POST** /paymentrequest/finalize/{id} | Finalize Payment Request
*PaymentRequest* | [**list**](docs/PaymentRequest.md#list) | **GET** /paymentrequest | List Payment Request
*PaymentRequest* | [**notify**](docs/PaymentRequest.md#notify) | **POST** /paymentrequest/notify/{id} | Send Notification
*PaymentRequest* | [**totals**](docs/PaymentRequest.md#totals) | **GET** /paymentrequest/totals | Payment Request Total
*PaymentRequest* | [**update**](docs/PaymentRequest.md#update) | **PUT** /paymentrequest/{id} | Update Payment Request
*PaymentRequest* | [**verify**](docs/PaymentRequest.md#verify) | **GET** /paymentrequest/verify/{id} | Verify Payment Request
*Plan* | [**create**](docs/Plan.md#create) | **POST** /plan | Create Plan
*Plan* | [**fetch**](docs/Plan.md#fetch) | **GET** /plan/{code} | Fetch Plan
*Plan* | [**list**](docs/Plan.md#list) | **GET** /plan | List Plans
*Plan* | [**update**](docs/Plan.md#update) | **PUT** /plan/{code} | Update Plan
*Product* | [**create**](docs/Product.md#create) | **POST** /product | Create Product
*Product* | [**delete**](docs/Product.md#delete) | **DELETE** /product/{id} | Delete Product
*Product* | [**fetch**](docs/Product.md#fetch) | **GET** /product/{id} | Fetch Product
*Product* | [**list**](docs/Product.md#list) | **GET** /product | List Products
*Product* | [**update**](docs/Product.md#update) | **PUT** /product/{id} | Update product
*Refund* | [**create**](docs/Refund.md#create) | **POST** /refund | Create Refund
*Refund* | [**fetch**](docs/Refund.md#fetch) | **GET** /refund/{id} | Fetch Refund
*Refund* | [**list**](docs/Refund.md#list) | **GET** /refund | List Refunds
*Settlement* | [**fetch**](docs/Settlement.md#fetch) | **GET** /settlement | Fetch Settlements
*Settlement* | [**transaction**](docs/Settlement.md#transaction) | **GET** /settlement/{id}/transaction | Settlement Transactions
*Split* | [**add_subaccount**](docs/Split.md#add_subaccount) | **POST** /split/{id}/subaccount/add | Add Subaccount to Split
*Split* | [**create**](docs/Split.md#create) | **POST** /split | Create Split
*Split* | [**fetch**](docs/Split.md#fetch) | **GET** /split/{id} | Fetch Split
*Split* | [**list**](docs/Split.md#list) | **GET** /split | List/Search Splits
*Split* | [**remove_subaccount**](docs/Split.md#remove_subaccount) | **POST** /split/{id}/subaccount/remove | Remove Subaccount from split
*Split* | [**update**](docs/Split.md#update) | **PUT** /split/{id} | Update Split
*Subaccount* | [**create**](docs/Subaccount.md#create) | **POST** /subaccount | Create Subaccount
*Subaccount* | [**fetch**](docs/Subaccount.md#fetch) | **GET** /subaccount/{code} | Fetch Subaccount
*Subaccount* | [**list**](docs/Subaccount.md#list) | **GET** /subaccount | List Subaccounts
*Subaccount* | [**update**](docs/Subaccount.md#update) | **PUT** /subaccount/{code} | Update Subaccount
*Subscription* | [**create**](docs/Subscription.md#create) | **POST** /subscription | Create Subscription
*Subscription* | [**disable**](docs/Subscription.md#disable) | **POST** /subscription/disable | Disable Subscription
*Subscription* | [**enable**](docs/Subscription.md#enable) | **POST** /subscription/enable | Enable Subscription
*Subscription* | [**fetch**](docs/Subscription.md#fetch) | **GET** /subscription/{code} | Fetch Subscription
*Subscription* | [**list**](docs/Subscription.md#list) | **GET** /subscription | List Subscriptions
*Subscription* | [**manage_email**](docs/Subscription.md#manage_email) | **POST** /subscription/{code}/manage/email | Send Update Subscription Link
*Subscription* | [**manage_link**](docs/Subscription.md#manage_link) | **POST** /subscription/{code}/manage/link | Generate Update Subscription Link
*Transaction* | [**charge_authorization**](docs/Transaction.md#charge_authorization) | **POST** /transaction/charge_authorization | Charge Authorization
*Transaction* | [**check_authorization**](docs/Transaction.md#check_authorization) | **POST** /transaction/check_authorization | Check Authorization
*Transaction* | [**download**](docs/Transaction.md#download) | **GET** /transaction/export | Export Transactions
*Transaction* | [**event**](docs/Transaction.md#event) | **GET** /transaction/{id}/event | Get Transaction Event
*Transaction* | [**fetch**](docs/Transaction.md#fetch) | **GET** /transaction/{id} | Fetch Transaction
*Transaction* | [**initialize**](docs/Transaction.md#initialize) | **POST** /transaction/initialize | Initialize Transaction
*Transaction* | [**list**](docs/Transaction.md#list) | **GET** /transaction | List Transactions
*Transaction* | [**partial_debit**](docs/Transaction.md#partial_debit) | **POST** /transaction/partial_debit | Partial Debit
*Transaction* | [**session**](docs/Transaction.md#session) | **GET** /transaction/{id}/session | Get Transaction Session
*Transaction* | [**timeline**](docs/Transaction.md#timeline) | **GET** /transaction/timeline/{id_or_reference} | Fetch Transaction Timeline
*Transaction* | [**totals**](docs/Transaction.md#totals) | **GET** /transaction/totals | Transaction Totals
*Transaction* | [**verify**](docs/Transaction.md#verify) | **GET** /transaction/verify/{reference} | Verify Transaction
*Transfer* | [**bulk**](docs/Transfer.md#bulk) | **POST** /transfer/bulk | Initiate Bulk Transfer
*Transfer* | [**disable_otp**](docs/Transfer.md#disable_otp) | **POST** /transfer/disable_otp | Disable OTP requirement for Transfers
*Transfer* | [**disable_otp_finalize**](docs/Transfer.md#disable_otp_finalize) | **POST** /transfer/disable_otp_finalize | Finalize Disabling of OTP requirement for Transfers
*Transfer* | [**download**](docs/Transfer.md#download) | **GET** /transfer/export | Export Transfers
*Transfer* | [**enable_otp**](docs/Transfer.md#enable_otp) | **POST** /transfer/enable_otp | Enable OTP requirement for Transfers
*Transfer* | [**fetch**](docs/Transfer.md#fetch) | **GET** /transfer/{code} | Fetch Transfer
*Transfer* | [**finalize**](docs/Transfer.md#finalize) | **POST** /transfer/finalize_transfer | Finalize Transfer
*Transfer* | [**initiate**](docs/Transfer.md#initiate) | **POST** /transfer | Initiate Transfer
*Transfer* | [**list**](docs/Transfer.md#list) | **GET** /transfer | List Transfers
*Transfer* | [**resend_otp**](docs/Transfer.md#resend_otp) | **POST** /transfer/resend_otp | Resend OTP for Transfer
*Transfer* | [**verify**](docs/Transfer.md#verify) | **GET** /transfer/verify/{reference} | Verify Transfer
*TransferRecipient* | [**bulk**](docs/TransferRecipient.md#bulk) | **POST** /transferrecipient/bulk | Bulk Create Transfer Recipient
*TransferRecipient* | [**create**](docs/TransferRecipient.md#create) | **POST** /transferrecipient | Create Transfer Recipient
*TransferRecipient* | [**fetch**](docs/TransferRecipient.md#fetch) | **GET** /transferrecipient/{code} | Fetch Transfer recipient
*TransferRecipient* | [**list**](docs/TransferRecipient.md#list) | **GET** /transferrecipient | List Transfer Recipients
*TransferRecipient* | [**transferrecipient_code_delete**](docs/TransferRecipient.md#transferrecipient_code_delete) | **DELETE** /transferrecipient/{code} | Delete Transfer Recipient
*TransferRecipient* | [**transferrecipient_code_put**](docs/TransferRecipient.md#transferrecipient_code_put) | **PUT** /transferrecipient/{code} | Update Transfer recipient
*Verification* | [**avs**](docs/Verification.md#avs) | **GET** /address_verification/states | List States (AVS)
*Verification* | [**fetch_banks**](docs/Verification.md#fetch_banks) | **GET** /bank | Fetch Banks
*Verification* | [**list_countries**](docs/Verification.md#list_countries) | **GET** /country | List Countries
*Verification* | [**resolve_account_number**](docs/Verification.md#resolve_account_number) | **GET** /bank/resolve | Resolve Account Number
*Verification* | [**resolve_card_bin**](docs/Verification.md#resolve_card_bin) | **GET** /decision/bin/{bin} | Resolve Card BIN


## Documentation For Models

 - [Accepted](docs/Accepted.md)
 - [Bank](docs/Bank.md)
 - [BulkChargeInitiate](docs/BulkChargeInitiate.md)
 - [ChargeCreate](docs/ChargeCreate.md)
 - [ChargeSubmitAddress](docs/ChargeSubmitAddress.md)
 - [ChargeSubmitBirthday](docs/ChargeSubmitBirthday.md)
 - [ChargeSubmitOTP](docs/ChargeSubmitOTP.md)
 - [ChargeSubmitPhone](docs/ChargeSubmitPhone.md)
 - [ChargeSubmitPin](docs/ChargeSubmitPin.md)
 - [CustomerCreate](docs/CustomerCreate.md)
 - [CustomerDeactivateAuthorization](docs/CustomerDeactivateAuthorization.md)
 - [CustomerRiskAction](docs/CustomerRiskAction.md)
 - [CustomerUpdate](docs/CustomerUpdate.md)
 - [CustomerValidate](docs/CustomerValidate.md)
 - [CustomerValidation](docs/CustomerValidation.md)
 - [DedicatedVirtualAccountCreate](docs/DedicatedVirtualAccountCreate.md)
 - [DedicatedVirtualAccountSplit](docs/DedicatedVirtualAccountSplit.md)
 - [DisputeEvidence](docs/DisputeEvidence.md)
 - [DisputeResolve](docs/DisputeResolve.md)
 - [DisputeUpdate](docs/DisputeUpdate.md)
 - [EFT](docs/EFT.md)
 - [Error](docs/Error.md)
 - [MobileMoney](docs/MobileMoney.md)
 - [PageCreate](docs/PageCreate.md)
 - [PageProduct](docs/PageProduct.md)
 - [PageUpdate](docs/PageUpdate.md)
 - [PaymentRequestCreate](docs/PaymentRequestCreate.md)
 - [PaymentRequestUpdate](docs/PaymentRequestUpdate.md)
 - [PlanCreate](docs/PlanCreate.md)
 - [PlanUpdate](docs/PlanUpdate.md)
 - [ProductCreate](docs/ProductCreate.md)
 - [ProductUpdate](docs/ProductUpdate.md)
 - [RefundCreate](docs/RefundCreate.md)
 - [Response](docs/Response.md)
 - [SplitCreate](docs/SplitCreate.md)
 - [SplitSubaccounts](docs/SplitSubaccounts.md)
 - [SplitUpdate](docs/SplitUpdate.md)
 - [SubaccountCreate](docs/SubaccountCreate.md)
 - [SubaccountUpdate](docs/SubaccountUpdate.md)
 - [SubscriptionCreate](docs/SubscriptionCreate.md)
 - [SubscriptionToggle](docs/SubscriptionToggle.md)
 - [TransactionChargeAuthorization](docs/TransactionChargeAuthorization.md)
 - [TransactionCheckAuthorization](docs/TransactionCheckAuthorization.md)
 - [TransactionInitialize](docs/TransactionInitialize.md)
 - [TransactionPartialDebit](docs/TransactionPartialDebit.md)
 - [TransferBulk](docs/TransferBulk.md)
 - [TransferFinalize](docs/TransferFinalize.md)
 - [TransferFinalizeDisableOTP](docs/TransferFinalizeDisableOTP.md)
 - [TransferInitiate](docs/TransferInitiate.md)
 - [TransferRecipientBulk](docs/TransferRecipientBulk.md)
 - [TransferRecipientCreate](docs/TransferRecipientCreate.md)
 - [TransferRecipientUpdate](docs/TransferRecipientUpdate.md)
 - [TransferResendOTP](docs/TransferResendOTP.md)
 - [USSD](docs/USSD.md)
 - [VerificationBVNMatch](docs/VerificationBVNMatch.md)



## Issues
Kindly [open an issue](https://github.com/PaystackOSS/paystack-python/issues) if you discover any bug or have problems using this library. 

## License
This repository is made available under the MIT license. Kindly read the [LICENSE](https://github.com/PaystackOSS/paystack-python/blob/main/LICENSE) file for more information.
