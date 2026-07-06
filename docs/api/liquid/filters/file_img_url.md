---
title: 'Liquid filters: file_img_url'
description: >-
  Returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn)
  for an image from the

  [Files](https://www.shopify.com/admin/settings/files) page of the Shopify
  admin.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/file_img_url'
  md: 'https://shopify.dev/docs/api/liquid/filters/file_img_url.md'
api_name: liquid
---

# file\_​img\_​url

```oobleck
string | file_img_url
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Returns the [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) for an image from the [Files](https://www.shopify.com/admin/settings/files) page of the Shopify admin.

##### Code

```liquid
{{ 'potions-header.png' | file_img_url }}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header_small.png?v=4246568442683817558
```

### The size parameter

```oobleck
image | file_img_url: string
```

By default, the `file_img_url` filter returns the `small` version of the image (100 x 100 px). However, you can specify a [size](https://shopify.dev/docs/api/liquid/filters/img_url#img_url-size).

##### Code

```liquid
{{ 'potions-header.png' | file_img_url: 'large' }}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header_large.png?v=4246568442683817558
```
