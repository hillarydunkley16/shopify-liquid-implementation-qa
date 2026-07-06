---
title: 'Liquid filters: uniq'
description: Removes any duplicate items in an array.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/uniq'
  md: 'https://shopify.dev/docs/api/liquid/filters/uniq.md'
api_name: liquid
---

# uniq

```oobleck
array | uniq
```

Removes any duplicate items in an array.

##### Code

```liquid
{% assign potion_array = 'invisibility, health, love, health, invisibility' | split: ', ' %}

{{ potion_array | uniq | join: ', ' }}
```

##### Output

```html
invisibility, health, love
```
