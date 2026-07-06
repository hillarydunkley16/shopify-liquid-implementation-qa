---
title: 'Liquid objects: tax_line'
description: Information about a tax line of a checkout or order.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/tax_line'
  md: 'https://shopify.dev/docs/api/liquid/objects/tax_line.md'
api_name: liquid
---

# tax\_​line

Information about a tax line of a checkout or order.

## Properties

* * **price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The tax amount in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

  * **rate**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The decimal value of the tax rate.

  * **rate\_​percentage**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The decimal value of the tax rate, as a percentage.

  * **title**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The title of the tax.

##### Example

```json
{
  "price": 1901,
  "rate": 0.05,
  "rate_percentage": 5,
  "title": "GST"
}
```
