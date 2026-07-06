---
title: 'Liquid objects: company_address'
description: The address of a company location.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/company_address'
  md: 'https://shopify.dev/docs/api/liquid/objects/company_address.md'
api_name: liquid
---

# company\_​address

The address of a company location.

To learn about B2B in themes, refer to [Support B2B customers in your theme](https://shopify.dev/themes/pricing-payments/b2b).

## Properties

* * **address1**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The first line of the address.

  * **address2**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The second line of the address.

    If no second line is specified, then `nil` is returned.

  * **attention**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The attention line of the address.

  * **city**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The city of the address.

  * **country**

    [country](https://shopify.dev/docs/api/liquid/objects/country)

  * The country of the address.

  * **country\_​code**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The country of the address in [ISO 3166-1 (alpha 2) format](https://www.iso.org/glossary-for-iso-3166.html).

  * **first\_​name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The first name of the address.

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the address.

  * **last\_​name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The last name of the address.

  * **province**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The province of the address.

  * **province\_​code**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The province of the address in [ISO 3166-2 (alpha 2) format](https://www.iso.org/glossary-for-iso-3166.html).

    **Note:** The value doesn\&#39;t include the preceding \<a href="https://www\.iso.org/glossary-for-iso-3166.html">ISO 3166-1\</a> country code.

  * **street**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A combination of the first and second lines of the address.

  * **zip**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The zip or postal code of the address.

##### Example

```json
{
  "address1": "99 Cauldron Lane",
  "address2": "Unit 4B",
  "attention": "Cornelius&#39; Custom Concoctions",
  "city": "Edinburgh",
  "country": {},
  "country_code": "GB",
  "first_name": "Cornelius",
  "id": 65,
  "last_name": "Potionmaker",
  "province": null,
  "province_code": null,
  "street": "99 Cauldron Lane, Unit 4B",
  "zip": "EH95 1AF"
}
```
