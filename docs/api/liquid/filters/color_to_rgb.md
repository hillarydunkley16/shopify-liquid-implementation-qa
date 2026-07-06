---
title: 'Liquid filters: color_to_rgb'
description: Converts a CSS color string to `RGB` format.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/color_to_rgb'
  md: 'https://shopify.dev/docs/api/liquid/filters/color_to_rgb.md'
api_name: liquid
---

# color\_​to\_​rgb

```oobleck
string | color_to_rgb
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Converts a CSS color string to `RGB` format.

If a color with an alpha component is provided, then the color is converted to `RGBA` format.

##### Code

```liquid
{{ '#EA5AB9' | color_to_rgb }}
```

##### Output

```html
rgb(234, 90, 185)
```
