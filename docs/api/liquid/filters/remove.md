---
title: 'Liquid filters: remove'
description: Removes any instance of a substring inside a string.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/remove'
  md: 'https://shopify.dev/docs/api/liquid/filters/remove.md'
api_name: liquid
---

# remove

```oobleck
string | remove: string
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Removes any instance of a substring inside a string.

##### Code

```liquid
{{ "I can't do it!" | remove: "'t" }}
```

##### Output

```html
I can do it!
```
