---
title: 'Liquid filters: upcase'
description: Converts a string to all uppercase characters.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/upcase'
  md: 'https://shopify.dev/docs/api/liquid/filters/upcase.md'
api_name: liquid
---

# upcase

```oobleck
string | upcase
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Converts a string to all uppercase characters.

##### Code

```liquid
{{ product.title | upcase }}
```

##### Data

```json
{
  "product": {
    "title": "Health potion"
  }
}
```

##### Output

```html
HEALTH POTION
```
