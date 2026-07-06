---
title: 'Liquid filters: escape'
description: >-
  Escapes special characters in HTML, such as `<>`, `'`, and `&`, and converts
  characters into escape sequences. The filter doesn't effect characters within
  the string that don’t have a corresponding escape sequence.".
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/escape'
  md: 'https://shopify.dev/docs/api/liquid/filters/escape.md'
api_name: liquid
---

# escape

```oobleck
string | escape
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Escapes special characters in HTML, such as `<>`, `'`, and `&`, and converts characters into escape sequences. The filter doesn't effect characters within the string that don’t have a corresponding escape sequence.".

##### Code

```liquid
{{ '<p>Text to be escaped.</p>' | escape }}
```

##### Output

```html
&lt;p&gt;Text to be escaped.&lt;/p&gt;
```
