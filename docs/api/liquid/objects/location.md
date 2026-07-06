---
title: 'Liquid objects: location'
description: 'A store [location](https://help.shopify.com/manual/locations).'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/location'
  md: 'https://shopify.dev/docs/api/liquid/objects/location.md'
api_name: liquid
---

# location

A store [location](https://help.shopify.com/manual/locations).

***

**Tip:** The \<code>location\</code> object is defined only if one or more locations has \<a href="https://help.shopify.com/manual/shipping/setting-up-and-managing-your-shipping/local-methods/local-pickup">local pickup\</a> enabled.

***

## Properties

* * **address**

    [address](https://shopify.dev/docs/api/liquid/objects/address)

  * The location's address.

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The location's ID.

  * **latitude**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The latitude of the location's address.

    If the location's address isn't verified, then `nil` is returned.

  * **longitude**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The longitude of the location's address.

    If the location's address isn't verified, then `nil` is returned.

  * **metafields**

  * The [metafields](https://shopify.dev/docs/api/liquid/objects/metafield) applied to the location.

    **Tip:** To learn about how to create metafields, refer to \<a href="/apps/metafields/manage">Create and manage metafields\</a> or visit the \<a href="https://help.shopify.com/manual/metafields">Shopify Help Center\</a>.

  * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The location's name.

##### Example

```json
{
  "address": {},
  "id": 62002462785,
  "latitude": 43.6556377,
  "longitude": -79.38681079999999,
  "metafields": {},
  "name": "123 Edward Street"
}
```
