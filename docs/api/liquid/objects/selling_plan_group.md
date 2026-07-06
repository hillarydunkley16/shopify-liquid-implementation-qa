---
title: 'Liquid objects: selling_plan_group'
description: >-
  Information about a specific group of [selling
  plans](/apps/subscriptions/selling-plans) that include any of a

  product's variants.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/selling_plan_group'
  md: 'https://shopify.dev/docs/api/liquid/objects/selling_plan_group.md'
api_name: liquid
---

# selling\_​plan\_​group

Information about a specific group of [selling plans](https://shopify.dev/apps/subscriptions/selling-plans) that include any of a product's variants.

Selling plans are grouped based on shared [selling plan option names](https://shopify.dev/docs/api/liquid/objects/selling_plan_option#selling_plan_option-name).

To learn about how to support selling plans in your theme, refer to [Purchase options](https://shopify.dev/themes/pricing-payments/purchase-options).

## Properties

* * **app\_​id**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * An optional string provided by an app to identify selling plan groups created by that app.

    If the app doesn't provide a value, then `nil` is returned.

    **Tip:** You can use this property, with the \<a href="/docs/api/liquid/filters/where">\<code>where\</code> filter\</a>, to filter the \<a href="/docs/api/liquid/objects/product#product-selling\_plan\_groups">\<code>\<span class="PreventFireFoxApplyingGapToWBR">product.selling\<wbr/>\_plan\<wbr/>\_groups\</span>\</code> array\</a> for all selling plan groups from a specific app.

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the selling plan group.

  * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the selling plan group.

  * **options**

    array of [selling\_plan\_group\_option](https://shopify.dev/docs/api/liquid/objects/selling_plan_group_option)

  * The selling plan group options.

  * **selling\_​plan\_​selected**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the currently selected selling plan is part of the selling plan group. Returns `false` if not.

    **Note:** The selected selling plan is determined by the \<code>\<span class="PreventFireFoxApplyingGapToWBR">selling\<wbr/>\_plan\</span>\</code> URL parameter.

  * **selling\_​plans**

    array of [selling\_plan](https://shopify.dev/docs/api/liquid/objects/selling_plan)

  * The selling plans in the group.

##### Example

```json
{
  "app_id": "gid://shopify/App/66228322305",
  "id": "e88ff8fdb3c39c89b564859e34542e0b982076d6",
  "name": "1 Week(s), 4 Week(s)",
  "options": [],
  "selling_plan_selected": false,
  "selling_plans": []
}
```
