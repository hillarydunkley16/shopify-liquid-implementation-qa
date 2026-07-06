---
title: 'Liquid filters: color_to_hex'
description: Converts a CSS color string to hexadecimal format (`hex6`).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/color_to_hex'
  md: 'https://shopify.dev/docs/api/liquid/filters/color_to_hex.md'
api_name: liquid
---

# color\_​to\_​hex

```oobleck
string | color_to_hex
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Converts a CSS color string to hexadecimal format (`hex6`).

Because colors are converted to `hex6` format, if a color with an alpha component is provided, then the alpha component is excluded from the output.

##### Code

```liquid
{{ 'rgb(234, 90, 185)' | color_to_hex }}
```

##### Output

```html
#ea5ab9
```
