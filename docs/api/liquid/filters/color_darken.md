---
title: 'Liquid filters: color_darken'
description: >-
  Darkens a given color by a specific percentage. The percentage must be between
  0 and 100.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/color_darken'
  md: 'https://shopify.dev/docs/api/liquid/filters/color_darken.md'
api_name: liquid
---

# color\_​darken

```oobleck
string | color_darken: number
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Darkens a given color by a specific percentage. The percentage must be between 0 and 100.

##### Code

```liquid
{{ '#EA5AB9' | color_darken: 30 }}
```

##### Output

```html
#98136b
```
