---
title: 'Liquid filters: url_for_type'
description: >-
  Generates a URL for a [collection
  page](https://shopify.dev/docs/storefronts/themes/architecture/templates/collection)
  that lists all products of the given product type.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/url_for_type'
  md: 'https://shopify.dev/docs/api/liquid/filters/url_for_type.md'
api_name: liquid
---

# url\_​for\_​type

```oobleck
string | url_for_type
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates a URL for a [collection page](https://shopify.dev/docs/storefronts/themes/architecture/templates/collection) that lists all products of the given product type.

##### Code

```liquid
{{ 'health' | url_for_type }}
```

##### Output

```html
/collections/types?q=health
```
