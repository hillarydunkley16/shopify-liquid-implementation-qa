---
title: 'Liquid filters: color_saturate'
description: >-
  Saturates a given color by a specific percentage. The percentage must be
  between 0 and 100.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/color_saturate'
  md: 'https://shopify.dev/docs/api/liquid/filters/color_saturate.md'
api_name: liquid
---

# color\_​saturate

```oobleck
string | color_saturate: number
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Saturates a given color by a specific percentage. The percentage must be between 0 and 100.

##### Code

```liquid
{{ '#EA5AB9' | color_saturate: 30 }}
```

##### Output

```html
#ff45c0
```
