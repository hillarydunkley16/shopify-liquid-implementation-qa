---
title: 'Liquid filters: color_desaturate'
description: >-
  Desaturates a given color by a specific percentage. The percentage must be
  between 0 and 100.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/color_desaturate'
  md: 'https://shopify.dev/docs/api/liquid/filters/color_desaturate.md'
api_name: liquid
---

# color\_​desaturate

```oobleck
string | color_desaturate: number
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Desaturates a given color by a specific percentage. The percentage must be between 0 and 100.

##### Code

```liquid
{{ '#EA5AB9' | color_desaturate: 30 }}
```

##### Output

```html
#ce76b0
```
