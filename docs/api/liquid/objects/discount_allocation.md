---
title: 'Liquid objects: discount_allocation'
description: Information about how a discount affects an item.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/discount_allocation'
  md: 'https://shopify.dev/docs/api/liquid/objects/discount_allocation.md'
api_name: liquid
---

# discount\_​allocation

Information about how a discount affects an item.

To learn about how to display discounts in your theme, refer to [Discounts](https://shopify.dev/themes/pricing-payments/discounts).

## Properties

* * **amount**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The amount that the item is discounted by in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **discount\_​application**

    [discount\_application](https://shopify.dev/docs/api/liquid/objects/discount_application)

  * The discount application that applies the discount to the item.

##### Example

```json
{
  "amount": "40.00",
  "discount_application": "DiscountApplicationDrop"
}
```
