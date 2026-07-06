---
title: 'Liquid objects: order'
description: 'An [order](https://help.shopify.com/manual/orders).'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/order'
  md: 'https://shopify.dev/docs/api/liquid/objects/order.md'
api_name: liquid
---

# order

An [order](https://help.shopify.com/manual/orders).

## Properties

* * **attributes**

  * The attributes on the order.

    If there are no attributes on the order, then `nil` is returned.

    **Tip:** Attributes are \<a href="https://shopify.dev/themes/architecture/templates/cart#support-cart-notes-and-attributes">collected with the cart\</a>.

    ExampleOutput the attributes

    ```liquid
    <ul>
      {% for attribute in order.attributes -%}
        <li><strong>{{ attribute.first }}:</strong> {{ attribute.last }}</li>
      {%- endfor %}
    </ul>
    ```

  * **billing\_​address**

    [address](https://shopify.dev/docs/api/liquid/objects/address)

  * The billing address of the order.

  * **cancel\_​reason**

    [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values

  * The reason that the order was cancelled.

    | Possible values | Description |
    | - | - |
    | customer | Customer changed/cancelled order |
    | declined | Payment declined |
    | fraud | Fraudulent order |
    | inventory | Items unavailable |
    | staff | Staff error |
    | other | Other |

  * **cancel\_​reason\_​label**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The localized version of the [cancellation reason](https://shopify.dev/docs/api/liquid/objects/order#order-cancel_reason) for the order.

    **Tip:** Use this property to output the cancellation reason on the storefront.

  * **cancelled**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the order was cancelled. Returns `false` if not.

  * **cancelled\_​at**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A timestamp for when the order was cancelled.

    **Tip:** Use the \<a href="/docs/api/liquid/filters/date">\<code>date\</code> filter\</a> to format the timestamp.

  * **cart\_​level\_​discount\_​applications**

    array of [discount\_application](https://shopify.dev/docs/api/liquid/objects/discount_application)

  * The discount applications that apply at the order level.

  * **confirmation\_​number**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A randomly generated alpha-numeric identifier for the order that may be shown to the customer instead of the sequential order name. For example, "XPAV284CT", "R50KELTJP" or "35PKUN0UJ". This value isn't guaranteed to be unique.

  * **created\_​at**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A timestamp for when the order was created.

    **Tip:** Use the \<a href="/docs/api/liquid/filters/date">\<code>date\</code> filter\</a> to format the timestamp.

  * **customer**

    [customer](https://shopify.dev/docs/api/liquid/objects/customer)

  * The customer that placed the order.

  * **customer\_​order\_​url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The URL for the new order details page.

    Customer accounts includes a list of Buyers Orders and an Order Details View. This liquid function exposes a URL to a specific Orders Details in customer accounts. [Setup process for the new order details page](https://help.shopify.com/en/manual/customers/customer-accounts/new-customer-accounts) can be found in the help center.

  * **customer\_​url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The URL for the customer to view the order in their account.

  * **discount\_​applications**

    array of [discount\_application](https://shopify.dev/docs/api/liquid/objects/discount_application)

  * All of the discount applications for the order and its line items.

  * **email**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The email that's associated with the order.

    If no email is associated with the order, then `nil` is returned.

  * **financial\_​status**

    [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values

  * The order's financial status.

    | Possible values |
    | - |
    | authorized |
    | expired |
    | paid |
    | partially\_paid |
    | partially\_refunded |
    | pending |
    | refunded |
    | unpaid |
    | voided |

  * **financial\_​status\_​label**

  * The localized version of the [financial status](https://shopify.dev/docs/api/liquid/objects/order#order-financial_status) of the order.

    **Tip:** Use this property to output the financial status on the storefront.

  * **fulfillment\_​status**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The fulfillment status of the order.

  * **fulfillment\_​status\_​label**

    [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values

  * The localized version of the [fulfillment status](https://shopify.dev/docs/api/liquid/objects/order#order-fulfillment_status) of the order.

    **Tip:** Use this property to output the fulfillment status on the storefront.

    | Possible values |
    | - |
    | complete |
    | fulfilled |
    | partial |
    | restocked |
    | unfulfilled |

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the order.

  * **item\_​count**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The number of items in the order.

  * **line\_​items**

    array of [line\_item](https://shopify.dev/docs/api/liquid/objects/line_item)

  * The line items in the order.

  * **line\_​items\_​subtotal\_​price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The sum of the prices of all of the line items in the order in the currency's subunit, after any line item discounts have been applied.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **metafields**

  * The [metafields](https://shopify.dev/docs/api/liquid/objects/metafield) applied to the order.

    **Tip:** To learn about how to create metafields, refer to \<a href="/apps/metafields/manage">Create and manage metafields\</a> or visit the \<a href="https://help.shopify.com/manual/metafields">Shopify Help Center\</a>.

  * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the order.

  * **note**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The note on the order.

    If there's no note on the order, then `nil` is returned.

    **Tip:** Notes are \<a href="https://shopify.dev/themes/architecture/templates/cart#support-cart-notes-and-attributes">collected with the cart\</a>.

  * **order\_​number**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The integer representation of the order [name](https://shopify.dev/docs/api/liquid/objects/order#order-name).

  * **order\_​status\_​url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The URL for the [**Order status** page](https://help.shopify.com/manual/orders/status-tracking) for the order.

  * **phone**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The phone number associated with the order.

  * **pickup\_​in\_​store?**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the order is a store pickup order.

  * **shipping\_​address**

    [address](https://shopify.dev/docs/api/liquid/objects/address)

  * The shipping address of the order.

  * **shipping\_​methods**

    array of [shipping\_method](https://shopify.dev/docs/api/liquid/objects/shipping_method)

  * The shipping methods for the order.

  * **shipping\_​price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The shipping price of the order in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **subtotal\_​line\_​items**

    array of [line\_item](https://shopify.dev/docs/api/liquid/objects/line_item)

  * The non-tip line items in the order.

    **Note:** These line items are used to calculate the the \<a href="/docs/api/liquid/objects/order#order-subtotal\_price">subtotal price\</a>.

  * **subtotal\_​price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The sum of the prices of the [subtotal line items](https://shopify.dev/docs/api/liquid/objects/order#order-subtotal_line_items) in the currency's subunit, after any line item or cart discounts have been applied.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **tags**

    array of [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The [tags](https://help.shopify.com/manual/shopify-admin/productivity-tools/using-tags) on the order.

    The tags are returned in alphabetical order.

  * **tax\_​lines**

    array of [tax\_line](https://shopify.dev/docs/api/liquid/objects/tax_line)

  * The tax lines on the order.

  * **tax\_​price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The total amount of taxes applied to the order in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **total\_​discounts**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The total amount of all discounts applied to the order in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **total\_​duties**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The sum of all duties applied to the line items in the order in the currency's subunit.

    If there are no duties, then `nil` is returned. The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **total\_​net\_​amount**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The net amount of the order in the currency's subunit.

    The amount is calculated after refunds are applied, so is equal to `order.total_price` minus `order.total_refunded_amount`.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **total\_​price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The total price of the order in the currency's subunit.

    **Note:** The total price is calculated before refunds are applied. Use \<a href="/docs/api/liquid/objects/order#order-total\_net\_amount">\<code>\<span class="PreventFireFoxApplyingGapToWBR">order.total\<wbr/>\_net\<wbr/>\_amount\</span>\</code>\</a> to output the total minus any refunds.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **total\_​refunded\_​amount**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The total amount that's been refunded from the order in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **transactions**

    array of [transaction](https://shopify.dev/docs/api/liquid/objects/transaction)

  * The transactions of the order.

## Deprecated Properties

* * **discounts**

    [discount](https://shopify.dev/docs/api/liquid/objects/discount)

    Deprecated

  * The discounts on the order.

    **Deprecated:**

    Deprecated because not all discount types and details are captured.

    The `order.discounts` property has been replaced by [`order.discount_applications`](https://shopify.dev/docs/api/liquid/objects/order#order-discount_applications).

##### Example

```json
{
  "attributes": {},
  "billing_address": {},
  "cancel_reason": null,
  "cancel_reason_label": null,
  "cancelled": false,
  "cancelled_at": null,
  "cart_level_discount_applications": [],
  "confirmation_number": "0YMJHPM8U",
  "created_at": "2022-04-29 11:15:46 -0400",
  "customer": {},
  "customer_order_url": "https://shopify.com/56174706753/account/orders/4295688749121?locale=en&region_country=CA&buyer_flags=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwb2xpbmFzLXBvdGVudC1wb3Rpb25zLm15c2hvcGlmeS5jb20iLCJmbGFncyI6W10sImV4cCI6MTc4MzM0ODY2MiwibmJmIjoxNzgyNzQzODYyfQ.qKYjt8xHtqb-cp71IfrMzwK21DiWrRmCFanN-AfY1KQ",
  "customer_url": "https://polinas-potent-potions.myshopify.com/account/orders/8be02e56c658bcd1f034d28c496fddd9",
  "discount_applications": [],
  "discounts": null,
  "email": "cornelius.potionmaker@gmail.com",
  "financial_status": "paid",
  "financial_status_label": "Paid",
  "fulfillment_status": "partial",
  "fulfillment_status_label": "Partial",
  "id": 4295688749121,
  "item_count": 6,
  "line_items": [],
  "line_items_subtotal_price": "492.93",
  "metafields": {},
  "name": "#1001",
  "note": null,
  "order_number": 1001,
  "order_status_url": "https://polinas-potent-potions.myshopify.com/56174706753/orders/8be02e56c658bcd1f034d28c496fddd9/authenticate?key=4f9baf2b8ebd0f75ec73eb9bac6e4519",
  "phone": null,
  "pickup_in_store?": false,
  "shipping_address": {},
  "shipping_methods": [],
  "shipping_price": "0.00",
  "subtotal_line_items": [],
  "subtotal_price": "492.93",
  "tags": [],
  "tax_lines": [],
  "tax_price": "0.00",
  "total_discounts": "0.00",
  "total_duties": null,
  "total_net_amount": "492.93",
  "total_price": "492.93",
  "total_refunded_amount": "0.00",
  "transactions": []
}
```

## Templates using order

[Theme architecture](https://shopify.dev/themes/architecture/templates/customers-order)

[customers/order template](https://shopify.dev/themes/architecture/templates/customers-order)
