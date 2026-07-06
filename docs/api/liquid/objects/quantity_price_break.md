---
title: 'Liquid objects: quantity_price_break'
description: The per-unit price of a variant when purchasing the minimum quantity or more.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/quantity_price_break'
  md: 'https://shopify.dev/docs/api/liquid/objects/quantity_price_break.md'
api_name: liquid
---

# quantity\_​price\_​break

The per-unit price of a variant when purchasing the minimum quantity or more.

## Properties

* * **minimum\_​quantity**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The minimum quantity required to qualify for the price break.

  * **price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The price for the quantity price break once the minimum quantity is met.

    The value is the price in the customer's local (presentment) currency.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

##### Example

```json
{
  "minimum_quantity": "10",
  "price": "20.00"
}
```
