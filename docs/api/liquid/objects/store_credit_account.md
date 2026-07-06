---
title: 'Liquid objects: store_credit_account'
description: >-
  A [store credit
  account](https://help.shopify.com/en/manual/customers/store-credit) owned by a
  [customer](/docs/api/liquid/objects/customer).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/store_credit_account'
  md: 'https://shopify.dev/docs/api/liquid/objects/store_credit_account.md'
api_name: liquid
---

# store\_​credit\_​account

A [store credit account](https://help.shopify.com/en/manual/customers/store-credit) owned by a [customer](https://shopify.dev/docs/api/liquid/objects/customer).

## Properties

* * **balance**

    [money](https://shopify.dev/docs/api/liquid/objects/money)

  * The balance of the store credit account in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

##### Example

```json
{
  "balance": {}
}
```
