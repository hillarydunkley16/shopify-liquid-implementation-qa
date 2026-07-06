---
title: 'Liquid filters: round'
description: Rounds a number to the nearest integer.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/round'
  md: 'https://shopify.dev/docs/api/liquid/filters/round.md'
api_name: liquid
---

# round

```oobleck
number | round
```

returns [number](https://shopify.dev/docs/api/liquid/basics#number)

Rounds a number to the nearest integer.

##### Code

```liquid
{{ 2.7 | round }}
{{ 1.3 | round }}
```

##### Output

```html
3
1
```

### Round to a specific number of decimal places

You can specify a number of decimal places to round to. If you don't specify a number, then the `round` filter rounds to the nearest integer.

##### Code

```liquid
{{ 3.14159 | round: 2 }}
```

##### Output

```html
3.14
```
