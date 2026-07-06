---
title: 'Liquid filters: url_decode'
description: >-
  Decodes any
  [percent-encoded](https://developer.mozilla.org/en-US/docs/Glossary/percent-encoding)
  characters

  in a string.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/url_decode'
  md: 'https://shopify.dev/docs/api/liquid/filters/url_decode.md'
api_name: liquid
---

# url\_​decode

```oobleck
string | url_decode
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Decodes any [percent-encoded](https://developer.mozilla.org/en-US/docs/Glossary/percent-encoding) characters in a string.

##### Code

```liquid
{{ 'test%40test.com' | url_decode }}
```

##### Output

```html
test@test.com
```
