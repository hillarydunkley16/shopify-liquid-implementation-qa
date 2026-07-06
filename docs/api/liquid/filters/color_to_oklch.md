---
title: 'Liquid filters: color_to_oklch'
description: Converts a CSS color string to `OKLCH` format.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/color_to_oklch'
  md: 'https://shopify.dev/docs/api/liquid/filters/color_to_oklch.md'
api_name: liquid
---

# color\_​to\_​oklch

```oobleck
string | color_to_oklch
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Converts a CSS color string to `OKLCH` format.

##### Code

```liquid
{{ '#EA5AB9' | color_to_oklch }}
```

##### Output

```html
oklch(68% 0.2 343 / 1.0)
```
