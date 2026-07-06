---
title: 'Liquid filters: base64_decode'
description: >-
  Decodes a string in [Base64
  format](https://developer.mozilla.org/en-US/docs/Glossary/Base64).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/base64_decode'
  md: 'https://shopify.dev/docs/api/liquid/filters/base64_decode.md'
api_name: liquid
---

# base64\_​decode

```oobleck
string | base64_decode
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Decodes a string in [Base64 format](https://developer.mozilla.org/en-US/docs/Glossary/Base64).

##### Code

```liquid
{{ 'b25lIHR3byB0aHJlZQ==' | base64_decode }}
```

##### Output

```html
one two three
```
