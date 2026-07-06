---
title: 'Liquid filters: money'
description: >-
  Formats a given price based on the store's [**HTML without currency**
  setting](https://help.shopify.com/manual/payments/currency-formatting).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/money'
  md: 'https://shopify.dev/docs/api/liquid/filters/money.md'
api_name: liquid
---

# money

```oobleck
number | money
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Formats a given price based on the store's [**HTML without currency** setting](https://help.shopify.com/manual/payments/currency-formatting).

##### Code

```liquid
{{ product.price | money }}
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
$10.00
```
