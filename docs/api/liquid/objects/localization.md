---
title: 'Liquid objects: localization'
description: Information about the countries and languages that are available on a store.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/localization'
  md: 'https://shopify.dev/docs/api/liquid/objects/localization.md'
api_name: liquid
---

# localization

Information about the countries and languages that are available on a store.

The `localization` object can be used in a [localization form](https://shopify.dev/docs/api/liquid/tags/form#form-localization).

To learn about how to offer localization options in your theme, refer to [Support multiple currencies and languages](https://shopify.dev/themes/internationalization/multiple-currencies-languages).

## Properties

* * **available\_​countries**

    array of [country](https://shopify.dev/docs/api/liquid/objects/country)

  * The countries that are available on the store.

  * **available\_​languages**

    array of [shop\_locale](https://shopify.dev/docs/api/liquid/objects/shop_locale)

  * The languages that are available on the store.

  * **country**

    [country](https://shopify.dev/docs/api/liquid/objects/country)

  * The currently selected country on the storefront.

  * **language**

    [shop\_locale](https://shopify.dev/docs/api/liquid/objects/shop_locale)

  * The currently selected language on the storefront.

  * **market**

    [market](https://shopify.dev/docs/api/liquid/objects/market)

  * The currently selected market on the storefront.

##### Example

```json
{
  "available_countries": [],
  "available_languages": [],
  "country": {},
  "language": {},
  "market": {}
}
```
