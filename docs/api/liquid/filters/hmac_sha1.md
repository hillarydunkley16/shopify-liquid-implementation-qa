---
title: 'Liquid filters: hmac_sha1'
description: >-
  Converts a string into an SHA-1 hash using a hash message authentication code
  (HMAC).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/hmac_sha1'
  md: 'https://shopify.dev/docs/api/liquid/filters/hmac_sha1.md'
api_name: liquid
---

# hmac\_​sha1

```oobleck
string | hmac_sha1: string
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Converts a string into an SHA-1 hash using a hash message authentication code (HMAC).

The secret key for the message is supplied as a parameter to the filter.

##### Code

```liquid
{%- assign secret_potion = 'Polyjuice' | hmac_sha1: 'Polina' -%}

My secret potion: {{ secret_potion }}
```

##### Output

```html
My secret potion: 63304203b005ea4bc80546f1c6fdfe252d2062b2
```
