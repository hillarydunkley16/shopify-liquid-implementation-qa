---
title: 'Liquid filters: inline_asset_content'
description: >-
  Outputs the content of an asset inline in the template. The asset must be
  either a SVG, JS, or CSS file.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/inline_asset_content'
  md: 'https://shopify.dev/docs/api/liquid/filters/inline_asset_content.md'
api_name: liquid
---

# inline\_​asset\_​content

```oobleck
asset_name | inline_asset_content
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Outputs the content of an asset inline in the template. The asset must be either a SVG, JS, or CSS file.

***

**Note:** The asset size must be less than 15KB to be inlined.

***

##### Code

```liquid
{{ 'icon.svg' | inline_asset_content }}
```

##### Output

```html
'<svg xmlns="http://www.w3.org/2000/svg"/>'
```
