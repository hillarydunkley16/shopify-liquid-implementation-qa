---
title: 'Liquid objects: shop_locale'
description: A language in a store.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/shop_locale'
  md: 'https://shopify.dev/docs/api/liquid/objects/shop_locale.md'
api_name: liquid
---

# shop\_​locale

A language in a store.

To learn how to offer localization options in your theme, refer to [Support multiple currencies and languages](https://shopify.dev/themes/internationalization/multiple-currencies-languages).

## Properties

* * **endonym\_​name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the locale in the locale itself.

  * **iso\_​code**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The ISO code of the locale in [IETF language tag format](https://en.wikipedia.org/wiki/IETF_language_tag).

  * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the locale in the store's primary locale.

  * **primary**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the locale is the store's primary locale. Returns `false` if not.

  * **root\_​url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The relative root URL of the locale.

##### Example

```json
{
  "endonym_name": "English",
  "iso_code": "en",
  "name": "English",
  "primary": true,
  "root_url": "/"
}
```
