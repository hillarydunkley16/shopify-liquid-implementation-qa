---
title: 'Liquid filters: color_brightness'
description: >-
  Calculates the [perceived
  brightness](https://www.w3.org/WAI/ER/WD-AERT/#color-contrast) of a given
  color.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/color_brightness'
  md: 'https://shopify.dev/docs/api/liquid/filters/color_brightness.md'
api_name: liquid
---

# color\_​brightness

```oobleck
string | color_brightness
```

returns [number](https://shopify.dev/docs/api/liquid/basics#number)

Calculates the [perceived brightness](https://www.w3.org/WAI/ER/WD-AERT/#color-contrast) of a given color.

##### Code

```liquid
{{ '#EA5AB9' | color_brightness }}
```

##### Output

```html
143.89
```
