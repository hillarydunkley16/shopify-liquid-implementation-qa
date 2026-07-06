---
title: 'Liquid filters: script_tag'
description: >-
  Generates an HTML `<script>` tag for a given resource URL. The tag has a
  `type` attribute of `text/javascript`.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/script_tag'
  md: 'https://shopify.dev/docs/api/liquid/filters/script_tag.md'
api_name: liquid
---

# script\_​tag

```oobleck
string | script_tag
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates an HTML `<script>` tag for a given resource URL. The tag has a `type` attribute of `text/javascript`.

##### Code

```liquid
{{ 'cart.js' | asset_url | script_tag }}
```

##### Output

```html
<script src="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/cart.js?v=83971781268232213281663872410" type="text/javascript"></script>
```
