---
title: 'Liquid objects: policy'
description: >-
  A [store
  policy](https://help.shopify.com/manual/checkout-settings/refund-privacy-tos),
  such as a privacy or return policy.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/policy'
  md: 'https://shopify.dev/docs/api/liquid/objects/policy.md'
api_name: liquid
---

# policy

A [store policy](https://help.shopify.com/manual/checkout-settings/refund-privacy-tos), such as a privacy or return policy.

## Properties

* * **body**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The content of the policy.

  * **id**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The ID of the policy.

  * **title**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The title of the policy.

  * **url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The relative URL of the policy.

##### Example

```json
{
  "body": "<p>We have a 30-day return policy, which means you have 30 days after receiving your item to request a return. ...</p>",
  "id": 23805034561,
  "title": "Refund policy",
  "url": "/policies/refund-policy"
}
```
