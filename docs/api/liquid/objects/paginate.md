---
title: 'Liquid objects: paginate'
description: >-
  Information about the pagination inside a set of [`paginate`
  tags](/docs/api/liquid/tags/paginate).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/paginate'
  md: 'https://shopify.dev/docs/api/liquid/objects/paginate.md'
api_name: liquid
---

# paginate

Information about the pagination inside a set of [`paginate` tags](https://shopify.dev/docs/api/liquid/tags/paginate).

***

**Tip:** Use the \<a href="/docs/api/liquid/filters/default\_pagination">\<code>\<span class="PreventFireFoxApplyingGapToWBR">default\<wbr/>\_pagination\</span>\</code> filter\</a> to output pagination links.

***

## Properties

* * **current\_​offset**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The total number of items on pages previous to the current page.

    For example, if you show 5 items per page and are on page 3, then the value of `paginate.current_offset` is 10.

    Limited to 24,999 see [Pagination Limits](https://shopify.dev/themes/best-practices/performance/platform#pagination-limits) for more information.

  * **current\_​page**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The page number of the current page.

    Limited to 25,000 see [Pagination Limits](https://shopify.dev/themes/best-practices/performance/platform#pagination-limits) for more information.

  * **items**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The total number of items to be paginated.

    For example, if you paginate a collection of 120 products, then the value of `paginate.items` is 120.

    Limited to 25,000 see [Pagination Limits](https://shopify.dev/themes/best-practices/performance/platform#pagination-limits) for more information.

  * **next**

    [part](https://shopify.dev/docs/api/liquid/objects/part)

  * The pagination part to go to the next page.

  * **page\_​param**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The URL parameter denoting the pagination.

    The default value is `page`.

    If you paginate over an array defined in a setting or a metafield list type, then a unique key is appended to page to allow the paginated list to operate independently from other lists on the page. For example, a paginated list defined in a setting might use the key `page_a9e329dc`.

  * **page\_​size**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The number of items displayed per page.

    Limited to 250.

  * **pages**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The total number of pages.

    Limited to 25,000 see [Pagination Limits](https://shopify.dev/themes/best-practices/performance/platform#pagination-limits) for more information.

  * **parts**

    array of [part](https://shopify.dev/docs/api/liquid/objects/part)

  * The pagination parts.

    Pagination parts are used to build pagination navigation.

  * **previous**

    [part](https://shopify.dev/docs/api/liquid/objects/part)

  * The pagination part to go to the previous page.

##### Example

```json
{
  "current_offset": 10,
  "current_page": 3,
  "items": 17,
  "next": {},
  "page_param": "page",
  "page_size": 5,
  "pages": 4,
  "parts": [],
  "previous": {}
}
```
