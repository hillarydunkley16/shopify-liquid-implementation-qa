---
title: 'Liquid objects: sort_option'
description: A sort option for a collection or search results page.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/sort_option'
  md: 'https://shopify.dev/docs/api/liquid/objects/sort_option.md'
api_name: liquid
---

# sort\_​option

A sort option for a collection or search results page.

## Properties

* * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The customer-facing name of the sort option.

    The name can be edited by merchants in the [language editor](https://help.shopify.com/manual/online-store/themes/customizing-themes/language/change-wording).

  * **value**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The value of the sort option.

    This value is used when assigning the [`collection.sort_by`](https://shopify.dev/docs/api/liquid/objects/collection#collection-sort_by) and [`search.sort_by`](https://shopify.dev/docs/api/liquid/objects/search#search-sort_by) parameters.

##### Example

```json
{
  "name": "Alphabetically, A-Z",
  "value": "title-ascending"
}
```
