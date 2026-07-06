---
title: 'Liquid filters: font_url'
description: >-
  Returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn)
  for the provided font in `woff2` format.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/font_url'
  md: 'https://shopify.dev/docs/api/liquid/filters/font_url.md'
api_name: liquid
---

# font\_​url

```oobleck
font | font_url
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Returns the [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) for the provided font in `woff2` format.

##### Code

```liquid
{{ settings.type_header_font | font_url }}
```

##### Data

```json
{
  "settings": {
    "type_header_font": {}
  }
}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant_n4.9120912a469cad1cc292572851508ca49d12e768.woff2
```

### woff format

```oobleck
font | font_url: string
```

By default, the `font_url` filter returns the [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) for the font in `woff2` format. However, you can also choose `woff` format.

##### Code

```liquid
{{ settings.type_header_font | font_url: 'woff' }}
```

##### Data

```json
{
  "settings": {
    "type_header_font": {}
  }
}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant_n4.6e9875ce64e0fefcd3f4446b7ec9036b3ddd2985.woff
```
