---
title: 'Liquid objects: company_location'
description: >-
  A location of the [company](/docs/api/liquid/objects/company) that a
  [customer](/docs/api/liquid/objects/customer) is purchasing for.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/company_location'
  md: 'https://shopify.dev/docs/api/liquid/objects/company_location.md'
api_name: liquid
---

# company\_​location

A location of the [company](https://shopify.dev/docs/api/liquid/objects/company) that a [customer](https://shopify.dev/docs/api/liquid/objects/customer) is purchasing for.

To learn about B2B in themes, refer to [Support B2B customers in your theme](https://shopify.dev/themes/pricing-payments/b2b).

## Properties

* * **company**

    [company](https://shopify.dev/docs/api/liquid/objects/company)

  * The company that the location is associated with.

  * **current?**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the location is currently selected. Returns `false` if not.

  * **external\_​id**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The external ID of the location.

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the location.

  * **metafields**

    array of [metafield](https://shopify.dev/docs/api/liquid/objects/metafield)

  * The [metafields](https://shopify.dev/docs/api/liquid/objects/metafield) applied to the company location.

    **Tip:** To learn about how to create metafields, refer to \<a href="/apps/metafields/manage">Create and manage metafields\</a> or visit the \<a href="https://help.shopify.com/manual/metafields">Shopify Help Center\</a>.

  * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the location.

  * **shipping\_​address**

    [company\_address](https://shopify.dev/docs/api/liquid/objects/company_address)

  * The address of the location.

  * **store\_​credit\_​account**

    [store\_credit\_account](https://shopify.dev/docs/api/liquid/objects/store_credit_account)

  * The store credit account associated with the company location.

    The account shown will be in the currency associated with the company location’s current context. For example, when browsing a storefront for a company location in the US market, the company location's USD store credit account will be returned. If the company location does not have a USD store credit account `nil` will be returned.

  * **tax\_​registration\_​id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The tax ID of the location.

  * **url\_​to\_​set\_​as\_​current**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The URL to set the location as the current location for the customer.

##### Example

```json
{
  "company": {},
  "current?": false,
  "external_id": null,
  "id": 98369,
  "metafields": {},
  "name": "99 Cauldron Lane",
  "shipping_address": {},
  "store_credit_account": null,
  "tax_registration_id": null,
  "url_to_set_as_current": "https://polinas-potent-potions.myshopify.com/company_location/update?location_id=98369&return_to=/resource"
}
```
