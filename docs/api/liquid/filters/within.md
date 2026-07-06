---
title: 'Liquid filters: within'
description: Generates a product URL within the context of the provided collection.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/within'
  md: 'https://shopify.dev/docs/api/liquid/filters/within.md'
api_name: liquid
---

# within

```oobleck
string | within: collection
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates a product URL within the context of the provided collection.

When the collection context is included, you can access the associated [`collection` object](https://shopify.dev/docs/api/liquid/objects/collection) in the [product template](https://shopify.dev/themes/architecture/templates/product).

***

**Caution:** Because a standard product page and a product page in the context of a collection have the same content on separate URLs, you should consider the SEO implications of using the \<code>within\</code> filter.

***

##### Code

```liquid
{%- assign collection_product = collection.products.first -%}

{{ collection_product.url | within: collection }}
```

##### Data

```json
{
  "collection": {
    "products": [
      {
        "url": "/products/draught-of-immortality"
      },
      {
        "url": "/products/glacier-ice"
      },
      {
        "url": "/products/health-potion"
      },
      {
        "url": "/products/invisibility-potion"
      }
    ]
  }
}
```

##### Output

```html
/collections/sale-potions/products/draught-of-immortality
```
