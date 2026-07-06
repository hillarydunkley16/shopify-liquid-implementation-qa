---
title: 'Liquid filters: asset_img_url'
description: >-
  Returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn)
  for an image in the

  [`assets` directory](/themes/architecture#assets) of a theme.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/asset_img_url'
  md: 'https://shopify.dev/docs/api/liquid/filters/asset_img_url.md'
api_name: liquid
---

# asset\_​img\_​url

```oobleck
string | asset_img_url
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Returns the [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) for an image in the [`assets` directory](https://shopify.dev/themes/architecture#assets) of a theme.

##### Code

```liquid
{{ 'red-and-black-bramble-berries.jpg' | asset_img_url }}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/red-and-black-bramble-berries_small.jpg?v=337
```

### size

```oobleck
image | asset_img_url: string
```

By default, the `asset_img_url` filter returns the `small` version of the image (100 x 100 px). However, you can specify a [size](https://shopify.dev/docs/api/liquid/filters/img_url#img_url-size).

##### Code

```liquid
{{ 'red-and-black-bramble-berries.jpg' | asset_img_url: 'large' }}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/red-and-black-bramble-berries_large.jpg?v=337
```
