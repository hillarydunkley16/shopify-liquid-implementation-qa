---
title: 'Liquid filters: line_items_for'
description: >-
  Returns the subset of
  [`cart`](https://shopify.dev/docs/api/liquid/objects/cart) line items that
  include a specified product or variant.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/line_items_for'
  md: 'https://shopify.dev/docs/api/liquid/filters/line_items_for.md'
api_name: liquid
---

# line\_​items\_​for

```oobleck
cart | line_items_for: object
```

returns array of [line\_item](https://shopify.dev/docs/api/liquid/objects/line_item)

Returns the subset of [`cart`](https://shopify.dev/docs/api/liquid/objects/cart) line items that include a specified product or variant.

Accepts the following object types:

* `product`
* `variant`

##### Code

```liquid
{% assign product = all_products['bloodroot-whole'] %}
{% assign line_items = cart | line_items_for: product %}

Total cart quantity for product: {{ line_items | sum: 'quantity' }}
```

##### Data

```json
{
  "all_products": {
    "bloodroot-whole": {}
  }
}
```

##### Output

```html
Total cart quantity for product: 1
```

##### Code

```liquid
{% assign product = all_products['bloodroot-whole'] %}
{% assign variant = product.variants.first %}
{% assign line_items = cart | line_items_for: variant %}

Total cart quantity for variant: {{ line_items | sum: 'quantity' }}
```

##### Data

```json
{
  "all_products": {
    "bloodroot-whole": {
      "variants": []
    }
  },
  "product": {
    "variants": []
  }
}
```

##### Output

```html
Total cart quantity for variant: 1
```
