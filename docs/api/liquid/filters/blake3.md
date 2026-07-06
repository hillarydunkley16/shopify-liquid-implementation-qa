---
title: 'Liquid filters: blake3'
description: Converts a string into a Blake3 hash.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/blake3'
  md: 'https://shopify.dev/docs/api/liquid/filters/blake3.md'
api_name: liquid
---

# blake3

```oobleck
string | blake3
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Converts a string into a Blake3 hash.

##### Code

```liquid
{{ '' | blake3 }}
```

##### Output

```html
af1349b9f5f9a1a6a0404dea36dcc9499bcb25c9adc112b7cc9a93cae41f3262
```
