---
title: 'Liquid filters: color_mix'
description: >-
  Blends two colors together by a specific percentage factor. The percentage
  must be between 0 and 100.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/color_mix'
  md: 'https://shopify.dev/docs/api/liquid/filters/color_mix.md'
api_name: liquid
---

# color\_​mix

```oobleck
string | color_mix: string, number
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Blends two colors together by a specific percentage factor. The percentage must be between 0 and 100.

***

**Tip:** A percentage factor of 100 returns the color being filtered. A percentage factor of 0 returns the color supplied to the filter.

***

##### Code

```liquid
{{ '#E800B0' | color_mix: '#00936F', 50 }}
```

##### Output

```html
#744a90
```

If one input has an alpha component, but the other does not, an alpha component of 1.0 will be assumed for the input without an alpha component.

##### Code

```liquid
{{ 'rgba(232, 0, 176, 0.75)' | color_mix: '#00936F', 50 }}
```

##### Output

```html
rgba(116, 74, 144, 0.88)
```
