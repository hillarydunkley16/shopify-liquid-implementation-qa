---
title: 'Liquid objects: shop'
description: >-
  Information about the store, such as the store address, the total number of
  products, and various settings.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/shop'
  md: 'https://shopify.dev/docs/api/liquid/objects/shop.md'
api_name: liquid
---

# shop

Information about the store, such as the store address, the total number of products, and various settings.

## Properties

* * **accepts\_​gift\_​cards**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the store accepts gift cards. Returns `false` if not.

  * **address**

    [address](https://shopify.dev/docs/api/liquid/objects/address)

  * The address of the store.

  * **brand**

    [brand](https://shopify.dev/docs/api/liquid/objects/brand)

  * The [brand assets](https://help.shopify.com/manual/promoting-marketing/managing-brand-assets) for the store.

  * **collections\_​count**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The number of collections in the store.

  * **currency**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The currency of the store.

  * **customer\_​accounts\_​enabled**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the store shows a login link. Returns `false` if not.

  * **customer\_​accounts\_​optional**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if customer accounts are optional to complete checkout. Returns `false` if not.

  * **description**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The [description](https://help.shopify.com/manual/online-store/setting-up/preferences#edit-the-title-and-meta-description) of the store.

  * **domain**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The primary domain of the store.

  * **email**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The [sender email](https://help.shopify.com/manual/intro-to-shopify/initial-setup/setup-your-email#change-your-sender-email-address) of the store.

  * **enabled\_​currencies**

    array of [currency](https://shopify.dev/docs/api/liquid/objects/currency)

  * The currencies that the store accepts.

    **Tip:** You can get the store\&#39;s currency with \<a href="/docs/api/liquid/objects/shop#shop-currency">\<code>shop.currency\</code>\</a>.

  * **enabled\_​payment\_​types**

    array of [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The accepted payment types on the store.

    The payment types are based on the store's enabled [payment providers](https://help.shopify.com/manual/payments) and the customer's current region and currency.

    **Tip:** You can output an \<code>svg\</code> logo for each payment type with the \<a href="/docs/api/liquid/filters/payment\_type\_svg\_tag">\<code>\<span class="PreventFireFoxApplyingGapToWBR">payment\<wbr/>\_type\<wbr/>\_svg\<wbr/>\_tag\</span>\</code> filter\</a>. Alternatively, you can get the source URL for each \<code>svg\</code> with the \<a href="/docs/api/liquid/filters/payment\_type\_img\_url">\<code>\<span class="PreventFireFoxApplyingGapToWBR">payment\<wbr/>\_type\<wbr/>\_img\<wbr/>\_url\</span>\</code> filter\</a>.

  * **id**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The ID of the store.

  * **metafields**

  * The [metafields](https://shopify.dev/docs/api/liquid/objects/metafield) applied to the store.

    **Tip:** To learn about how to create metafields, refer to \<a href="/apps/metafields/manage">Create and manage metafields\</a> or visit the \<a href="https://help.shopify.com/manual/metafields">Shopify Help Center\</a>.

  * **money\_​format**

    [currency](https://shopify.dev/docs/api/liquid/objects/currency)

  * The money format of the store.

  * **money\_​with\_​currency\_​format**

    [currency](https://shopify.dev/docs/api/liquid/objects/currency)

  * The money format of the store with the currency included.

  * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the store.

  * **password\_​message**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The password page message of the store.

  * **permanent\_​domain**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The `.myshopify.com` domain of the store.

  * **phone**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The phone number of the store.

  * **policies**

    array of [policy](https://shopify.dev/docs/api/liquid/objects/policy)

  * The policies for the store.

    The policies are set in the store's [Policies settings](https://www.shopify.com/admin/settings/legal).

    ExampleOutput the policies

    ##### Code

    ```liquid
    <ul>
    {%- for policy in shop.policies %}
      <li>{{ policy.title }}</li>
    {%- endfor %}
    </ul>
    ```

    ##### Data

    ```json
    {
      "shop": {
        "policies": [
          "<p>We have a 30-day return policy, which means you have 30 days after receiving your item to request a return. ...</p>",
          "<p>This Privacy Policy describes how polinas-potent-potions.myshopify.com (the “Site” or “we”) collects, uses, and discloses your Personal Information when you visit or make a purchase from the Site. ...</p>",
          "<strong>OVERVIEW</strong> <br> This website is operated by Polina's Potent Potions. Throughout the site, the terms “we”, “us” and “our” refer to Polina's Potent Potions. ...",
          "<meta charset=\"utf-8\">\n<p data-mce-fragment=\"1\">All orders are processed within X to X business days (excluding weekends and holidays) after receiving your order confirmation email. You will receive another notification when your order has shipped. ...&nbsp;</p>\n<h3 data-mce-fragment=\"1\"></h3>"
        ]
      }
    }
    ```

    ##### Output

    ```html
    <ul>
      <li>Refund policy</li>
      <li>Privacy policy</li>
      <li>Terms of service</li>
      <li>Shipping policy</li>
    </ul>
    ```

  * **privacy\_​policy**

    [policy](https://shopify.dev/docs/api/liquid/objects/policy)

  * The privacy policy for the store.

  * **products\_​count**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The number of products in the store.

  * **published\_​locales**

    array of [shop\_locale](https://shopify.dev/docs/api/liquid/objects/shop_locale)

  * The locales (languages) that are published on the store.

  * **refund\_​policy**

    [policy](https://shopify.dev/docs/api/liquid/objects/policy)

  * The refund policy for the store.

  * **search\_​types**

    array of [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The resource types searched for by default when no `type` parameter is specified.

    Search types are `["article", "page", "product"]` by default, and can be configured in the Search & Discovery app. These search types are used when a search query is performed without a `?type=` parameter.

    **Tip:** A search with a \<code>?type=\</code> parameter value not in the \<code>\<span class="PreventFireFoxApplyingGapToWBR">shop.search\<wbr/>\_types\</span>\</code> list will still return results for the specified type, if they exist.

  * **secure\_​url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The full URL of the store, with an `https` protocol.

  * **shipping\_​policy**

    [policy](https://shopify.dev/docs/api/liquid/objects/policy)

  * The shipping policy for the store.

  * **subscription\_​policy**

    [policy](https://shopify.dev/docs/api/liquid/objects/policy)

  * The subscription policy for the store.

  * **terms\_​of\_​service**

    [policy](https://shopify.dev/docs/api/liquid/objects/policy)

  * The terms of service for the store.

  * **types**

    array of [string](https://shopify.dev/docs/api/liquid/basics#string)

  * All of the product types in the store.

    ExampleOutput the product types

    ##### Code

    ```liquid
    {% for type in shop.types %}
      {{- type | link_to_type }}
    {% endfor %}
    ```

    ##### Data

    ```json
    {
      "shop": {
        "types": [
          "",
          "Animals & Pet Supplies",
          "Baking Flavors & Extracts",
          "Container",
          "Cooking & Baking Ingredients",
          "Dried Flowers",
          "Fruits & Vegetables",
          "Gift Cards",
          "Health",
          "Health & Beauty",
          "Invisibility",
          "Love",
          "Music & Sound Recordings",
          "Seasonings & Spices",
          "Water"
        ]
      }
    }
    ```

    ##### Output

    ```html
    Unknown Type

    <a href="/collections/types?q=Animals%20%26%20Pet%20Supplies" title="Animals &amp; Pet Supplies">Animals & Pet Supplies</a>

    <a href="/collections/types?q=Baking%20Flavors%20%26%20Extracts" title="Baking Flavors &amp; Extracts">Baking Flavors & Extracts</a>

    <a href="/collections/types?q=Container" title="Container">Container</a>

    <a href="/collections/types?q=Cooking%20%26%20Baking%20Ingredients" title="Cooking &amp; Baking Ingredients">Cooking & Baking Ingredients</a>

    <a href="/collections/types?q=Dried%20Flowers" title="Dried Flowers">Dried Flowers</a>

    <a href="/collections/types?q=Fruits%20%26%20Vegetables" title="Fruits &amp; Vegetables">Fruits & Vegetables</a>

    <a href="/collections/types?q=Gift%20Cards" title="Gift Cards">Gift Cards</a>

    <a href="/collections/types?q=Health" title="Health">Health</a>

    <a href="/collections/types?q=Health%20%26%20Beauty" title="Health &amp; Beauty">Health & Beauty</a>

    <a href="/collections/types?q=Invisibility" title="Invisibility">Invisibility</a>

    <a href="/collections/types?q=Love" title="Love">Love</a>

    <a href="/collections/types?q=Music%20%26%20Sound%20Recordings" title="Music &amp; Sound Recordings">Music & Sound Recordings</a>

    <a href="/collections/types?q=Seasonings%20%26%20Spices" title="Seasonings &amp; Spices">Seasonings & Spices</a>

    <a href="/collections/types?q=Water" title="Water">Water</a>
    ```

  * **url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The full URL of the store.

  * **vendors**

    array of [string](https://shopify.dev/docs/api/liquid/basics#string)

  * All of the product vendors for the store.

    ExampleOutput the vendors

    ##### Code

    ```liquid
    {% for vendor in shop.vendors %}
      {{- vendor | link_to_vendor }}
    {% endfor %}
    ```

    ##### Data

    ```json
    {
      "shop": {
        "vendors": [
          "Clover's Apothecary",
          "Polina's Potent Potions",
          "Ted's Apothecary Supply"
        ]
      }
    }
    ```

    ##### Output

    ```html
    <a href="/collections/vendors?q=Clover%27s%20Apothecary" title="Clover&#39;s Apothecary">Clover's Apothecary</a>

    <a href="/collections/vendors?q=Polina%27s%20Potent%20Potions" title="Polina&#39;s Potent Potions">Polina's Potent Potions</a>

    <a href="/collections/vendors?q=Ted%27s%20Apothecary%20Supply" title="Ted&#39;s Apothecary Supply">Ted's Apothecary Supply</a>
    ```

## Deprecated Properties

* * **enabled\_​locales**

    array of [shop\_locale](https://shopify.dev/docs/api/liquid/objects/shop_locale)

    Deprecated

  * The locales (languages) that are published on the store.

    **Deprecated:**

    Deprecated because the name didn't make it clear that the returned locales were published.

    The `shop.enabled_locales` property has been replaced by [`shop.published_locales`](https://shopify.dev/docs/api/liquid/objects/shop#shop-published_locales).

  * **locale**

    [shop\_locale](https://shopify.dev/docs/api/liquid/objects/shop_locale)

    Deprecated

  * The currently active locale (language).

    **Deprecated:**

    Deprecated because this value is contextual to the request and not a property of the shop resource.

    The `shop.locale` property has been replaced by [request.locale](https://shopify.dev/docs/api/liquid/objects/request#request-locale).

  * **metaobjects**

    Deprecated

  * All of the [metaobjects](https://shopify.dev/docs/api/liquid/objects/metaobject) of the store.

    **Deprecated:**

    The `shop.metaobjects` property has been replaced by [`metaobjects`](https://shopify.dev/docs/api/liquid/objects/metaobjects).

  * **taxes\_​included**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

    Deprecated

  * Returns `true` if prices include taxes. Returns `false` if not.

    **Deprecated:**

    Deprecated because whether or not prices have taxes included is dependent on the customer's country.

    The `shop.taxes_included` property has been replaced by [cart.taxes\_included](https://shopify.dev/docs/api/liquid/objects/cart#cart-taxes_included).

##### Example

```json
{
  "accepts_gift_cards": true,
  "address": {},
  "brand": {},
  "collections_count": 7,
  "currency": "CAD",
  "customer_accounts_enabled": true,
  "customer_accounts_optional": true,
  "description": "Canada's foremost retailer for potions and potion accessories. Try one of our award-winning artisanal potions, or find the supplies to make your own!",
  "domain": "polinas-potent-potions.myshopify.com",
  "email": "polinas.potent.potions@gmail.com",
  "enabled_currencies": [],
  "enabled_locales": [],
  "enabled_payment_types": [
    "visa",
    "master",
    "american_express",
    "paypal",
    "diners_club",
    "discover"
  ],
  "id": 56174706753,
  "locale": "en",
  "metafields": {},
  "metaobjects": {},
  "money_format": "${{amount}}",
  "money_with_currency_format": "${{amount}} CAD",
  "name": "Polina&#39;s Potent Potions",
  "password_message": "Our store will be opening when the moon is in the seventh house!!",
  "permanent_domain": "polinas-potent-potions.myshopify.com",
  "phone": "416-123-1234",
  "policies": [],
  "privacy_policy": {},
  "products_count": 19,
  "published_locales": [],
  "refund_policy": {},
  "search_types": [
    "article",
    "page",
    "product"
  ],
  "secure_url": "https://polinas-potent-potions.myshopify.com",
  "shipping_policy": {},
  "subscription_policy": null,
  "taxes_included": false,
  "terms_of_service": {},
  "types": [
    "",
    "Animals & Pet Supplies",
    "Baking Flavors & Extracts",
    "Container",
    "Cooking & Baking Ingredients",
    "Dried Flowers",
    "Fruits & Vegetables",
    "Gift Cards",
    "Health",
    "Health & Beauty",
    "Invisibility",
    "Love",
    "Music & Sound Recordings",
    "Seasonings & Spices",
    "Water"
  ],
  "url": "https://polinas-potent-potions.myshopify.com",
  "vendors": [
    "Clover's Apothecary",
    "Polina's Potent Potions",
    "Ted's Apothecary Supply"
  ]
}
```
