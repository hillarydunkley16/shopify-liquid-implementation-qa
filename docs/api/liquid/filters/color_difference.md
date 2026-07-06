---
title: 'Liquid filters: color_difference'
description: >-
  Calculates the [color
  difference](https://www.w3.org/WAI/ER/WD-AERT/#color-contrast) between two
  colors.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/color_difference'
  md: 'https://shopify.dev/docs/api/liquid/filters/color_difference.md'
api_name: liquid
---

# color\_​difference

```oobleck
string | color_difference: string
```

returns [number](https://shopify.dev/docs/api/liquid/basics#number)

Calculates the [color difference](https://www.w3.org/WAI/ER/WD-AERT/#color-contrast) between two colors.

***

**Tip:** For accessibility best practices, it\&#39;s recommended to have a minimum color difference of 500.

***

##### Code

```liquid
{{ '#720955' | color_difference: '#FFF3F9' }}
```

##### Output

```html
539
```
