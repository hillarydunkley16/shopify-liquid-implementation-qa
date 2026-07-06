---
title: 'Liquid objects: powered_by_link'
description: >-
  Creates an HTML link element that links to a localized version of
  `shopify.com`, based on the locale of the store.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/powered_by_link'
  md: 'https://shopify.dev/docs/api/liquid/objects/powered_by_link.md'
api_name: liquid
---

# powered\_​by\_​link

Creates an HTML link element that links to a localized version of `shopify.com`, based on the locale of the store.

### Directly accessible in

* Global

##### Code

```liquid
{{ powered_by_link }}
```

##### Output

```html
<a target="_blank" rel="nofollow" href="https://www.shopify.com?utm_campaign=poweredby&amp;utm_medium=shopify&amp;utm_source=onlinestore">Powered by Shopify</a>
```
