---
title: 'Liquid filters: money_without_trailing_zeros'
description: >-
  Formats a given price based on the store's [**HTML without currency**
  setting](https://help.shopify.com/manual/payments/currency-formatting),
  excluding the decimal separator

  (either `.` or `,`) and trailing zeros.


  If the price has a non-zero decimal value, then the output is the same as the
  [`money` filter](/docs/api/liquid/filters#money).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/money_without_trailing_zeros'
  md: 'https://shopify.dev/docs/api/liquid/filters/money_without_trailing_zeros.md'
api_name: liquid
---

# money\_​without\_​trailing\_​zeros

```oobleck
number | money_without_trailing_zeros
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Formats a given price based on the store's [**HTML without currency** setting](https://help.shopify.com/manual/payments/currency-formatting), excluding the decimal separator (either `.` or `,`) and trailing zeros.

If the price has a non-zero decimal value, then the output is the same as the [`money` filter](https://shopify.dev/docs/api/liquid/filters#money).

##### Code

```liquid
{{ product.price | money_without_trailing_zeros }}
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
$10
```
