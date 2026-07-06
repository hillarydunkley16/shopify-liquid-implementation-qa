---
title: 'Liquid filters: money_with_currency'
description: >-
  Formats a given price based on the store's [**HTML with currency**
  setting](https://help.shopify.com/manual/payments/currency-formatting).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/money_with_currency'
  md: 'https://shopify.dev/docs/api/liquid/filters/money_with_currency.md'
api_name: liquid
---

# money\_​with\_​currency

```oobleck
number | money_with_currency
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Formats a given price based on the store's [**HTML with currency** setting](https://help.shopify.com/manual/payments/currency-formatting).

##### Code

```liquid
{{ product.price | money_with_currency }}
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
$10.00 CAD
```
