---
title: 'Liquid objects: product_option'
description: 'A product option, such as size or color.'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/product_option'
  md: 'https://shopify.dev/docs/api/liquid/objects/product_option.md'
api_name: liquid
---

# product\_​option

A product option, such as size or color.

## Properties

* * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the product option.

  * **position**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The 1-based index of the product option in the [`product.options_with_values` array](https://shopify.dev/docs/api/liquid/objects/product#product-options_with_values).

  * **selected\_​value**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The currently selected product option value.

    If no value is currently selected, then the first available variant is returned.

  * **values**

    array of [product\_option\_value](https://shopify.dev/docs/api/liquid/objects/product_option_value)

  * The possible values for the product option.

##### Example

```json
{
  "name": "Size",
  "position": 1,
  "selected_value": {},
  "values": []
}
```
