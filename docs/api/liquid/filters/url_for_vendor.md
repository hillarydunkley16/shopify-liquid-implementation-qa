---
title: 'Liquid filters: url_for_vendor'
description: >-
  Generates a URL for a [collection
  page](https://shopify.dev/docs/storefronts/themes/architecture/templates/collection)
  that lists all products from the given product vendor.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/url_for_vendor'
  md: 'https://shopify.dev/docs/api/liquid/filters/url_for_vendor.md'
api_name: liquid
---

# url\_​for\_​vendor

```oobleck
string | url_for_vendor
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates a URL for a [collection page](https://shopify.dev/docs/storefronts/themes/architecture/templates/collection) that lists all products from the given product vendor.

##### Code

```liquid
{{ "Polina's Potent Potions" | url_for_vendor }}
```

##### Output

```html
/collections/vendors?q=Polina%27s%20Potent%20Potions
```
