---
title: 'Liquid objects: selling_plan_allocation'
description: >-
  Information about how a specific [selling
  plan](/apps/subscriptions/selling-plans) affects a line item.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation'
  md: 'https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation.md'
api_name: liquid
---

# selling\_​plan\_​allocation

Information about how a specific [selling plan](https://shopify.dev/apps/subscriptions/selling-plans) affects a line item.

To learn about how to support selling plans in your theme, refer to [Purchase options](https://shopify.dev/themes/pricing-payments/purchase-options).

## Properties

* * **checkout\_​charge\_​amount**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The amount that the customer will be charged at checkout in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

  * **compare\_​at\_​price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The **compare at** price of the selling plan allocation in the currency's subunit.

    The value of the **compare at** price is the line item's price without the selling plan applied.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

  * **per\_​delivery\_​price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The price for each delivery in the selling plan in the currency's subunit.

    If a selling plan includes multiple deliveries, then the `per_delivery_price` is the `price` divided by the number of deliveries.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

  * **price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The price of the selling plan allocation in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

  * **price\_​adjustments**

    array of [selling\_plan\_allocation\_price\_adjustment](https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation_price_adjustment)

  * The selling plan allocation price adjustments.

    The maximum length of the array is two. If the associated selling plan doesn't create any price adjustments, then the array is empty.

    Each `selling_plan_allocation_price_adjustment` maps to a [`selling_plan_price_adjustment`](https://shopify.dev/docs/api/liquid/objects/selling_plan_price_adjustment) in the [`selling_plan.price_adjustments` array](https://shopify.dev/docs/api/liquid/objects/selling_plan#selling_plan-price_adjustments). The `selling_plan.price_adjustments` array contains the intent of the selling plan, and the `selling_plan_allocation.price_adjustments` array contains the resulting money amounts.

  * **remaining\_​balance\_​charge\_​amount**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The remaining amount for the customer to pay, in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

  * **selling\_​plan**

    [selling\_plan](https://shopify.dev/docs/api/liquid/objects/selling_plan)

  * The selling plan that created the allocation.

  * **selling\_​plan\_​group\_​id**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The ID of the [`selling_plan_group`](https://shopify.dev/docs/api/liquid/objects/selling_plan_group) that the selling plan of the allocation belongs to.

  * **unit\_​price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The [unit price](https://shopify.dev/docs/api/liquid/objects/variant#variant-unit_price) of the variant associated with the selling plan, in the currency's subunit.

    If the variant doesn't have a unit price, then `nil` is returned.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

### Returned by

* [line\_​item.selling\_​plan\_​allocation](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-selling_plan_allocation)
* [variant.selling\_​plan\_​allocations](https://shopify.dev/docs/api/liquid/objects/variant#variant-selling_plan_allocations)
* [product.selected\_​selling\_​plan\_​allocation](https://shopify.dev/docs/api/liquid/objects/product#product-selected_selling_plan_allocation)
* [product.selected\_​or\_​first\_​available\_​selling\_​plan\_​allocation](https://shopify.dev/docs/api/liquid/objects/product#product-selected_or_first_available_selling_plan_allocation)
* [variant.selected\_​selling\_​plan\_​allocation](https://shopify.dev/docs/api/liquid/objects/variant#variant-selected_selling_plan_allocation)
* [remote\_​product.selected\_​selling\_​plan\_​allocation](https://shopify.dev/docs/api/liquid/objects/remote_product#remote_product-selected_selling_plan_allocation)
* [remote\_​product.selected\_​or\_​first\_​available\_​selling\_​plan\_​allocation](https://shopify.dev/docs/api/liquid/objects/remote_product#remote_product-selected_or_first_available_selling_plan_allocation)
