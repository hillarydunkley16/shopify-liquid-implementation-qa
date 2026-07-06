---
title: 'Liquid objects: unit_price_measurement'
description: >-
  Information about how units of a product variant are measured. It's used to
  calculate

  [unit
  prices](https://help.shopify.com/manual/products/details/product-pricing/unit-pricing#add-unit-prices-to-your-product).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/unit_price_measurement'
  md: 'https://shopify.dev/docs/api/liquid/objects/unit_price_measurement.md'
api_name: liquid
---

# unit\_​price\_​measurement

Information about how units of a product variant are measured. It's used to calculate [unit prices](https://help.shopify.com/manual/products/details/product-pricing/unit-pricing#add-unit-prices-to-your-product).

## Properties

* * **measured\_​type**

    [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values

  * The type of unit measurement.

    | Possible values |
    | - |
    | volume |
    | weight |
    | length |
    | area |
    | count |

  * **quantity\_​unit**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The unit of measurement used to measure the [`quantity_value`](https://shopify.dev/docs/api/liquid/objects/unit_price_measurement#unit_price_measurement-quantity_value).

  * **quantity\_​value**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The quantity of the unit.

  * **reference\_​unit**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The unit of measurement used to measure the [`reference_value`](https://shopify.dev/docs/api/liquid/objects/unit_price_measurement#unit_price_measurement-reference_value).

  * **reference\_​value**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The quantity of the unit for the base unit price.

##### Example

```json
{
  "measured_type": "weight",
  "quantity_value": "500.0",
  "quantity_unit": "g",
  "reference_value": 1,
  "reference_unit": "kg"
}
```
