---
title: 'Liquid filters: sha1'
description: >-
  Converts a string into an SHA-1 hash. SHA-1 is not considered safe anymore.
  Please use ['blake3'](https://shopify.dev/docs/api/liquid/filters/blake3)
  instead for better security and performance.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/sha1'
  md: 'https://shopify.dev/docs/api/liquid/filters/sha1.md'
api_name: liquid
---

# sha1

```oobleck
string | sha1: string
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Converts a string into an SHA-1 hash. SHA-1 is not considered safe anymore. Please use ['blake3'](https://shopify.dev/docs/api/liquid/filters/blake3) instead for better security and performance.

##### Code

```liquid
{%- assign secret_potion = 'Polyjuice' | sha1 -%}

My secret potion: {{ secret_potion }}
```

##### Output

```html
My secret potion: bd0ca3935467e5238d7662ada4df899f09b70d5a
```
