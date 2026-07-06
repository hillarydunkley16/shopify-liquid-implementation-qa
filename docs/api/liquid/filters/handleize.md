---
title: 'Liquid filters: handleize'
description: 'Converts a string into a [handle](/docs/api/liquid/basics#handles).'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/handleize'
  md: 'https://shopify.dev/docs/api/liquid/filters/handleize.md'
api_name: liquid
---

# handleize

```oobleck
string | handleize
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Converts a string into a [handle](https://shopify.dev/docs/api/liquid/basics#handles).

***

**Note:** The \<code>handleize\</code> filter has an alias of \<code>handle\</code>.

***

##### Code

```liquid
{{ product.title | handleize }}
{{ product.title | handle }}
```

##### Data

```json
{
  "product": {
    "title": "Health potion"
  }
}
```

##### Output

```html
health-potion
health-potion
```
