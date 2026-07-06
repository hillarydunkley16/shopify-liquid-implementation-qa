---
title: 'Liquid objects: discount'
description: 'A discount applied to a cart, line item, or order.'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/discount'
  md: 'https://shopify.dev/docs/api/liquid/objects/discount.md'
api_name: liquid
---

# discount

A discount applied to a cart, line item, or order.

**deprecated:**

Deprecated because not all discount types and details are captured.

The `discount` object has been replaced by the [`discount_allocation`](https://shopify.dev/docs/api/liquid/objects/discount_allocation) and [`discount_application`](https://shopify.dev/docs/api/liquid/objects/discount_application) objects.

## Properties

* * **amount**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The amount of the discount in the currency's subunit.

    **Note:** This is the same value as \<a href="/docs/api/liquid/objects/discount#discount-total\_amount">\<code>\<span class="PreventFireFoxApplyingGapToWBR">discount.total\<wbr/>\_amount\</span>\</code>\</a>.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **code**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The customer-facing name of the discount.

    **Note:** This is the same value as \<a href="/docs/api/liquid/objects/discount#discount-title">\<code>discount.title\</code>\</a>.

  * **savings**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The amount of the discount as a negative value, in the currency's subunit.

    **Note:** This is the same value as \<a href="/docs/api/liquid/objects/discount#discount-total\_savings">\<code>\<span class="PreventFireFoxApplyingGapToWBR">discount.total\<wbr/>\_savings\</span>\</code>\</a>. The value is output in the customer\&#39;s local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **title**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The customer-facing name of the discount.

    **Note:** This is the same value as \<a href="/docs/api/liquid/objects/discount#discount-code">\<code>discount.code\</code>\</a>.

  * **total\_​amount**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The amount of the discount in the currency's subunit.

    **Note:** This is the same value as \<a href="/docs/api/liquid/objects/discount#discount-amount">\<code>discount.amount\</code>\</a>.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **total\_​savings**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The amount of the discount as a negative value, in the currency's subunit.

    **Note:** This is the same value as \<a href="/docs/api/liquid/objects/discount#discount-savings">\<code>discount.savings\</code>\</a>. The value is output in the customer\&#39;s local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **type**

    [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values

  * The type of the discount.

    | Possible values |
    | - |
    | FixedAmountDiscount |
    | PercentageDiscount |
    | ShippingDiscount |

##### Example

```json
{
  "amount": "40.00",
  "code": "DIY",
  "savings": "-40.00",
  "title": "DIY",
  "total_amount": "40.00",
  "total_savings": "-40.00",
  "type": "PercentageDiscount"
}
```
