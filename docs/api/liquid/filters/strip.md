---
title: 'Liquid filters: strip'
description: Strips all whitespace from the left and right of a string.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/strip'
  md: 'https://shopify.dev/docs/api/liquid/filters/strip.md'
api_name: liquid
---

# strip

```oobleck
string | strip
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Strips all whitespace from the left and right of a string.

##### Code

```liquid
{%- assign text = '  Some potions create whitespace.      ' -%}

"{{ text }}"
"{{ text | strip }}"
```

##### Output

```html
"  Some potions create whitespace.      "
"Some potions create whitespace."
```
