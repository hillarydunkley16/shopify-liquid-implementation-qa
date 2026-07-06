---
title: 'Liquid filters: split'
description: Splits a string into an array of substrings based on a given separator.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/split'
  md: 'https://shopify.dev/docs/api/liquid/filters/split.md'
api_name: liquid
---

# split

```oobleck
string | split: string
```

returns array of [string](https://shopify.dev/docs/api/liquid/basics#string)

Splits a string into an array of substrings based on a given separator.

##### Code

```liquid
{%- assign title_words = product.handle | split: '-' -%}

{% for word in title_words -%}
  {{ word }}
{%- endfor %}
```

##### Data

```json
{
  "product": {
    "handle": "health-potion"
  }
}
```

##### Output

```html
health
potion
```
