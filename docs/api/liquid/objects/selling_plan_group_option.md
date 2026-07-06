---
title: 'Liquid objects: selling_plan_group_option'
description: >-
  Information about a specific option in a [selling plan
  group](/docs/api/liquid/objects/selling_plan_group).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/selling_plan_group_option'
  md: 'https://shopify.dev/docs/api/liquid/objects/selling_plan_group_option.md'
api_name: liquid
---

# selling\_​plan\_​group\_​option

Information about a specific option in a [selling plan group](https://shopify.dev/docs/api/liquid/objects/selling_plan_group).

## Properties

* * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the option.

  * **position**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The 1-based index of the option in the [`selling_plan_group.options` array](https://shopify.dev/docs/api/liquid/objects/selling_plan_group#selling_plan_group-options).

  * **selected\_​value**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The option value of the currently selected selling plan.

    If no selling plan is currently selected, then `nil` is returned.

    **Note:** The selected selling plan is determined by the \<code>\<span class="PreventFireFoxApplyingGapToWBR">selling\<wbr/>\_plan\</span>\</code> URL parameter.

  * **values**

    array of [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The values of the option.

##### Example

```json
{
  "name": "Delivery frequency",
  "position": 1,
  "selected_value": null,
  "values": [
    "Deliver every week",
    "Deliver every 4 weeks"
  ]
}
```
