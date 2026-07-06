---
title: 'Liquid filters: replace_last'
description: Replaces the last instance of a substring inside a string with a given string.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/replace_last'
  md: 'https://shopify.dev/docs/api/liquid/filters/replace_last.md'
api_name: liquid
---

# replace\_​last

```oobleck
string | replace_last: string, string
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Replaces the last instance of a substring inside a string with a given string.

##### Code

```liquid
{{ product.handle | replace_last: '-', ' ' }}
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
komodo-dragon scale
```
