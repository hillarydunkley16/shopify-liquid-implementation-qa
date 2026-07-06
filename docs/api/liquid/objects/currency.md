---
title: 'Liquid objects: currency'
description: 'Information about a currency, like the ISO code and symbol.'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/currency'
  md: 'https://shopify.dev/docs/api/liquid/objects/currency.md'
api_name: liquid
---

# currency

Information about a currency, like the ISO code and symbol.

## Properties

* * **iso\_​code**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The [ISO code](https://www.iso.org/iso-4217-currency-codes.html) of the currency.

  * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the currency.

  * **symbol**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The symbol of the currency.

##### Example

```json
{
  "iso_code": "CAD",
  "name": "Canadian Dollar",
  "symbol": "$"
}
```
