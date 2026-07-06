---
title: 'Liquid objects: taxonomy_category'
description: The taxonomy category for a product
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/taxonomy_category'
  md: 'https://shopify.dev/docs/api/liquid/objects/taxonomy_category.md'
api_name: liquid
---

# taxonomy\_​category

The taxonomy category for a product

## Properties

* * **ancestors**

    array of [taxonomy\_category](https://shopify.dev/docs/api/liquid/objects/taxonomy_category)

  * All parent nodes of the current taxonomy category.

  * **gid**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The public node ID for the category, formatted as a Shopify GID.

  * **id**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The public node ID for the category

  * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The localized category name

##### Example

```json
{
  "ancestors": [],
  "gid": "gid://shopify/TaxonomyCategory/hb-1-9-6",
  "id": "hb-1-9-6",
  "name": "Vitamins & Supplements"
}
```
