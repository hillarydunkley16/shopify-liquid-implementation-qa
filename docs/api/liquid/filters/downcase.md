---
title: 'Liquid filters: downcase'
description: Converts a string to all lowercase characters.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/downcase'
  md: 'https://shopify.dev/docs/api/liquid/filters/downcase.md'
api_name: liquid
---

# downcase

```oobleck
string | downcase
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Converts a string to all lowercase characters.

##### Code

```liquid
{{ product.title | downcase }}
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
health potion
```
