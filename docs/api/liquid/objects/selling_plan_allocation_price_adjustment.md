---
title: 'Liquid objects: selling_plan_allocation_price_adjustment'
description: >-
  The resulting price from the intent of the associated
  [`selling_plan_price_adjustment`](/docs/api/liquid/objects/selling_plan_price_adjustment).
source_url:
  html: >-
    https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation_price_adjustment
  md: >-
    https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation_price_adjustment.md
api_name: liquid
---

# selling\_​plan\_​allocation\_​price\_​adjustment

The resulting price from the intent of the associated [`selling_plan_price_adjustment`](https://shopify.dev/docs/api/liquid/objects/selling_plan_price_adjustment).

To learn about how to support selling plans in your theme, refer to [Purchase options](https://shopify.dev/themes/pricing-payments/purchase-options).

## Properties

* * **position**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The 1-based index of the price adjustment in the [`selling_plan_allocation.price_adjustments` array](https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation#selling_plan_allocation-price_adjustments).

  * **price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The price that will be charged for the price adjustment's lifetime, in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

### Returned by

* [selling\_​plan\_​allocation.price\_​adjustments](https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation#selling_plan_allocation-price_adjustments)
