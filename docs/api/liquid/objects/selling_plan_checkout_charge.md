---
title: 'Liquid objects: selling_plan_checkout_charge'
description: >-
  Information about how a specific [selling
  plan](/apps/subscriptions/selling-plans) affects the amount that a

  customer needs to pay for a line item at checkout.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/selling_plan_checkout_charge'
  md: 'https://shopify.dev/docs/api/liquid/objects/selling_plan_checkout_charge.md'
api_name: liquid
---

# selling\_​plan\_​checkout\_​charge

Information about how a specific [selling plan](https://shopify.dev/apps/subscriptions/selling-plans) affects the amount that a customer needs to pay for a line item at checkout.

To learn about how to support selling plans in your theme, refer to [Purchase options](https://shopify.dev/themes/pricing-payments/purchase-options).

## Properties

* * **value**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The value of the checkout charge.

    How this value is interpreted depends on the [value type](https://shopify.dev/docs/api/liquid/objects/selling_plan_checkout_charge#selling_plan_checkout_charge-value_type) of the checkout charge. The following table outlines what the value represents for each value type:

    | Value type | Value |
    | - | - |
    | `percentage` | The percent amount of the original price that the customer needs to pay. For example, if the value is 50, then the customer needs to pay 50% of the original price. |
    | `price` | The amount that the customer needs to pay in the currency's subunit. |

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

  * **value\_​type**

    [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values

  * The value type of the checkout charge.

    | Possible values |
    | - |
    | percentage |
    | price |

##### Example

```json
{
  "value": 100,
  "value_type": "percentage"
}
```
