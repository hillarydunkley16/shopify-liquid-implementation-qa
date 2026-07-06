---
title: 'Liquid filters: at_least'
description: Limits a number to a minimum value.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/at_least'
  md: 'https://shopify.dev/docs/api/liquid/filters/at_least.md'
api_name: liquid
---

# at\_​least

```oobleck
number | at_least
```

returns [number](https://shopify.dev/docs/api/liquid/basics#number)

Limits a number to a minimum value.

##### Code

```liquid
{{ 4 | at_least: 5 }}
{{ 4 | at_least: 3 }}
```

##### Output

```html
5
4
```
