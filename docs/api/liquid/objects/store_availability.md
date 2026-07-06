---
title: 'Liquid objects: store_availability'
description: A variant's inventory information for a physical store location.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/store_availability'
  md: 'https://shopify.dev/docs/api/liquid/objects/store_availability.md'
api_name: liquid
---

# store\_​availability

A variant's inventory information for a physical store location.

If a location doesn't stock a variant, then there won't be a `store_availability` for that variant and location.

***

**Note:** The \<code>\<span class="PreventFireFoxApplyingGapToWBR">store\<wbr/>\_availability\</span>\</code> object is defined only if one or more locations has \<a href="https://help.shopify.com/manual/shipping/setting-up-and-managing-your-shipping/local-methods/local-pickup">local pickup\</a> enabled.

***

## Properties

* * **available**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the variant has available inventory at the location. Returns `false` if not.

  * **location**

    [location](https://shopify.dev/docs/api/liquid/objects/location)

  * The location that the variant is stocked at.

  * **pick\_​up\_​enabled**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the location has pickup enabled. Returns `false` if not.

  * **pick\_​up\_​time**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The amount of time that it takes for pickup orders to be ready at the location.

    **Tip:** This value can be configured in the Shopify admin. To learn more, visit the \<a href="https://help.shopify.com/en/manual/sell-in-person/shopify-pos/order-management/local-pickup-for-online-orders#manage-preferences-for-a-local-pickup-location">Shopify Help Center\</a>.

##### Example

```json
{
  "available": true,
  "location": {},
  "pick_up_enabled": true,
  "pick_up_time": "Usually ready in 24 hours"
}
```
