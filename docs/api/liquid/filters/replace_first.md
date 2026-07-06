---
title: 'Liquid filters: replace_first'
description: >-
  Replaces the first instance of a substring inside a string with a given
  string.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/replace_first'
  md: 'https://shopify.dev/docs/api/liquid/filters/replace_first.md'
api_name: liquid
---

# replace\_​first

```oobleck
string | replace_first: string, string
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Replaces the first instance of a substring inside a string with a given string.

##### Code

```liquid
{{ product.handle | replace_first: '-', ' ' }}
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
komodo dragon-scale
```
