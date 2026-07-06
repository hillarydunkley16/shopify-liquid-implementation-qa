---
title: 'Liquid filters: shopify_asset_url'
description: >-
  Returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn)
  for a globally accessible Shopify asset.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/shopify_asset_url'
  md: 'https://shopify.dev/docs/api/liquid/filters/shopify_asset_url.md'
api_name: liquid
---

# shopify\_​asset\_​url

```oobleck
string | shopify_asset_url
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Returns the [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) for a globally accessible Shopify asset.

The following are the globally accessible Shopify assets:

* `option_selection.js`
* `api.jquery.js`
* `shopify_common.js`
* `customer_area.js`
* `currencies.js`
* `customer.css`

##### Code

```liquid
{{ 'option_selection.js' | shopify_asset_url }}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/themes_support/option_selection-b017cd28.js
```
