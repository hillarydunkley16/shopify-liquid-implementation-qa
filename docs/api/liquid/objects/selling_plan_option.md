---
title: 'Liquid objects: selling_plan_option'
description: >-
  Information about a selling plan's value for a specific
  [`selling_plan_group_option`](/docs/api/liquid/objects/selling_plan_group_option).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/selling_plan_option'
  md: 'https://shopify.dev/docs/api/liquid/objects/selling_plan_option.md'
api_name: liquid
---

# selling\_​plan\_​option

Information about a selling plan's value for a specific [`selling_plan_group_option`](https://shopify.dev/docs/api/liquid/objects/selling_plan_group_option).

To learn about how to support selling plans in your theme, refer to [Purchase options](https://shopify.dev/themes/pricing-payments/purchase-options).

## Properties

* * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the associated `selling_plan_group_option`.

  * **position**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The 1-based index of the selling plan option in the associated [`selling_plan_group.options` array](https://shopify.dev/docs/api/liquid/objects/selling_plan_group#selling_plan_group-options).

  * **value**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The value of the selling plan option.

    The value is one of the [`selling_plan_group_option.values`](https://shopify.dev/docs/api/liquid/objects/selling_plan_group_option#selling_plan_group_option-values).

##### Example

```json
{
  "name": "Delivery frequency",
  "position": 1,
  "value": "Deliver every week"
}
```
