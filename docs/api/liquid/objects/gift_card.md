---
title: 'Liquid objects: gift_card'
description: >-
  A [gift card](https://help.shopify.com/manual/products/gift-card-products)
  that's been issued to a customer or a recipient.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/gift_card'
  md: 'https://shopify.dev/docs/api/liquid/objects/gift_card.md'
api_name: liquid
---

# gift\_​card

A [gift card](https://help.shopify.com/manual/products/gift-card-products) that's been issued to a customer or a recipient.

## Properties

* * **balance**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The remaining balance of the gift card in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **code**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The code used to redeem the gift card.

  * **currency**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The [ISO code](https://www.iso.org/iso-4217-currency-codes.html) of the currency that the gift card was issued in.

  * **customer**

    [customer](https://shopify.dev/docs/api/liquid/objects/customer)

  * The customer associated with the gift card.

  * **enabled**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the gift card is enabled. Returns `false` if not.

  * **expired**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the gift card is expired. Returns `false` if not.

  * **expires\_​on**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A timestamp for when the gift card expires.

    If the gift card never expires, then `nil` is returned.

    **Tip:** Use the \<a href="/docs/api/liquid/filters/date">\<code>date\</code> filter\</a> to format the timestamp.

  * **initial\_​value**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The initial balance of the gift card in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **last\_​four\_​characters**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The last 4 characters of the code used to redeem the gift card.

  * **message**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The personalized message intended for the recipient.

    If there is no message intended for the recipient, then `nil` is returned.

  * **pass\_​url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The URL to download the gift card as an Apple Wallet Pass.

  * **product**

    [product](https://shopify.dev/docs/api/liquid/objects/product)

  * The product associated with the gift card.

  * **properties**

  * The [line item properties](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-properties) assigned to the gift card.

    If there aren't any line item properties, then an [`EmptyDrop`](https://shopify.dev/docs/api/liquid/basics#emptydrop) is returned.

  * **qr\_​identifier**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A string used to generate a QR code for the gift card.

  * **recipient**

    [recipient](https://shopify.dev/docs/api/liquid/objects/recipient)

  * The recipient associated with the gift card.

    If there is no recipient associated with the gift card, then `nil` is returned.

  * **send\_​on**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The scheduled date on which the gift card will be sent to the recipient.

    If the gift card does not have a scheduled date, then `nil` is returned.

    **Tip:** Use the \<a href="/docs/api/liquid/filters/date">\<code>date\</code> filter\</a> to format the date.

  * **template\_​suffix**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the [custom template](https://shopify.dev/themes/architecture/templates#alternate-templates) assigned to the gift card.

    The name doesn't include the `gift_card.` prefix, or the `.liquid` file extension.

    If a custom template isn't assigned to the gift card, then `nil` is returned.

  * **url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The URL to view the gift card. This URL is on the `checkout.shopify.com` domain.

    **Tip:** The page at this URL is rendered through the \<a href="/themes/architecture/templates/gift-card-liquid">\<code>\<span class="PreventFireFoxApplyingGapToWBR">gift\<wbr/>\_card.liquid\</span>\</code> template\</a> of the theme.

  * **variant**

    [variant](https://shopify.dev/docs/api/liquid/objects/variant)

  * The variant associated with the gift card.

    If there is no variant associated with the gift card, then `nil` is returned.

##### Example

```json
{
  "balance": 5000,
  "code": "WCGX 7X97 K9HJ DFR8",
  "currency": "CAD",
  "customer": {},
  "enabled": true,
  "expired": false,
  "expires_on": null,
  "initial_value": 5000,
  "last_four_characters": "DFR8",
  "message": null,
  "send_on": null,
  "pass_url": "https://polinas-potent-potions.myshopify.com/v1/passes/pass.com.shopify.giftcardnext/94af7fbe55d010130df8d8bc4a338d36/",
  "product": {},
  "variant": {},
  "properties": {},
  "qr_identifier": "shopify-giftcard-v1-3TKWJKJBM3X7PBRK",
  "recipient": null,
  "template_suffix": null,
  "url": "https://checkout.shopify.com/gift_cards/56174706753/0011c591fc720d0a51b80cdb694f969e"
}
```

## Templates using gift\_card

[Theme architecture](https://shopify.dev/themes/architecture/templates/gift-card-liquid)

[gift\_card.liquid template](https://shopify.dev/themes/architecture/templates/gift-card-liquid)
