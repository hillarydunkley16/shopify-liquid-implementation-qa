---
title: 'Liquid filters: lstrip'
description: Strips all whitespace from the left of a string.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/lstrip'
  md: 'https://shopify.dev/docs/api/liquid/filters/lstrip.md'
api_name: liquid
---

# lstrip

```oobleck
string | lstrip
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Strips all whitespace from the left of a string.

##### Code

```liquid
{%- assign text = '  Some potions create whitespace.      ' -%}

"{{ text }}"
"{{ text | lstrip }}"
```

##### Output

```html
"  Some potions create whitespace.      "
"Some potions create whitespace.      "
```
