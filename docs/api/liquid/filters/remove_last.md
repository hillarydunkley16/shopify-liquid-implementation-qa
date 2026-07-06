---
title: 'Liquid filters: remove_last'
description: Removes the last instance of a substring inside a string.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/remove_last'
  md: 'https://shopify.dev/docs/api/liquid/filters/remove_last.md'
api_name: liquid
---

# remove\_​last

```oobleck
string | remove_last: string
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Removes the last instance of a substring inside a string.

##### Code

```liquid
{{ "I hate it when I accidentally spill my duplication potion accidentally!" | remove_last: ' accidentally' }}
```

##### Output

```html
I hate it when I accidentally spill my duplication potion!
```
