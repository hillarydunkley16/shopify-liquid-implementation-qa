---
title: 'Liquid filters: money_without_currency'
description: >-
  Formats a given price based on the store's [**HTML without currency**
  setting](https://help.shopify.com/manual/payments/currency-formatting),
  without the currency symbol.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/money_without_currency'
  md: 'https://shopify.dev/docs/api/liquid/filters/money_without_currency.md'
api_name: liquid
---

# money\_​without\_​currency

```oobleck
number | money_without_currency
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Formats a given price based on the store's [**HTML without currency** setting](https://help.shopify.com/manual/payments/currency-formatting), without the currency symbol.

##### Code

```liquid
{{ product.price | money_without_currency }}
```

##### Data

```json
{
  "product": {
    "price": "10.00"
  }
}
```

##### Output

```html
10.00
```
