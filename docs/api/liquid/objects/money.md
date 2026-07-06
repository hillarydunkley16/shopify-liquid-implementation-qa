---
title: 'Liquid objects: money'
description: 'A money value, in the the customer''s local (presentment) currency.'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/money'
  md: 'https://shopify.dev/docs/api/liquid/objects/money.md'
api_name: liquid
---

# money

A money value, in the the customer's local (presentment) currency.

***

**Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

***

## Properties

* * **currency**

    [currency](https://shopify.dev/docs/api/liquid/objects/currency)

  * The customer's local (presentment) currency.

##### Example

```json
{
  "currency": {}
}
```

### Referencing money objects directly

When a money object is referenced directly, the money value in cents is returned.

##### Code

```liquid
{{ product.metafields.details.price_per_100g.value }}
```

##### Data

```json
{
  "product": {
    "metafields": {}
  }
}
```

##### Output

```html
1796
```
