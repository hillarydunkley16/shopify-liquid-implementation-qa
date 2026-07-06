---
title: 'Liquid filters: md5'
description: >-
  Converts a string into an MD5 hash. MD5 is not considered safe anymore. Please
  use ['blake3'](https://shopify.dev/docs/api/liquid/filters/blake3) instead for
  better security and performance.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/md5'
  md: 'https://shopify.dev/docs/api/liquid/filters/md5.md'
api_name: liquid
---

# md5

```oobleck
string | md5
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Converts a string into an MD5 hash. MD5 is not considered safe anymore. Please use ['blake3'](https://shopify.dev/docs/api/liquid/filters/blake3) instead for better security and performance.

##### Code

```liquid
{{ '' | md5 }}
```

##### Output

```html
d41d8cd98f00b204e9800998ecf8427e
```
