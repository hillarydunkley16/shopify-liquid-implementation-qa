---
title: 'Liquid filters: color_lighten'
description: >-
  Lightens a given color by a specific percentage. The percentage must be
  between 0 and 100.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/color_lighten'
  md: 'https://shopify.dev/docs/api/liquid/filters/color_lighten.md'
api_name: liquid
---

# color\_​lighten

```oobleck
string | color_lighten: number
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Lightens a given color by a specific percentage. The percentage must be between 0 and 100.

##### Code

```liquid
{{ '#EA5AB9' | color_lighten: 30 }}
```

##### Output

```html
#fbe2f3
```
