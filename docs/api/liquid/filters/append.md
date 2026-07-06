---
title: 'Liquid filters: append'
description: Adds a given string to the end of a string.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/append'
  md: 'https://shopify.dev/docs/api/liquid/filters/append.md'
api_name: liquid
---

# append

```oobleck
string | append: string
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Adds a given string to the end of a string.

##### Code

```liquid
{%-  assign path = product.url -%}

{{ request.origin | append: path }}
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
