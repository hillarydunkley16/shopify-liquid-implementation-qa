---
title: 'Liquid filters: hmac_sha256'
description: >-
  Converts a string into an SHA-256 hash using a hash message authentication
  code (HMAC).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/hmac_sha256'
  md: 'https://shopify.dev/docs/api/liquid/filters/hmac_sha256.md'
api_name: liquid
---

# hmac\_​sha256

```oobleck
string | hmac_sha256: string
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Converts a string into an SHA-256 hash using a hash message authentication code (HMAC).

The secret key for the message is supplied as a parameter to the filter.

##### Code

```liquid
{%- assign secret_potion = 'Polyjuice' | hmac_sha256: 'Polina' -%}

My secret potion: {{ secret_potion }}
```

##### Output

```html
My secret potion: 8e0d5d65cff1242a4af66c8f4a32854fd5fb80edcc8aabe9b302b29c7c71dc20
```
