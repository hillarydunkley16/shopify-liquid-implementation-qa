---
title: 'Liquid filters: url_param_escape'
description: Escapes any characters in a string that are unsafe for URL parameters.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/url_param_escape'
  md: 'https://shopify.dev/docs/api/liquid/filters/url_param_escape.md'
api_name: liquid
---

# url\_​param\_​escape

```oobleck
string | url_param_escape
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Escapes any characters in a string that are unsafe for URL parameters.

The `url_param_escape` filter escapes the same characters as [`url_escape`](https://shopify.dev/docs/api/liquid/filters/url_escape), with the addition of `&`.

##### Code

```liquid
{{ '<p>Health & Love potions</p>' | url_param_escape }}
```

##### Output

```html
%3Cp%3EHealth%20%26%20Love%20potions%3C/p%3E
```
