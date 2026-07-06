---
title: 'Liquid objects: customer_payment_method'
description: A customer's saved payment method.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/customer_payment_method'
  md: 'https://shopify.dev/docs/api/liquid/objects/customer_payment_method.md'
api_name: liquid
---

# customer\_​payment\_​method

A customer's saved payment method.

A payment method that a customer has saved to their account for reuse (e.g. a credit card).

## Properties

* * **payment\_​instrument\_​type**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The instrument type of the payment method (e.g credit\_card).

  * **token**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The identifier for the payment method.

### Returned by

* [customer.payment\_​methods](https://shopify.dev/docs/api/liquid/objects/customer#customer-payment_methods)
