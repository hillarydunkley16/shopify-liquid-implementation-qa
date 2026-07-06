---
title: 'Liquid filters: color_modify'
description: Modifies a specific color component of a given color by a specific amount.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/color_modify'
  md: 'https://shopify.dev/docs/api/liquid/filters/color_modify.md'
api_name: liquid
---

# color\_​modify

```oobleck
string | color_modify: string, number
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Modifies a specific color component of a given color by a specific amount.

The following table outlines valid color components, and the value range for their modifications:

| Component | Value range |
| - | - |
| * `red`
* `green`
* `blue` | An integer between 0 and 255 |
| `alpha` | A decimal between 0 and 1 |
| `hue` | An integer between 0 and 360 |
| - `saturation`
- `lightness` | An integer between 0 and 100 |

##### Code

```liquid
{{ '#EA5AB9' | color_modify: 'red', 255 }}
```

##### Output

```html
#ff5ab9
```

The format of the modified color depends on the component being modified. For example, if you modify the `alpha` component of a color in hexadecimal format, then the modified color will be in `rgba()` format.

##### Code

```liquid
{{ '#EA5AB9' | color_modify: 'alpha', 0.85 }}
```

##### Output

```html
rgba(234, 90, 185, 0.85)
```
