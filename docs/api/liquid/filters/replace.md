---
title: 'Liquid filters: replace'
description: Replaces any instance of a substring inside a string with a given string.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/replace'
  md: 'https://shopify.dev/docs/api/liquid/filters/replace.md'
api_name: liquid
---

# replace

```oobleck
string | replace: string, string
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Replaces any instance of a substring inside a string with a given string.

##### Code

```liquid
{{ product.handle | replace: '-', ' ' }}
```

##### Data

```json
{
  "product": {
    "handle": "komodo-dragon-scale"
  }
}
```

##### Output

```html
komodo dragon scale
```
