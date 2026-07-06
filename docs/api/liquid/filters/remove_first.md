---
title: 'Liquid filters: remove_first'
description: Removes the first instance of a substring inside a string.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/remove_first'
  md: 'https://shopify.dev/docs/api/liquid/filters/remove_first.md'
api_name: liquid
---

# remove\_​first

```oobleck
string | remove_first: string
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Removes the first instance of a substring inside a string.

##### Code

```liquid
{{ "I hate it when I accidentally spill my duplication potion accidentally!" | remove_first: ' accidentally' }}
```

##### Output

```html
I hate it when I spill my duplication potion accidentally!
```
