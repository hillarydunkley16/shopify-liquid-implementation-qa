---
title: 'Liquid objects: pending_payment_instruction_input'
description: >-
  Header-value pairs that make up the list of payment information specific to
  the payment method.

  This information can be be used by the customer to complete the transaction
  offline.
source_url:
  html: >-
    https://shopify.dev/docs/api/liquid/objects/pending_payment_instruction_input
  md: >-
    https://shopify.dev/docs/api/liquid/objects/pending_payment_instruction_input.md
api_name: liquid
---

# pending\_​payment\_​instruction\_​input

Header-value pairs that make up the list of payment information specific to the payment method. This information can be be used by the customer to complete the transaction offline.

## Properties

* * **header**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The header of the payment instruction. These are payment method-specific. Example: "Entity" and "Reference" for Multibanco

  * **value**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * Contains the corresponding values to the headers of the payment instruction.

### Returned by

* [transaction.buyer\_​pending\_​payment\_​instructions](https://shopify.dev/docs/api/liquid/objects/transaction#transaction-buyer_pending_payment_instructions)
