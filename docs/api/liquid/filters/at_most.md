---
title: 'Liquid filters: at_most'
description: Limits a number to a maximum value.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/at_most'
  md: 'https://shopify.dev/docs/api/liquid/filters/at_most.md'
api_name: liquid
---

# at\_​most

```oobleck
number | at_most
```

returns [number](https://shopify.dev/docs/api/liquid/basics#number)

Limits a number to a maximum value.

##### Code

```liquid
{{ 6 | at_most: 5 }}
{{ 4 | at_most: 5 }}
```

##### Output

```html
5
4
```
