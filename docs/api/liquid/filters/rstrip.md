---
title: 'Liquid filters: rstrip'
description: Strips all whitespace from the right of a string.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/rstrip'
  md: 'https://shopify.dev/docs/api/liquid/filters/rstrip.md'
api_name: liquid
---

# rstrip

```oobleck
string | rstrip
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Strips all whitespace from the right of a string.

##### Code

```liquid
{%- assign text = '  Some potions create whitespace.      ' -%}

"{{ text }}"
"{{ text | rstrip }}"
```

##### Output

```html
"  Some potions create whitespace.      "
"  Some potions create whitespace."
```
