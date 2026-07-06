---
title: 'Liquid objects: linklist'
description: >-
  A
  [menu](https://help.shopify.com/manual/online-store/menus-and-links/drop-down-menus)
  in a store.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/linklist'
  md: 'https://shopify.dev/docs/api/liquid/objects/linklist.md'
api_name: liquid
---

# linklist

A [menu](https://help.shopify.com/manual/online-store/menus-and-links/drop-down-menus) in a store.

To learn about how to implement navigation in a theme, refer to [Add navigation to your theme](https://shopify.dev/themes/navigation-search/navigation).

## Properties

* * **handle**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The [handle](https://shopify.dev/docs/api/liquid/basics#handles) of the menu.

  * **levels**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The number of nested levels in the menu.

    **Note:** There\&#39;s a maximum of 3 levels.

  * **links**

    array of [link](https://shopify.dev/docs/api/liquid/objects/link)

  * The links in the menu.

  * **title**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The title of the menu.

##### Example

```json
{
  "handle": "main-menu",
  "levels": 2,
  "links": [],
  "title": "Main menu"
}
```
