---
title: 'Liquid objects: recipient'
description: >-
  A recipient that is associated with a [gift
  card](https://help.shopify.com/manual/products/gift-card-products).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/recipient'
  md: 'https://shopify.dev/docs/api/liquid/objects/recipient.md'
api_name: liquid
---

# recipient

A recipient that is associated with a [gift card](https://help.shopify.com/manual/products/gift-card-products).

## Properties

* * **email**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The email of the recipient.

  * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The full name of the recipient.

  * **nickname**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The nickname of the recipient.

##### Example

```json
{
  "email": "cornelius.potionmaker@gmail.com",
  "name": "Cornelius Potionmaker",
  "nickname": "Cornelius"
}
```

## Templates using recipient

[Theme architecture](https://shopify.dev/themes/architecture/templates/gift-card-liquid)

[gift\_card.liquid template](https://shopify.dev/themes/architecture/templates/gift-card-liquid)
