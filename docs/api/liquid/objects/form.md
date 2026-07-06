---
title: 'Liquid objects: form'
description: >-
  Information about a form created by a [`form`
  tag](/docs/api/liquid/tags/form).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/form'
  md: 'https://shopify.dev/docs/api/liquid/objects/form.md'
api_name: liquid
---

# form

Information about a form created by a [`form` tag](https://shopify.dev/docs/api/liquid/tags/form).

## Properties

* * **address1**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The first address line associated with the address.

    This property is exclusive to the [`customer_address` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address).

  * **address2**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The second address line associated with the address.

    This property is exclusive to the [`customer_address` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address).

  * **author**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the author of the article comment.

    This property is exclusive to the [`new_comment` form](https://shopify.dev/docs/api/liquid/tags/form#form-new_comment).

  * **body**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The content of the contact submission or article comment.

    This property is exclusive to the [`contact`](https://shopify.dev/docs/api/liquid/tags/form#form-contact) and [`new_comment`](https://shopify.dev/docs/api/liquid/tags/form#form-new_comment) forms.

  * **city**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The city associated with the address.

    This property is exclusive to the [`customer_address` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address).

  * **company**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The company associated with the address.

    This property is exclusive to the [`customer_address` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address).

  * **country**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The country associated with the address.

    This property is exclusive to the [`customer_address` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address).

  * **email**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The email associated with the form.

    This property is exclusive to the following forms:

    * [`contact`](https://shopify.dev/docs/api/liquid/tags/form#form-contact)
    * [`create_customer`](https://shopify.dev/docs/api/liquid/tags/form#form-create_customer)
    * [`customer`](https://shopify.dev/docs/api/liquid/tags/form#form-customer)
    * [`customer_login`](https://shopify.dev/docs/api/liquid/tags/form#form-customer_login)
    * [`new_comment`](https://shopify.dev/docs/api/liquid/tags/form#form-new_comment)
    * [`recover_customer_password`](https://shopify.dev/docs/api/liquid/tags/form#form-recover_customer_password)
    * [`product`](https://shopify.dev/docs/api/liquid/tags/form#form-product)

  * **errors**

    [form\_errors](https://shopify.dev/docs/api/liquid/objects/form_errors)

  * Any errors from the form.

    If there are no errors, then `nil` is returned.

    **Tip:** You can apply the \<a href="/docs/api/liquid/filters/default\_errors">\<code>\<span class="PreventFireFoxApplyingGapToWBR">default\<wbr/>\_errors\</span>\</code> filter\</a> to \<code>form.errors\</code> to output default error messages without having to loop through the array.

  * **first\_​name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The first name associated with the customer or address.

    This property is exclusive to the [`create_customer`](https://shopify.dev/docs/api/liquid/tags/form#form-create_customer) and [`customer_address`](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address) forms.

  * **id**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The ID of the form.

  * **last\_​name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The last name associated with the customer or address.

    This property is exclusive to the [`create_customer`](https://shopify.dev/docs/api/liquid/tags/form#form-create_customer) and [`customer_address`](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address) forms.

  * **message**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The personalized message intended for the recipient.

    This property is exclusive to the [`product` form](https://shopify.dev/docs/api/liquid/tags/form#form-product).

  * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The nickname of the gift card recipient.

    This property is exclusive to the [`product` form](https://shopify.dev/docs/api/liquid/tags/form#form-product).

  * **password\_​needed**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true`.

    This property is exclusive to the [`customer_login` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_login).

  * **phone**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The phone number associated with the address.

    This property is exclusive to the [`customer_address` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address).

  * **posted\_​successfully?**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the form was submitted successfully. Returns `false` if there were errors.

    **Note:** The \<a href="/docs/api/liquid/tags/form#form-customer\_address">\<code>\<span class="PreventFireFoxApplyingGapToWBR">customer\<wbr/>\_address\</span>\</code> form\</a> always returns \<code>true\</code>.

  * **province**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The province associated with the address.

    This property is exclusive to the [`customer_address` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address).

  * **set\_​as\_​default\_​checkbox**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * Renders an HTML checkbox that can submit the address as the customer's default address.

    This property is exclusive to the [`customer_address` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address).

  * **zip**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The zip or postal code associated with the address.

    This property is exclusive to the [`customer_address` form](https://shopify.dev/docs/api/liquid/tags/form#form-customer_address).

##### Example

```json
{
  "address1": "12 Phoenix Feather Alley",
  "address2": "1",
  "author": null,
  "body": null,
  "city": "Calgary",
  "company": null,
  "country": "Canada",
  "email": null,
  "errors": null,
  "first_name": "Cornelius",
  "id": "new",
  "last_name": "Potionmaker",
  "password_needed?": false,
  "phone": "44 131 496 0905",
  "posted_successfully?": true,
  "province": "Alberta",
  "set_as_default_checkbox": "<input type='checkbox' id='address_default_address_new' name='address[default]' value='1'>",
  "zip": "T1X 0L4"
}
```
