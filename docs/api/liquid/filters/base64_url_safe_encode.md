---
title: 'Liquid filters: base64_url_safe_encode'
description: >-
  Encodes a string to URL-safe [Base64
  format](https://developer.mozilla.org/en-US/docs/Glossary/Base64).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/base64_url_safe_encode'
  md: 'https://shopify.dev/docs/api/liquid/filters/base64_url_safe_encode.md'
api_name: liquid
---

# base64\_​url\_​safe\_​encode

```oobleck
string | base64_url_safe_encode
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Encodes a string to URL-safe [Base64 format](https://developer.mozilla.org/en-US/docs/Glossary/Base64).

To produce URL-safe Base64, this filter uses `-` and `_` in place of `+` and `/`.

##### Code

```liquid
{{ 'one two three' | base64_url_safe_encode }}
```

##### Output

```html
b25lIHR3byB0aHJlZQ==
```
