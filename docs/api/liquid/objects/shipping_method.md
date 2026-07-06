---
title: 'Liquid objects: shipping_method'
description: Information about the shipping method for an order.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/shipping_method'
  md: 'https://shopify.dev/docs/api/liquid/objects/shipping_method.md'
api_name: liquid
---

# shipping\_​method

Information about the shipping method for an order.

## Properties

* * **discount\_​allocations**

    array of [discount\_allocation](https://shopify.dev/docs/api/liquid/objects/discount_allocation)

  * The discount allocations that apply to the shipping method.

  * **handle**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The [handle](https://shopify.dev/docs/api/liquid/basics#handles) of the shipping method.

    **Note:** The price of the shipping method is appended to handle.

  * **id**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The ID of the shipping method.

  * **original\_​price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The price of the shipping method in the currency's subunit, before discounts have been applied.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

  * **price\_​with\_​discounts**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The price of the shipping method in the currency's subunit, after discounts have been applied, including order level discounts.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

  * **tax\_​lines**

    array of [tax\_line](https://shopify.dev/docs/api/liquid/objects/tax_line)

  * The tax lines for the shipping method.

  * **title**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The title of the shipping method.

    In most contexts, the shipping method title appears in the customer's preferred language. However, in the context of an [order](https://shopify.dev/docs/api/liquid/objects/order), the shipping method title appears in the language that the customer checked out in.

## Deprecated Properties

* * **price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

    Deprecated

  * The price of the shipping method in the currency's subunit, after discounts have been applied.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

    **Deprecated:**

    Deprecated because the price did not include order level discounts.

    The `shipping_line.price` property has been replaced by [`shipping_line.price_with_discounts`](https://shopify.dev/docs/api/liquid/objects/shipping_method#shipping_method-price_with_discounts).

##### Example

```json
{
  "handle": "shopify-Standard-0.00",
  "id": "shopify-Standard-0.00",
  "original_price": "0.00",
  "price": "0.00",
  "price_with_discounts": "0.00",
  "tax_lines": [],
  "title": "Standard"
}
```
