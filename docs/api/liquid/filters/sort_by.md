---
title: 'Liquid filters: sort_by'
description: >-
  Generates a collection URL with the provided `sort_by` parameter appended.

  This filter must be applied to the object property
  [`collection.url`](https://shopify.dev/docs/api/liquid/objects/collection#collection-url).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/sort_by'
  md: 'https://shopify.dev/docs/api/liquid/filters/sort_by.md'
api_name: liquid
---

# sort\_​by

```oobleck
string | sort_by: string
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates a collection URL with the provided `sort_by` parameter appended. This filter must be applied to the object property [`collection.url`](https://shopify.dev/docs/api/liquid/objects/collection#collection-url).

Accepts the following values:

* `manual` (as defined in the [collection settings](https://help.shopify.com/manual/products/collections/collection-layout#change-the-sort-order-for-the-products-in-a-collection))
* `best-selling`
* `title-ascending`
* `title-descending`
* `price-ascending`
* `price-descending`
* `created-ascending`
* `created-descending`

***

**Tip:** You can append the \<code>\<span class="PreventFireFoxApplyingGapToWBR">sort\<wbr/>\_by\</span>\</code> filter to the \<a href="/docs/api/liquid/filters/url\_for\_type">\<code>\<span class="PreventFireFoxApplyingGapToWBR">url\<wbr/>\_for\<wbr/>\_type\</span>\</code>\</a> and \<a href="/docs/api/liquid/filters/url\_for\_vendor">\<code>\<span class="PreventFireFoxApplyingGapToWBR">url\<wbr/>\_for\<wbr/>\_vendor\</span>\</code>\</a> filters.

***

##### Code

```liquid
{{ collection.url | sort_by: 'best-selling' }}
```

##### Data

```json
{
  "collection": {
    "url": "/collections/sale-potions"
  }
}
```

##### Output

```html
/collections/sale-potions?sort_by=best-selling
```
