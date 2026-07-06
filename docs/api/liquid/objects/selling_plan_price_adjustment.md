---
title: 'Liquid objects: selling_plan_price_adjustment'
description: >-
  Information about how a selling plan changes the price of a variant for a
  given period of time.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/selling_plan_price_adjustment'
  md: 'https://shopify.dev/docs/api/liquid/objects/selling_plan_price_adjustment.md'
api_name: liquid
---

# selling\_​plan\_​price\_​adjustment

Information about how a selling plan changes the price of a variant for a given period of time.

To learn about how to support selling plans in your theme, refer to [Purchase options](https://shopify.dev/themes/pricing-payments/purchase-options).

## Properties

* * **order\_​count**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The number of orders that the price adjustment applies to.

  * **position**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The 1-based index of the price adjustment in the [`selling_plan.price_adjustments` array](https://shopify.dev/docs/api/liquid/objects/selling_plan#selling_plan-price_adjustments).

  * **value**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The value of the price adjustment as a decimal.

    How this value is interpreted depends on the [value type](https://shopify.dev/docs/api/liquid/objects/selling_plan_price_adjustment#selling_plan_price_adjustment-value_type) of the price adjustment. The following table outlines what the value represents for each value type:

    | Value type | Value |
    | - | - |
    | `fixed_amount` | The amount that the original price is being adjusted by, in the currency's subunit. |
    | `percentage` | The percent amount that the original price is being adjusted by. |
    | `price` | The adjusted amount in the currency's subunit. |

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

  * **value\_​type**

    [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values

  * The type of price adjustment.

    | Possible values |
    | - |
    | percentage |
    | fixed\_amount |
    | price |

##### Example

```json
{
  "order_count": null,
  "position": 1,
  "value": 10,
  "value_type": "percentage"
}
```
