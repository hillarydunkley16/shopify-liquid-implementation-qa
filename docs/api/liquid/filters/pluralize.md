---
title: 'Liquid filters: pluralize'
description: Outputs the singular or plural version of a string based on a given number.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/pluralize'
  md: 'https://shopify.dev/docs/api/liquid/filters/pluralize.md'
api_name: liquid
---

# pluralize

```oobleck
number | pluralize: string, string
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Outputs the singular or plural version of a string based on a given number.

***

**Caution:** The \<code>pluralize\</code> filter applies English pluralization rules to determine which string to output. You shouldn\&#39;t use this filter on non-English strings because it could lead to incorrect pluralizations.

***

##### Code

```liquid
Cart item count: {{ cart.item_count }} {{ cart.item_count | pluralize: 'item', 'items' }}
```

##### Data

```json
{
  "cart": {
    "item_count": 2
  }
}
```

##### Output

```html
Cart item count: 2 items
```
