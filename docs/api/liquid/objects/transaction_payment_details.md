---
title: 'Liquid objects: transaction_payment_details'
description: Information about the payment methods used for a transaction.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/transaction_payment_details'
  md: 'https://shopify.dev/docs/api/liquid/objects/transaction_payment_details.md'
api_name: liquid
---

# transaction\_​payment\_​details

Information about the payment methods used for a transaction.

## Properties

* * **credit\_​card\_​company**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the company that issued the credit card used for the transaction.

  * **credit\_​card\_​last\_​four\_​digits**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The last four digits of the credit card number of the credit card used for the transaction.

  * **credit\_​card\_​number**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The credit card number of the credit card used for the transaction.

    All but the last four digits are redacted.

  * **gift\_​card**

    [gift\_card](https://shopify.dev/docs/api/liquid/objects/gift_card)

  * The gift card used for the transaction.

    If no gift card was used, then `nil` is returned.

##### Example

```json
{
  "credit_card_number": "•••• •••• •••• 4242",
  "credit_card_company": "Visa",
  "credit_card_last_four_digits": "4242"
}
```
