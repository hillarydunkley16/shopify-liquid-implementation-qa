---
title: 'Liquid filters: hex_to_rgba'
description: >-
  Converts a CSS color string from  hexadecimal format to `RGBA` format.
  Shorthand hexadecimal formatting (`hex3`) is also accepted.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/hex_to_rgba'
  md: 'https://shopify.dev/docs/api/liquid/filters/hex_to_rgba.md'
api_name: liquid
---

# hex\_​to\_​rgba

```oobleck
string | hex_to_rgba
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Converts a CSS color string from hexadecimal format to `RGBA` format. Shorthand hexadecimal formatting (`hex3`) is also accepted.

**Deprecated:**

The `hex_to_rgba` filter has been replaced by [`color_to_rgb`](https://shopify.dev/docs/api/liquid/filters/color_to_rgb) and [`color_modify`](https://shopify.dev/docs/api/liquid/filters/color_modify).

##### Code

```liquid
{{ '#EA5AB9' | hex_to_rgba }}
```

##### Output

```html
rgba(234,90,185,1)
```

### alpha

```oobleck
string | hex_to_rgba: number
```

The default `alpha` value is 1.0. However, you can specify a decimal value between 0.0 and 1.0.

##### Code

```liquid
{{ '#EA5AB9' | hex_to_rgba: 0.5 }}
```

##### Output

```html
rgba(234,90,185,0.5)
```
