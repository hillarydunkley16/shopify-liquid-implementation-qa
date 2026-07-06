---
title: 'Liquid filters: capitalize'
description: Capitalizes the first word in a string and downcases the remaining characters.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/capitalize'
  md: 'https://shopify.dev/docs/api/liquid/filters/capitalize.md'
api_name: liquid
---

# capitalize

```oobleck
string | capitalize
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Capitalizes the first word in a string and downcases the remaining characters.

##### Code

```liquid
{{ 'this sentence should start with a capitalized word.' | capitalize }}
```

##### Output

```html
This sentence should start with a capitalized word.
```
