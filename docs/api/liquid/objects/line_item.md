---
title: 'Liquid objects: line_item'
description: >-
  A line in a cart, checkout, or order. Each line item represents a product
  variant.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/line_item'
  md: 'https://shopify.dev/docs/api/liquid/objects/line_item.md'
api_name: liquid
---

# line\_​item

A line in a cart, checkout, or order. Each line item represents a product variant.

## Properties

* * **discount\_​allocations**

    array of [discount\_allocation](https://shopify.dev/docs/api/liquid/objects/discount_allocation)

  * The discount allocations that apply to the line item.

    **Caution:** Not applicable for item component as discounts are applied to the parent line item.

  * **error\_​message**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * An informational error message about the status of the line item in the buyer's chosen language.

    **Note:** This field is applicable for cart line item only and currently available for shops using Checkout Extensibility.

  * **final\_​line\_​price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The combined price, in the currency's subunit, of all of the items in the line item. This includes any line-level discounts.

    The value is equal to `line_item.final_price` multiplied by `line_item.quantity`. It's output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

  * **final\_​price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The price of the line item in the currency's subunit. This includes any line-level discounts.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

  * **fulfillment**

    [fulfillment](https://shopify.dev/docs/api/liquid/objects/fulfillment)

  * The fulfillment of the line item.

  * **fulfillment\_​service**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The [fulfillment service](https://help.shopify.com/manual/shipping/understanding-shipping/dropshipping-and-fulfillment-services) for the vartiant associated with the line item. If there's no fulfillment service, then `manual` is returned.

  * **gift\_​card**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the product associated with the line item is a gift card. Returns `false` if not.

  * **grams**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The weight of the line item in the store's [default weight unit](https://help.shopify.com/manual/intro-to-shopify/initial-setup/setup-business-settings#set-or-change-your-stores-default-weight-unit).

    **Tip:** Use this property with the \<a href="/docs/api/liquid/filters/weight\_with\_unit">\<code>\<span class="PreventFireFoxApplyingGapToWBR">weight\<wbr/>\_with\<wbr/>\_unit\</span>\</code> filter\</a> to format the weight.

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the line item.

    The ID differs depending on the context. The following table outlines the possible contexts and their associated values:

    | Context | Value |
    | - | - |
    | [`cart.items`](https://shopify.dev/docs/api/liquid/objects/cart#cart-items) | The ID of the line item's variant.\<br>\<br>This ID isn't unique, and can be shared by multiple items with the same variant. |
    | [`checkout.line_items`](https://shopify.dev/docs/api/liquid/objects/checkout#checkout-line_items) | A temporary unique hash generated for the checkout. |
    | [`order.line_items`](https://shopify.dev/docs/api/liquid/objects/order#order-line_items) | A unique integer ID. |

  * **image**

    [image](https://shopify.dev/docs/api/liquid/objects/image)

  * The image of the line item.

    The image can come from one of the following sources:

    * The image of the variant associated with the line item
    * The featured image of the product associated with the line item, if there's no variant image

  * **instructions**

    [instructions](https://shopify.dev/docs/api/liquid/objects/instructions)

  * Instructions define behaviours and operations that can be performed on the nested cart line.

    **Note:** This field is applicable for cart line item only.

  * **item\_​components**

    array of [line\_item](https://shopify.dev/docs/api/liquid/objects/line_item)

  * The components of a line item.

    **Note:** This field is applicable for cart line item only.

  * **key**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The key of the line item.

    Line item keys are unique identifiers that consist of the following components separated by a colon:

    * The ID of the variant associated with the line item
    * A hash of unique characteristics of the line item.

    Note: Line item keys are not stable identifiers. The line item key will change as characteristics of the line item change. This includes, but is not limited to, properties and discount applications.

  * **line\_​level\_​discount\_​allocations**

    array of [discount\_allocation](https://shopify.dev/docs/api/liquid/objects/discount_allocation)

  * The discount allocations that apply directly to the line item.

    **Caution:** Not applicable for item component as discounts are applied to the parent line item.

  * **line\_​level\_​total\_​discount**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The total amount of any discounts applied to the line item in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **message**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * Information about the discounts that have affected the line item.

    The following table outlines what's returned depending on the number of discounts affecting the line item:

    | Number of discounts | Value |
    | - | - |
    | 0 | `nil` |
    | 1 | The [title](https://shopify.dev/docs/api/liquid/objects/discount_application#discount_application-title) of the discount. |
    | More than 1 | A Shopify generated string noting how many discounts have been applied. |

  * **options\_​with\_​values**

  * The name and value pairs for each option of the variant associated with the line item.

    **Note:** The array is never empty because variants with no options still have a default option. Because of this, you should use \<code>\<span class="PreventFireFoxApplyingGapToWBR">line\<wbr/>\_item.product.has\<wbr/>\_only\<wbr/>\_default\<wbr/>\_variant\</span>\</code> to check whether there\&#39;s any information to output.

    ExampleOutput the option values

    ##### Code

    ```liquid
    {% for item in cart.items %}
    <div class="cart__item">
      <p class="cart__item-title">
        {{ item.title }}
      </p>

      {%- unless item.product.has_only_default_variant %}
      <ul>
        {% for option in item.options_with_values -%}
        <li>{{ option.name }}: {{ option.value }}</li>
        {%- endfor %}
      </ul>
      {% endunless %}
    </div>
    {% endfor %}
    ```

    ##### Data

    ```json
    {
      "cart": {
        "items": [
          {
            "product": {
              "has_only_default_variant": true
            },
            "title": "Whole bloodroot"
          },
          {
            "product": {
              "has_only_default_variant": true
            },
            "title": "Viper venom"
          }
        ]
      }
    }
    ```

    ##### Output

    ```html
    <div class="cart__item">
      <p class="cart__item-title">
        Whole bloodroot
      </p>
    </div>

    <div class="cart__item">
      <p class="cart__item-title">
        Viper venom
      </p>
    </div>
    ```

  * **original\_​line\_​price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The combined price of all of the items in a line item in the currency's subunit, before any discounts have been applied.

    The value is equal to `line_item.original_price` multiplied by `line_item.quantity`. It's output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

  * **original\_​price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The price of the line item in the currency's subunit, before discounts have been applied.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

  * **parent\_​relationship**

    [parent\_relationship](https://shopify.dev/docs/api/liquid/objects/parent_relationship)

  * The parent relationship for a nested line item.

    **Note:** This field is applicable for cart line item only.

  * **product**

    [product](https://shopify.dev/docs/api/liquid/objects/product)

  * The product associated with the line item. May be a regular [product](https://shopify.dev/docs/api/liquid/objects/product) or a [remote product](https://shopify.dev/docs/api/liquid/objects/remote_product).

  * **product\_​id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The [ID](https://shopify.dev/docs/api/liquid/objects/product#product-id) of the line item's product.

  * **properties**

  * The properties of the line item.

    You can add, or allow customers to add, custom information to a line item with line item properties.

    Line item properties consist of a name and value pair. They can be captured with the following methods:

    * [A custom input inside a product form](https://shopify.dev/themes/architecture/templates/product#line-item-properties)
    * [The AJAX Cart API](https://shopify.dev/api/ajax/reference/cart#add-line-item-properties)

    **Tip:** To learn about how to display captured properties, refer to \<a href="/themes/architecture/templates/cart#display-line-item-properties">Display line item properties\</a>.

    ExampleCapture line item properties in the product form

    To capture line item properties inside the [product form](https://shopify.dev/docs/api/liquid/tags/form#form-product), you need to include an input, for each property. Each input needs a unique `name` attribute. Use the following format:

    ```
    name="properties[property-name]"
    ```

    The value of the input is captured as the value of the property.

    For example, you can use the following code to capture custom engraving text for a product:

    ```liquid
    {% form 'product', product %}
      ...
      <label for="engravingText">Engraving<label>
      <input type="text" id="engravingText" name="properties[Engraving]">
      ...
    {% endform %}
    ```

    ***

    **Tip:** You can add an underscore to the beginning of a property name to hide it from customers at checkout. For example, \<code>\<span class="PreventFireFoxApplyingGapToWBR">properties\[\_hidden\<wbr/>Property\<wbr/>Name]\</span>\</code>.

    ***

  * **quantity**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The quantity of the line item.

  * **requires\_​shipping**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the variant associated with the line item requires shipping. Returns `false` if not.

  * **selling\_​plan\_​allocation**

    [selling\_plan\_allocation](https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation)

  * The selling plan allocation of the line item. If the line item doesn't have a selling plan allocation, then `nil` is returned.

    #### Availability of selling plan information

    The following properties aren't available when referencing selling plan information through an [order's line items](https://shopify.dev/docs/api/liquid/objects/order#order-line_items):

    * [`selling_plan_allocation.compare_at_price`](https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation#selling_plan_allocation-compare_at_price)
    * [`selling_plan_allocation.price_adjustments`](https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation#selling_plan_allocation-price_adjustments)
    * [`selling_plan_allocation.selling_plan.group_id`](https://shopify.dev/docs/api/liquid/objects/selling_plan#selling_plan-group_id)
    * [`selling_plan_allocation.selling_plan.options`](https://shopify.dev/docs/api/liquid/objects/selling_plan#selling_plan-options)
    * [`selling_plan_allocation.selling_plan.price_adjustments`](https://shopify.dev/docs/api/liquid/objects/selling_plan#selling_plan-price_adjustments)
    * [`selling_plan_allocation.selling_plan_group_id`](https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation#selling_plan_allocation-selling_plan_group_id)

    **Tip:** If you need to show selling plan information post-purchase, then you should use \<a href="/docs/api/liquid/objects/selling\_plan#selling\_plan-name">\<code>\<span class="PreventFireFoxApplyingGapToWBR">selling\<wbr/>\_plan.name\</span>\</code>\</a>.

  * **sku**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The [sku](https://shopify.dev/docs/api/liquid/objects/variant#variant-sku) of the variant associated with the line item.

  * **successfully\_​fulfilled\_​quantity**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The number of items from the line item that have been successfully fulfilled.

  * **tax\_​lines**

    array of [tax\_line](https://shopify.dev/docs/api/liquid/objects/tax_line)

  * The tax lines for the line item.

  * **taxable**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if taxes should be charged on the line item. Returns `false` if not.

  * **title**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The title of the line item. The title is a combination of `line_item.product.title` and `line_item.variant.title`, separated by a hyphen.

    In most contexts, the line item title appears in the customer's preferred language. However, in the context of an [order](https://shopify.dev/docs/api/liquid/objects/order), the line item title appears in the language that the customer checked out in. The title can receive an override value from the [Cart Transform API](https://shopify.dev/docs/api/functions/reference/cart-transform#showing-overrides). Overrides take precedence over translations.

    #### Line item title history

    When referencing line item, product, and variant titles in the context of an order, the following changes might result in a different output than you expect:

    * A product or variant being deleted
    * A product or variant title being edited

    When `line_item.title` is referenced for an order, the line item title at the time of the order is returned. However, when `line_item.product.title` and `line_item.variant.title` are referenced, the current value for each title is returned.

  * **unit\_​price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The [unit price](https://help.shopify.com/manual/products/details/product-pricing/unit-pricing#add-unit-prices-to-your-product) of the line item in the currency's subunit.

    The price reflects any discounts that are applied to the line item. The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use the \<a href="/docs/api/liquid/filters/unit\_price\_with\_measurement">\<code>\<span class="PreventFireFoxApplyingGapToWBR">unit\<wbr/>\_price\<wbr/>\_with\<wbr/>\_measurement\</span>\</code> filter\</a> with this property and the \<code>\<span class="PreventFireFoxApplyingGapToWBR">line\<wbr/>\_item.unit\<wbr/>\_price\<wbr/>\_measurement\</span>\</code> property to output a formatted unit price with measurement.

    To learn about how to display unit prices in your theme, refer to [Unit pricing](https://shopify.dev/themes/pricing-payments/unit-pricing).

  * **unit\_​price\_​measurement**

    [unit\_price\_measurement](https://shopify.dev/docs/api/liquid/objects/unit_price_measurement)

  * The unit price measurement of the line item.

    To learn about how to display unit prices in your theme, refer to [Unit pricing](https://shopify.dev/themes/pricing-payments/unit-pricing).

    **Tip:** Use the \<a href="/docs/api/liquid/filters/unit\_price\_with\_measurement">\<code>\<span class="PreventFireFoxApplyingGapToWBR">unit\<wbr/>\_price\<wbr/>\_with\<wbr/>\_measurement\</span>\</code> filter\</a> with the \<code>\<span class="PreventFireFoxApplyingGapToWBR">line\<wbr/>\_item.unit\<wbr/>\_price\</span>\</code> property and this property to output a formatted unit price with measurement.

  * **url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The relative URL of the variant associated with the line item.

  * **url\_​to\_​remove**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A URL to remove the line item from the cart.

    **Tip:** To learn more about how to use this property in your theme, refer to \<a href="/themes/architecture/templates/cart#remove-line-items-from-the-cart">Remove line items from the cart\</a>.

  * **variant**

    [variant](https://shopify.dev/docs/api/liquid/objects/variant)

  * The variant associated with the line item.

  * **variant\_​id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The [ID](https://shopify.dev/docs/api/liquid/objects/variant#variant-id) of the line item's variant.

  * **vendor**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The vendor of the variant associated with the line item.

## Deprecated Properties

* * **discounts**

    array of [discount](https://shopify.dev/docs/api/liquid/objects/discount)

    Deprecated

  * The discounts applied to the line item.

    **Deprecated:**

    Deprecated because not all discount types and details are available.

    The `line_item.discounts` property has been replaced by [`line_item.discount_allocations`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-discount_allocations).

  * **line\_​price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

    Deprecated

  * The combined price, in the currency's subunit, of all of the items in a line item. This includes any discounts from [Shopify Scripts](https://help.shopify.com/manual/checkout-settings/script-editor).

    The value is equal to `line_item.price` multiplied by `line_item.quantity`. It's output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

    **Deprecated:**

    Deprecated because discounts from automatic discounts and discount codes aren't included.

    The `line_item.line_price` property has been replaced by [`line_item.final_line_price`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-final_line_price).

  * **price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

    Deprecated

  * The price of the line item in the currency's subunit. This includes any discounts from [Shopify Scripts](https://help.shopify.com/manual/checkout-settings/script-editor).

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

    **Deprecated:**

    Deprecated because discounts from automatic discounts and discount codes aren't included.

    The `line_item.price` property has been replaced by [`line_item.final_price`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-final_price).

  * **total\_​discount**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

    Deprecated

  * The total amount, in the currency's subunit, of any discounts applied to the line item by [Shopify Scripts](https://help.shopify.com/manual/checkout-settings/script-editor).

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

    **Deprecated:**

    Deprecated because discounts from automatic discounts and discount codes aren't included.

    The `line_item.total_discount` property has been replaced by [`line_item.line_level_total_discount`](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-line_level_total_discount).

##### Example

```json
{
  "discount_allocations": [],
  "discounts": [],
  "error_message": "",
  "final_line_price": "74.97",
  "final_price": "24.99",
  "fulfillment": {},
  "fulfillment_service": "manual",
  "gift_card": false,
  "grams": 0,
  "id": 10974183882817,
  "image": {},
  "instructions": null,
  "item_components": null,
  "key": 10974183882817,
  "line_level_discount_allocations": [],
  "line_level_total_discount": "0.00",
  "line_price": "74.97",
  "message": "",
  "options_with_values": [
    {
      "name": "Title",
      "value": "Default Title"
    }
  ],
  "original_line_price": "74.97",
  "original_price": "24.99",
  "parent_relationship": null,
  "price": "24.99",
  "product": {},
  "product_id": 6792596455489,
  "properties": {},
  "quantity": 3,
  "requires_shipping": true,
  "selling_plan_allocation": null,
  "sku": "",
  "successfully_fulfilled_quantity": 2,
  "tax_lines": [],
  "taxable": true,
  "title": "Bloodroot (whole)",
  "total_discount": "0.00",
  "unit_price": "49.98",
  "unit_price_measurement": {
    "measured_type": "weight",
    "quantity_value": "500.0",
    "quantity_unit": "g",
    "reference_value": 1,
    "reference_unit": "kg"
  },
  "url": {},
  "url_to_remove": null,
  "variant": {},
  "variant_id": 39888235757633,
  "vendor": "Clover's Apothecary"
}
```
