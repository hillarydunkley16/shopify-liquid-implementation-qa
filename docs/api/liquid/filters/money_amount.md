---
title: 'Liquid filters: money_amount'
description: >-
  Formats a given price as a plain decimal string, without currency symbols,
  thousand separators, or locale formatting.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/money_amount'
  md: 'https://shopify.dev/docs/api/liquid/filters/money_amount.md'
api_name: liquid
---

# money\_​amount

```oobleck
number | money_amount
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Formats a given price as a plain decimal string, without currency symbols, thousand separators, or locale formatting.

##### Code

```liquid
{{ product.price | money_amount }}
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
10.0
```
