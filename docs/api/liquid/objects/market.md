---
title: 'Liquid objects: market'
description: >-
  A group of one or more regions of the world that a merchant is targeting for
  sales.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/market'
  md: 'https://shopify.dev/docs/api/liquid/objects/market.md'
api_name: liquid
---

# market

A group of one or more regions of the world that a merchant is targeting for sales.

To learn more about markets, refer to [Shopify Markets](https://shopify.dev/docs/apps/markets). To make sure that visitors interact with the optimal version of a store using Shopify Markets, refer to [Detect and set a visitor's optimal localization](https://shopify.dev/docs/themes/markets/localization-discovery).

## Properties

* * **handle**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The [handle](https://shopify.dev/docs/api/liquid/basics#handles) of the market.

  * **id**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The ID of the market.

  * **metafields**

    array of [metafield](https://shopify.dev/docs/api/liquid/objects/metafield)

  * The [metafields](https://shopify.dev/docs/api/liquid/objects/metafield) applied to the market.

    **Tip:** To learn about how to create metafields, refer to \<a href="/apps/metafields/manage">Create and manage metafields\</a> or visit the \<a href="https://help.shopify.com/manual/metafields">Shopify Help Center\</a>.

##### Example

```json
{
  "handle": "ca",
  "id": 6157828161,
  "metafields": {}
}
```
