---
title: 'Liquid objects: customer'
description: 'A [customer](https://help.shopify.com/manual/customers) of the store.'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/customer'
  md: 'https://shopify.dev/docs/api/liquid/objects/customer.md'
api_name: liquid
---

# customer

A [customer](https://help.shopify.com/manual/customers) of the store.

The `customer` object is directly accessible globally when a customer is logged in to their account. It's also defined in the following contexts:

* The [`customers/account` template](https://shopify.dev/themes/architecture/templates/customers-account)
* The [`customers/addresses` template](https://shopify.dev/themes/architecture/templates/customers-addresses)
* The [`customers/order` template](https://shopify.dev/themes/architecture/templates/customers-order)
* When accessing [`checkout.customer`](https://shopify.dev/docs/api/liquid/objects/checkout#checkout-customer)
* When accessing [`gift_card.customer`](https://shopify.dev/docs/api/liquid/objects/gift_card#gift_card-customer)
* When accessing [`order.customer`](https://shopify.dev/docs/api/liquid/objects/order#order-customer)

Outside of the above contexts, if the customer isn't logged into their account, the `customer` object returns `nil`.

## Properties

* * **accepts\_​marketing**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the customer accepts marketing. Returns `false` if not.

  * **addresses**

    array of [address](https://shopify.dev/docs/api/liquid/objects/address)

  * All of the addresses associated with the customer.

    **Tip:** Use the \<a href="/docs/api/liquid/tags/paginate">paginate\</a> tag to choose how many addresses to show at once, up to a limit of 20.

  * **addresses\_​count**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The number of addresses associated with the customer.

  * **b2b?**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the customer is a B2B customer. Returns `false` if not.

    To learn about B2B in themes, refer to [Support B2B customers in your theme](https://shopify.dev/themes/pricing-payments/b2b).

  * **company\_​available\_​locations**

    array of [company\_location](https://shopify.dev/docs/api/liquid/objects/company_location)

  * The company locations that the customer has access to, or can interact with.

    To learn about B2B in themes, refer to [Support B2B customers in your theme](https://shopify.dev/themes/pricing-payments/b2b).

    **Tip:** Use the \<a href="/docs/api/liquid/tags/paginate">paginate\</a> tag to choose how many company locations to show at once, up to a limit of 100.

  * **company\_​available\_​locations\_​count**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The number of company locations associated with the customer.

  * **current\_​company**

    [company](https://shopify.dev/docs/api/liquid/objects/company)

  * The company that the customer is purchasing for.

    To learn about B2B in themes, refer to [Support B2B customers in your theme](https://shopify.dev/themes/pricing-payments/b2b).

  * **current\_​location**

    [company\_location](https://shopify.dev/docs/api/liquid/objects/company_location)

  * The currently selected company location.

    To learn about B2B in themes, refer to [Support B2B customers in your theme](https://shopify.dev/themes/pricing-payments/b2b).

  * **default\_​address**

    [address](https://shopify.dev/docs/api/liquid/objects/address)

  * The default address of the customer.

  * **email**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The email of the customer.

  * **first\_​name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The first name of the customer.

  * **has\_​account**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the email associated with the customer is tied to a [customer account](https://help.shopify.com/manual/customers/customer-accounts). Returns `false` if not.

    A customer can complete a checkout without making an account with the store. If the customer doesn't have an account with the store, then `customer.has_account` is `false` at checkout.

    During the checkout process, if the customer has an account with the store and enters an email associated with an account, then `customer.has_account` is `true`. The email is associated with the account regardless of whether the customer has logged into their account.

  * **has\_​avatar?**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if an avatar is associated with a customer. Returns `false` if not.

    A customer may have an avatar associated with their account, which can be displayed in the storefront.

    **Tip:** Use with the \<a href="/docs/api/liquid/filters/avatar">\<code>avatar\</code>\</a> filter to render the customer\&#39;s avatar.

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the customer.

  * **last\_​name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The last name of the customer.

  * **last\_​order**

    [order](https://shopify.dev/docs/api/liquid/objects/order)

  * The last order placed by the customer, not including test orders.

  * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The full name of the customer.

  * **orders**

    array of [order](https://shopify.dev/docs/api/liquid/objects/order)

  * All of the orders placed by the customer.

    **Tip:** Use the \<a href="/docs/api/liquid/tags/paginate">paginate\</a> tag to choose how many orders to show at once, up to a limit of 20.

  * **orders\_​count**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The total number of orders that the customer has placed.

  * **payment\_​methods**

    array of [customer\_payment\_method](https://shopify.dev/docs/api/liquid/objects/customer_payment_method)

  * The customer's saved payment methods.

  * **phone**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The phone number of the customer.

    This phone number is only populated if the customer checks out using a phone number during checkout, opts in to SMS notifications, or if the merchant has manually entered it.

  * **store\_​credit\_​account**

    [store\_credit\_account](https://shopify.dev/docs/api/liquid/objects/store_credit_account)

  * The store credit account associated with the customer.

    The account shown will be in the currency associated with the customer’s current context. For example, if a customer is browsing the storefront in the US market, their USD store credit account will be returned. If they do not have a USD store credit account `nil` will be returned.

  * **tags**

    array of [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The tags associated with the customer.

  * **tax\_​exempt**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the customer is exempt from taxes. Returns `false` if not.

  * **total\_​spent**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The total amount that the customer has spent on all orders in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

##### Example

```json
{
  "accepts_marketing": true,
  "addresses": [],
  "addresses_count": 5,
  "b2b?": false,
  "company_available_locations": [],
  "company_available_locations_count": 1,
  "current_company": {},
  "current_location": null,
  "default_address": {},
  "email": "cornelius.potionmaker@gmail.com",
  "first_name": "Cornelius",
  "has_account": true,
  "has_avatar?": false,
  "id": 5625411010625,
  "last_name": "Potionmaker",
  "last_order": {},
  "name": "Cornelius Potionmaker",
  "orders": [],
  "orders_count": 1,
  "payment_methods": [],
  "phone": "+441314960905",
  "store_credit_account": {},
  "tags": [
    "newsletter"
  ],
  "tax_exempt": false,
  "total_spent": "56.00"
}
```

### Check whether the `customer` object is defined

When using the `customer` object outside of customer-specific templates or objects that specifically return a customer, you should check whether the `customer` object is defined.

##### Code

```liquid
{% if customer %}
  Hello, {{ customer.first_name }}!
{% endif %}
```

##### Data

```json
{
  "customer": {
    "first_name": "Cornelius"
  }
}
```

##### Output

```html
Hello, Cornelius!
```

## Templates using customer

[Theme architecture](https://shopify.dev/themes/architecture/templates/customers-account)

[customers/account template](https://shopify.dev/themes/architecture/templates/customers-account)

[Theme architecture](https://shopify.dev/themes/architecture/templates/customers-addresses)

[customers/addresses template](https://shopify.dev/themes/architecture/templates/customers-addresses)

[Theme architecture](https://shopify.dev/themes/architecture/templates/customers-order)

[customers/order template](https://shopify.dev/themes/architecture/templates/customers-order)
