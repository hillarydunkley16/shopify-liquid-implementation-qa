---
title: 'Liquid filters: color_extract'
description: Extracts a specific color component from a given color.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/color_extract'
  md: 'https://shopify.dev/docs/api/liquid/filters/color_extract.md'
api_name: liquid
---

# color\_​extract

```oobleck
string | color_extract: string
```

returns [number](https://shopify.dev/docs/api/liquid/basics#number)

Extracts a specific color component from a given color.

Accepts the following color components:

* `alpha`
* `red`
* `green`
* `blue`
* `hue`
* `saturation`
* `lightness`

##### Code

```liquid
{{ '#EA5AB9' | color_extract: 'red' }}
```

##### Output

```html
234
```
