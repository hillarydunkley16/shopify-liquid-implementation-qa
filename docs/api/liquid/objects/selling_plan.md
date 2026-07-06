---
title: 'Liquid objects: selling_plan'
description: >-
  Information about the intent of how a specific [selling
  plan](/apps/subscriptions/selling-plans) affects a line item.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/selling_plan'
  md: 'https://shopify.dev/docs/api/liquid/objects/selling_plan.md'
api_name: liquid
---

# selling\_​plan

Information about the intent of how a specific [selling plan](https://shopify.dev/apps/subscriptions/selling-plans) affects a line item.

To learn about how to support selling plans in your theme, refer to [Purchase options](https://shopify.dev/themes/pricing-payments/purchase-options).

## Properties

* * **checkout\_​charge**

    [selling\_plan\_checkout\_charge](https://shopify.dev/docs/api/liquid/objects/selling_plan_checkout_charge)

  * The checkout charge of the selling plan.

  * **description**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The description of the selling plan.

  * **group\_​id**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The ID of the [`selling_plan_group`](https://shopify.dev/docs/api/liquid/objects/selling_plan_group) that the selling plan belongs to.

    **Note:** The name is shown at checkout with the line item summary.

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the selling plan.

  * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the selling plan.

    **Note:** The name is shown at checkout with the line item summary.

  * **options**

    array of [selling\_plan\_option](https://shopify.dev/docs/api/liquid/objects/selling_plan_option)

  * The selling plan options.

  * **price\_​adjustments**

    array of [selling\_plan\_price\_adjustment](https://shopify.dev/docs/api/liquid/objects/selling_plan_price_adjustment)

  * The selling plan price adjustments.

    The maximum length of the array is two. If the selling plan doesn't create any price adjustments, then the array is empty.

    Each `selling_plan_price_adjustment` maps to a [`selling_plan_allocation_price_adjustment`](https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation_price_adjustment) in the [`selling_plan_allocation.price_adjustments` array](https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation#selling_plan_allocation-price_adjustments). The `selling_plan.price_adjustments` array contains the intent of the selling plan, and the `selling_plan_allocation.price_adjustments` contains the resulting money amounts.

  * **recurring\_​deliveries**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the selling plan includes multiple deliveries. Returns `false` if not.

  * **selected**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the selling plan is currently selected. Returns `false` if not.

    **Note:** The selected selling plan is determined by the \<code>\<span class="PreventFireFoxApplyingGapToWBR">selling\<wbr/>\_plan\</span>\</code> URL parameter.

##### Example

```json
{
  "checkout_charge": {},
  "description": null,
  "group_id": "e88ff8fdb3c39c89b564859e34542e0b982076d6",
  "id": 2595487809,
  "name": "Deliver every week, 10% off",
  "options": [],
  "price_adjustments": [],
  "recurring_deliveries": true,
  "selected": true
}
```
