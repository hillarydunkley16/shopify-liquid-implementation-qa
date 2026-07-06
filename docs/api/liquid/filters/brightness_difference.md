---
title: 'Liquid filters: brightness_difference'
description: >-
  Calculates the [perceived brightness
  difference](https://www.w3.org/WAI/ER/WD-AERT/#color-contrast) between two
  colors.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/brightness_difference'
  md: 'https://shopify.dev/docs/api/liquid/filters/brightness_difference.md'
api_name: liquid
---

# brightness\_​difference

```oobleck
string | brightness_difference: string
```

returns [number](https://shopify.dev/docs/api/liquid/basics#number)

Calculates the [perceived brightness difference](https://www.w3.org/WAI/ER/WD-AERT/#color-contrast) between two colors.

***

**Tip:** For accessibility best practices, it\&#39;s recommended to have a minimum brightness difference of 125.

***

##### Code

```liquid
{{ '#E800B0' | brightness_difference: '#FECEE9' }}
```

##### Output

```html
134
```
