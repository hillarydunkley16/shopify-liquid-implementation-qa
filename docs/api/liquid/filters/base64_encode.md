---
title: 'Liquid filters: base64_encode'
description: >-
  Encodes a string to [Base64
  format](https://developer.mozilla.org/en-US/docs/Glossary/Base64).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/base64_encode'
  md: 'https://shopify.dev/docs/api/liquid/filters/base64_encode.md'
api_name: liquid
---

# base64\_​encode

```oobleck
string | base64_encode
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Encodes a string to [Base64 format](https://developer.mozilla.org/en-US/docs/Glossary/Base64).

##### Code

```liquid
{{ 'one two three' | base64_encode }}
```

##### Output

```html
b25lIHR3byB0aHJlZQ==
```
