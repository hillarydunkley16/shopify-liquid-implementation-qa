---
title: 'Liquid objects: checkout'
description: A customer's checkout.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/checkout'
  md: 'https://shopify.dev/docs/api/liquid/objects/checkout.md'
api_name: liquid
---

# checkout

A customer's checkout.

***

**Deprecated:** \</p> \<p>The \<code>checkout\</code> object will be deprecated for the Information, Shipping, and Payment pages on August 13, 2024. Merchants who have customized these pages using \<code>checkout.liquid\</code> need to \<a href="https://help.shopify.com/manual/online-store/themes/theme-structure/extend/checkout-migration#migrate-to-checkout-extensibility">upgrade to Checkout Extensibility\</a> before August 13, 2024.\</p> \<p>Learn \<a href="/apps/checkout">how to build checkout extensions\</a> that extend the functionality of Shopify checkout.

***

You can access the `checkout` object on the [**Order status** page](https://help.shopify.com/manual/orders/status-tracking/customize-order-status).

Shopify Plus merchants can access the `checkout` object in the [`checkout.liquid` layout](https://shopify.dev/themes/architecture/layouts/checkout-liquid).

## Properties

* * **applied\_​gift\_​cards**

    array of [gift\_card](https://shopify.dev/docs/api/liquid/objects/gift_card)

  * The gift cards applied to the checkout.

  * **attributes**

  * Additional attributes entered by the customer with the [cart](https://shopify.dev/docs/api/liquid/objects/cart#cart-attributes).

    Shopify Plus merchants that have access to `checkout.liquid` can [capture attributes at checkout](https://shopify.dev/themes/architecture/layouts/checkout-liquid#capture-checkout-attributes).

  * **billing\_​address**

    [address](https://shopify.dev/docs/api/liquid/objects/address)

  * The billing address entered at checkout.

  * **buyer\_​accepts\_​marketing**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the customer checks the email marketing subscription checkbox. Returns `false` if not.

  * **cart\_​level\_​discount\_​applications**

    array of [discount\_application](https://shopify.dev/docs/api/liquid/objects/discount_application)

  * The cart-specific discount applications for the checkout.

  * **currency**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The [ISO code](https://www.iso.org/iso-4217-currency-codes.html) of the currency of the checkout.

  * **customer**

    [customer](https://shopify.dev/docs/api/liquid/objects/customer)

  * The customer associated with the checkout.

    **Note:** The \<a href="/docs/api/liquid/objects/customer">\<code>customer\</code> object\</a> is directly accessible globally when a customer is logged in to their account.

  * **discount\_​applications**

    array of [discount\_application](https://shopify.dev/docs/api/liquid/objects/discount_application)

  * The discount applications for the checkout.

  * **discounts\_​amount**

    array of [discount\_application](https://shopify.dev/docs/api/liquid/objects/discount_application)

  * The total amount of the discounts applied to the checkout in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **discounts\_​savings**

    array of [discount\_application](https://shopify.dev/docs/api/liquid/objects/discount_application)

  * The total amount of the discounts applied to the checkout in the currency's subunit, as a negative value.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **email**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The email associated with the checkout.

  * **gift\_​cards\_​amount**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The amount of the checkout price paid in gift cards.

    The value is output in the customer's local (presentment) currency.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the checkout.

  * **item\_​count**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The number of items in the checkout.

  * **line\_​items**

    array of [line\_item](https://shopify.dev/docs/api/liquid/objects/line_item)

  * The line items of the checkout.

  * **line\_​items\_​subtotal\_​price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The sum of the prices of all of the line items of the checkout in the currency's subunit, after any line item discounts. have been applied.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **name**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The name of the checkout.

    This value is the same as [`checkout.id`](https://shopify.dev/docs/api/liquid/objects/checkout#checkout-id) with a `#` prepended to it.

  * **note**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * Additional information entered by the customer with the [cart](https://shopify.dev/docs/api/liquid/objects/cart#cart-note).

  * **order**

    [order](https://shopify.dev/docs/api/liquid/objects/order)

  * The order created by the checkout.

    Depending on the payment provider, the order might not have been created when the [**Thank you** page](https://help.shopify.com/en/manual/orders/status-tracking) is first viewed. In this case, `nil` is returned.

    **Note:** The \<code>order\</code> object isn\&#39;t available on the \<strong>Thank you\</strong> page.

  * **order\_​id**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The ID of the order created by the checkout.

    The value is the same as [`order.id`](https://shopify.dev/docs/api/liquid/objects/order#order-id).

    Depending on the payment provider, the order might not have been created when the [**Order status** page](https://help.shopify.com/en/manual/orders/status-tracking) is first viewed. In this case, `nil` is returned.

  * **order\_​name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the order created by the checkout.

    The value is the same as [`order.name`](https://shopify.dev/docs/api/liquid/objects/order#order-name).

    Depending on the payment provider, the order might not have been created when the [**Order status** page](https://help.shopify.com/en/manual/orders/status-tracking) is first viewed. In this case, `nil` is returned.

  * **order\_​number**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * An integer representation of the name of the order created by the checkout.

    The value is the same as [`order.order_number`](https://shopify.dev/docs/api/liquid/objects/order#order-order_number).

    Depending on the payment provider, the order might not have been created when the [**Order status** page](https://help.shopify.com/en/manual/orders/status-tracking) is first viewed. In this case, `nil` is returned.

  * **requires\_​shipping**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if any of the line items of the checkout require shipping. Returns `false` if not.

  * **shipping\_​address**

    [address](https://shopify.dev/docs/api/liquid/objects/address)

  * The shipping address of the checkout.

  * **shipping\_​method**

    [shipping\_method](https://shopify.dev/docs/api/liquid/objects/shipping_method)

  * The shipping method of the checkout.

  * **shipping\_​price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The shipping price of the checkout in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **tax\_​lines**

    array of [tax\_line](https://shopify.dev/docs/api/liquid/objects/tax_line)

  * The tax lines for the checkout.

  * **tax\_​price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The total tax amount of the checkout in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **total\_​price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The total price of the checkout in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **transactions**

    array of [transaction](https://shopify.dev/docs/api/liquid/objects/transaction)

  * The transactions of the checkout.

## Deprecated Properties

* * **cancelled**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

    Deprecated

  * Returns `true` if the checkout has been cancelled. Returns `false` if not.

    **Deprecated:**

    Deprecated because `false` is always returned.

  * **discount**

    [discount](https://shopify.dev/docs/api/liquid/objects/discount)

    Deprecated

  * A discount applied to the checkout without being saved.

    **Deprecated:**

    Deprecated because an unsaved discount doesn't exist on the [**Order status** page](https://help.shopify.com/manual/orders/status-tracking).

  * **discounts**

    array of [discount](https://shopify.dev/docs/api/liquid/objects/discount)

    Deprecated

  * The discounts applied to the checkout.

    **Deprecated:**

    Deprecated because not all discount types and details are captured.

    The `checkout.discounts` property has been replaced by [`checkout.discount_applications`](https://shopify.dev/docs/api/liquid/objects/checkout#checkout-discount_applications).

  * **financial\_​status**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

    Deprecated

  * The financial status of the checkout.

    **Deprecated:**

    Deprecated because `nil` is always returned.

  * **fulfilled\_​at**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

    Deprecated

  * A timestamp for the fulfullment of the checkout.

    **Deprecated:**

    Deprecated because `nil` is always returned.

  * **fulfilled\_​line\_​items**

    array of [line\_item](https://shopify.dev/docs/api/liquid/objects/line_item)

    Deprecated

  * The fulfilled line items from the checkout.

    **Deprecated:**

    Deprecated because the array is always empty.

  * **fulfillment\_​status**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

    Deprecated

  * The fulfillment status of the checkout.

    **Deprecated:**

    Deprecated because `unfulfilled` is always returned.

  * **unavailable\_​line\_​items**

    array of [line\_item](https://shopify.dev/docs/api/liquid/objects/line_item)

    Deprecated

  * The unavailable line items of the checkout.

    **Deprecated:**

    Deprecated because the array is always empty.

  * **unfulfilled\_​line\_​items**

    array of [line\_item](https://shopify.dev/docs/api/liquid/objects/line_item)

    Deprecated

  * The unfulfilled line items of the checkout.

    **Deprecated:**

    Deprecated because the array is always the same as [`checkout.line_items`](https://shopify.dev/docs/api/liquid/objects/checkout#checkout-line_items).

##### Example

```json
{
  "applied_gift_cards": [],
  "attributes": {},
  "billing_address": {},
  "buyer_accepts_marketing": false,
  "cart_level_discount_applications": [],
  "currency": "CAD",
  "customer": {},
  "discount_applications": [],
  "discounts_amount": 4224,
  "discounts_savings": -4224,
  "email": "cornelius.potionmaker@gmail.com",
  "gift_cards_amount": 0,
  "id": 29944051400769,
  "line_items": [],
  "line_items_subtotal_price": 42249,
  "name": "#29944051400769",
  "note": null,
  "order": null,
  "order_id": null,
  "order_name": "#29944051400769",
  "order_number": "#29944051400769",
  "requires_shipping": true,
  "shipping_address": {},
  "shipping_method": {},
  "shipping_price": 0,
  "tax_lines": [],
  "tax_price": 0,
  "total_price": 38025,
  "transactions": []
}
```

## Templates using checkout

[Theme architecture](https://shopify.dev/themes/architecture/layouts/checkout-liquid)

[checkout template](https://shopify.dev/themes/architecture/layouts/checkout-liquid)
