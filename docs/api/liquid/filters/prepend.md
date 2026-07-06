---
title: 'Liquid filters: prepend'
description: Adds a given string to the beginning of a string.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/prepend'
  md: 'https://shopify.dev/docs/api/liquid/filters/prepend.md'
api_name: liquid
---

# prepend

```oobleck
string | prepend: string
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Adds a given string to the beginning of a string.

##### Code

```liquid
{%- assign origin = request.origin -%}

{{ product.url | prepend: origin }}
```

##### Data

```json
{
  "product": {
    "url": "/products/health-potion"
  },
  "request": {
    "origin": "https://polinas-potent-potions.myshopify.com"
  }
}
```

##### Output

```html
https://polinas-potent-potions.myshopify.com/products/health-potion
```
