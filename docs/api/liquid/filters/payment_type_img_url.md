---
title: 'Liquid filters: payment_type_img_url'
description: >-
  Returns the URL for an SVG image of a given [payment
  type](/docs/api/liquid/objects/shop#shop-enabled_payment_types).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/payment_type_img_url'
  md: 'https://shopify.dev/docs/api/liquid/filters/payment_type_img_url.md'
api_name: liquid
---

# payment\_​type\_​img\_​url

```oobleck
string | payment_type_img_url
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Returns the URL for an SVG image of a given [payment type](https://shopify.dev/docs/api/liquid/objects/shop#shop-enabled_payment_types).

##### Code

```liquid
{% for type in shop.enabled_payment_types %}
<img src="{{ type | payment_type_img_url }}" width="50" height="50" />
{% endfor %}
```

##### Data

```json
{
  "shop": {
    "enabled_payment_types": [
      "visa",
      "master",
      "american_express",
      "paypal",
      "diners_club",
      "discover"
    ]
  }
}
```

##### Output

```html
<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment_icons/visa-b614b878.svg" width="50" height="50" />

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment_icons/master-f5a74105.svg" width="50" height="50" />

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment_icons/american_express-2bdbf0e2.svg" width="50" height="50" />

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment_icons/paypal-a7c68b85.svg" width="50" height="50" />

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment_icons/diners_club-678e3046.svg" width="50" height="50" />

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment_icons/discover-59880595.svg" width="50" height="50" />
```

## Rendered output
