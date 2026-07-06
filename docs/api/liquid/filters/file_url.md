---
title: 'Liquid filters: file_url'
description: >-
  Returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn)
  for a file from the

  [Files](https://www.shopify.com/admin/settings/files) page of the Shopify
  admin.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/file_url'
  md: 'https://shopify.dev/docs/api/liquid/filters/file_url.md'
api_name: liquid
---

# file\_​url

```oobleck
string | file_url
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Returns the [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) for a file from the [Files](https://www.shopify.com/admin/settings/files) page of the Shopify admin.

##### Code

```liquid
{{ 'disclaimer.pdf' | file_url }}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/disclaimer.pdf?v=9043651738044769859
```
