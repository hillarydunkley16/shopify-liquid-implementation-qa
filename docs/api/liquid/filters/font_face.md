---
title: 'Liquid filters: font_face'
description: >-
  Generates a CSS [`@font_face`
  declaration](https://developer.mozilla.org/en-US/docs/Web/CSS/%40font-face) to
  load the provided font.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/font_face'
  md: 'https://shopify.dev/docs/api/liquid/filters/font_face.md'
api_name: liquid
---

# font\_​face

```oobleck
font | font_face
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates a CSS [`@font_face` declaration](https://developer.mozilla.org/en-US/docs/Web/CSS/%40font-face) to load the provided font.

##### Code

```liquid
{{ settings.type_header_font | font_face }}
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
@font-face {
  font-family: Assistant;
  font-weight: 400;
  font-style: normal;
  src: url("//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant_n4.9120912a469cad1cc292572851508ca49d12e768.woff2") format("woff2"),
       url("//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant_n4.6e9875ce64e0fefcd3f4446b7ec9036b3ddd2985.woff") format("woff");
}
```

### font\_display

```oobleck
font | font_face: font_display: string
```

You can include an optional parameter to specify the [`font_display` property](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display) of the `@font_face` declaration.

##### Code

```liquid
{{ settings.type_header_font | font_face: font_display: 'swap' }}
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
@font-face {
  font-family: Assistant;
  font-weight: 400;
  font-style: normal;
  font-display: swap;
  src: url("//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant_n4.9120912a469cad1cc292572851508ca49d12e768.woff2") format("woff2"),
       url("//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant_n4.6e9875ce64e0fefcd3f4446b7ec9036b3ddd2985.woff") format("woff");
}
```
