---
title: 'Liquid filters: base64_url_safe_decode'
description: >-
  Decodes a string in URL-safe [Base64
  format](https://developer.mozilla.org/en-US/docs/Glossary/Base64).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/base64_url_safe_decode'
  md: 'https://shopify.dev/docs/api/liquid/filters/base64_url_safe_decode.md'
api_name: liquid
---

# base64\_​url\_​safe\_​decode

```oobleck
string | base64_url_safe_decode
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Decodes a string in URL-safe [Base64 format](https://developer.mozilla.org/en-US/docs/Glossary/Base64).

##### Code

```liquid
{{ 'b25lIHR3byB0aHJlZQ==' | base64_url_safe_decode }}
```

##### Output

```html
one two three
```
