---
title: 'Liquid objects: company'
description: >-
  A company that a [customer](/docs/api/liquid/objects/customer) is purchasing
  for.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/company'
  md: 'https://shopify.dev/docs/api/liquid/objects/company.md'
api_name: liquid
---

# company

A company that a [customer](https://shopify.dev/docs/api/liquid/objects/customer) is purchasing for.

To learn about B2B in themes, refer to [Support B2B customers in your theme](https://shopify.dev/themes/pricing-payments/b2b).

## Properties

* * **available\_​locations**

    array of [company\_location](https://shopify.dev/docs/api/liquid/objects/company_location)

  * The company locations that the current customer has access to, or can interact with.

  * **available\_​locations\_​count**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The number of company locations associated with the customer's company.

  * **external\_​id**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The external ID of the company.

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the company.

  * **metafields**

    array of [metafield](https://shopify.dev/docs/api/liquid/objects/metafield)

  * The [metafields](https://shopify.dev/docs/api/liquid/objects/metafield) applied to the company.

    **Tip:** To learn about how to create metafields, refer to \<a href="/apps/metafields/manage">Create and manage metafields\</a> or visit the \<a href="https://help.shopify.com/manual/metafields">Shopify Help Center\</a>.

  * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the company.

##### Example

```json
{
  "available_locations": [],
  "available_locations_count": 1,
  "external_id": null,
  "id": 98369,
  "metafields": {},
  "name": "Cornelius&#39; Custom Concoctions"
}
```
