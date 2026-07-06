---
title: 'Liquid objects: address'
description: 'An address, such as a customer address or order shipping address.'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/address'
  md: 'https://shopify.dev/docs/api/liquid/objects/address.md'
api_name: liquid
---

# address

An address, such as a customer address or order shipping address.

***

**Tip:** Use the \<a href="/docs/api/liquid/filters/format\_address">\<code>\<span class="PreventFireFoxApplyingGapToWBR">format\<wbr/>\_address\</span>\</code> filter\</a> to output an address according to its locale.

***

## Properties

* * **address1**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The first line of the address.

  * **address2**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The second line of the address.

    If no second line is specified, then `nil` is returned.

  * **city**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The city of the address.

  * **company**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The company of the address.

    If no company is specified, then `nil` is returned.

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

  * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A combination of the first and last names of the address.

  * **phone**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The phone number of the address.

    If no phone number is specified, then `nil` is returned.

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

  * **summary**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A summary of the address, including the following properties:

    * First and last name
    * First and second lines
    * City
    * Province
    * Country

  * **url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The relative URL for the address.

    **Note:** This only applies to customer addresses.

  * **zip**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The zip or postal code of the address.

##### Example

```json
{
  "address1": "150 Elgin Street",
  "address2": "8th floor",
  "city": "Ottawa",
  "company": "Polina&#39;s Potions, LLC",
  "country": {},
  "country_code": "CA",
  "first_name": null,
  "id": 56174706753,
  "last_name": null,
  "name": "",
  "phone": "416-123-1234",
  "province": "Ontario",
  "province_code": "ON",
  "street": "150 Elgin Street, 8th floor",
  "summary": "150 Elgin Street, 8th floor, Ottawa, Ontario, Canada",
  "url": "/account/addresses/56174706753",
  "zip": "K2P 1L4"
}
```
