---
title: 'Liquid filters: url_escape'
description: Escapes any URL-unsafe characters in a string.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/url_escape'
  md: 'https://shopify.dev/docs/api/liquid/filters/url_escape.md'
api_name: liquid
---

# url\_​escape

```oobleck
string | url_escape
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Escapes any URL-unsafe characters in a string.

##### Code

```liquid
{{ '<p>Health & Love potions</p>' | url_escape }}
```

##### Output

```html
%3Cp%3EHealth%20&%20Love%20potions%3C/p%3E
```
