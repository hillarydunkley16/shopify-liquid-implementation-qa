---
title: 'Liquid filters: asset_url'
description: >-
  Returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn)
  for a file in the

  [`assets` directory](/themes/architecture#assets) of a theme.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/asset_url'
  md: 'https://shopify.dev/docs/api/liquid/filters/asset_url.md'
api_name: liquid
---

# asset\_​url

```oobleck
string | asset_url
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Returns the [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) for a file in the [`assets` directory](https://shopify.dev/themes/architecture#assets) of a theme.

##### Code

```liquid
{{ 'cart.js' | asset_url }}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/cart.js?v=83971781268232213281663872410
```
