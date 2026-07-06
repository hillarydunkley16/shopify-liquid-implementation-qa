---
title: 'Liquid filters: divided_by'
description: >-
  Divides a number by a given number. The `divided_by` filter produces a result
  of the same type as the divisor. This means if you divide by an integer, the
  result will be an integer, and if you divide by a float, the result will be a
  float.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/divided_by'
  md: 'https://shopify.dev/docs/api/liquid/filters/divided_by.md'
api_name: liquid
---

# divided\_​by

```oobleck
number | divided_by: number
```

returns [number](https://shopify.dev/docs/api/liquid/basics#number)

Divides a number by a given number. The `divided_by` filter produces a result of the same type as the divisor. This means if you divide by an integer, the result will be an integer, and if you divide by a float, the result will be a float.

##### Code

```liquid
{{ 4 | divided_by: 2 }}

# divisor is an integer
{{ 20 | divided_by: 7 }}

# divisor is a float 
{{ 20 | divided_by: 7.0 }}
```

##### Output

```html
2

# divisor is an integer
2

# divisor is a float 
2.857142857142857
```
