---
title: 'Liquid filters: color_to_hsl'
description: Converts a CSS color string to `HSL` format.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/color_to_hsl'
  md: 'https://shopify.dev/docs/api/liquid/filters/color_to_hsl.md'
api_name: liquid
---

# color\_​to\_​hsl

```oobleck
string | color_to_hsl
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Converts a CSS color string to `HSL` format.

If a color with an alpha component is provided, the color is converted to `HSLA` format.

##### Code

```liquid
{{ '#EA5AB9' | color_to_hsl }}
```

##### Output

```html
hsl(320, 77%, 64%)
```
