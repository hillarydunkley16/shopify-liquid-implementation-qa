---
title: 'Liquid objects: remote_product'
description: >-
  A product that comes from a remote source, inheriting all
  [product](/docs/api/liquid/objects/product) functionality and also providing
  additional context about the remote source.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/remote_product'
  md: 'https://shopify.dev/docs/api/liquid/objects/remote_product.md'
api_name: liquid
---

# remote\_​product

A product that comes from a remote source, inheriting all [product](https://shopify.dev/docs/api/liquid/objects/product) functionality and also providing additional context about the remote source.

## Properties

* * **available**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if at least one of the variants of the product is available. Returns `false` if not.

    For a variant to be available, it needs to meet one of the following criteria:

    * The `variant.inventory_quantity` is greater than 0.
    * The `variant.inventory_policy` is set to `continue`.
    * The `variant.inventory_management` is `nil`.
    * The variant has an associated [delivery profile](https://shopify.dev/docs/apps/selling-strategies/purchase-options/deferred/shipping-delivery/delivery-profiles) with a valid shipping rate.

  * **category**

    [taxonomy\_category](https://shopify.dev/docs/api/liquid/objects/taxonomy_category)

  * The taxonomy category for the product

  * **compare\_​at\_​price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The lowest **compare at** price of any variants of the product in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

  * **compare\_​at\_​price\_​max**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The highest **compare at** price of any variants of the product in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

  * **compare\_​at\_​price\_​min**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The lowest **compare at** price of any variants of the product in the currency's subunit. This is the same as `product.compare_at_price`.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

  * **compare\_​at\_​price\_​varies**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the variant **compare at** prices of the product vary. Returns `false` if not.

  * **content**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The description of the product.

    **Note:** This is the same value as \<a href="/docs/api/liquid/objects/product#product-description">\<code>product.description\</code>\</a>.

  * **created\_​at**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A timestamp for when the product was created.

    **Tip:** Use the \<a href="/docs/api/liquid/filters/date">\<code>date\</code> filter\</a> to format the timestamp.

  * **description**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The description of the product.

    **Note:** This is the same value as \<a href="/docs/api/liquid/objects/product#product-content">\<code>product.content\</code>\</a>. The description of remote products is modified to include a link to the remote store\&#39;s shipping and refund policies, if the shop has defined them.

  * **featured\_​image**

    [image](https://shopify.dev/docs/api/liquid/objects/image)

  * The first (featured) image attached to the product.

  * **featured\_​media**

    [media](https://shopify.dev/docs/api/liquid/objects/media)

  * The first (featured) media attached to the product.

    **Note:** Depending on rendering context, the featured media of remote products may be modified to include a badge highlighting the remote source.

    **Tip:** You can use \<a href="/docs/api/liquid/filters/media-filters">media filters\</a> to output media URLs and displays. To learn about how to include media in your theme, refer to \<a href="/themes/product-merchandising/media/support-media">Support product media\</a>.

  * **first\_​available\_​variant**

    [variant](https://shopify.dev/docs/api/liquid/objects/variant)

  * The first available variant of the product.

    For a variant to be available, it needs to meet one of the following criteria:

    * The `variant.inventory_quantity` is greater than 0.
    * The `variant.inventory_policy` is set to `continue`.
    * The `variant.inventory_management` is `nil`.

  * **gift\_​card?**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the product is a gift card. Returns `false` if not.

  * **has\_​only\_​default\_​variant**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the product doesn't have any options. Returns `false` if not.

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the product.

  * **images**

    array of [image](https://shopify.dev/docs/api/liquid/objects/image)

  * The images attached to the product.

  * **media**

    array of [media](https://shopify.dev/docs/api/liquid/objects/media)

  * The media attached to the product, sorted by the date it was added to the product.

    **Note:** Depending on rendering context, the media of remote products may be modified to include a badge highlighting the remote source.

    **Tip:** You can use \<a href="/docs/api/liquid/filters/media-filters">media filters\</a> to output media URLs and displays. To learn about how to include media in your theme, refer to \<a href="/themes/product-merchandising/media/support-media">Support product media\</a>.

  * **metafields**

  * The metafields applied to the product.

    **Note:** Only standard metafields set by the remote store are included. Custom metafields are not.

  * **options**

    array of [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The option names of the product.

    ExampleOutput the options

    You can use the [`size` filter](https://shopify.dev/docs/api/liquid/filters/size) with dot notation to determine how many options a product has.

    ##### Code

    ```liquid
    {% if product.options.size > 0 -%}
      {% for option in product.options -%}
        - {{ option }}
      {%- endfor %}
    {%- endif %}
    ```

    ##### Data

    ```json
    {
      "product": {
        "options": [
          "Size",
          "Strength"
        ]
      }
    }
    ```

    ##### Output

    ```html
    - Size
    - Strength
    ```

  * **options\_​by\_​name**

  * Allows you to access a specific [product option](https://shopify.dev/docs/api/liquid/objects/product_option) by its name.

    ExampleOutput the values for a specific option

    When accessing a specific option, the name is case-insensitive.

    ##### Code

    ```liquid
    <label>
      Strength
      <select>
        {%- for value in product.options_by_name['strength'].values %}
        <option>{{ value }}</option>
        {%- endfor %}
      </select>
    </label>
    ```

    ##### Data

    ```json
    {
      "product": {
        "options_by_name": {}
      }
    }
    ```

    ##### Output

    ```html
    <label>
      Strength
      <select>
        <option>Low</option>
        <option>Medium</option>
        <option>High</option>
      </select>
    </label>
    ```

  * **options\_​with\_​values**

    array of [product\_option](https://shopify.dev/docs/api/liquid/objects/product_option)

  * The options on the product.

  * **price**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The lowest price of any variants of the product in the currency's subunit.

    **Note:** This is the same value as \<a href="/docs/api/liquid/objects/product#product-price\_min">\<code>\<span class="PreventFireFoxApplyingGapToWBR">product.price\<wbr/>\_min\</span>\</code>\</a>.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

  * **price\_​max**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The highest price of any variants of the product in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

  * **price\_​min**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The lowest price of any variants of the product in the currency's subunit.

    **Note:** This is the same value as \<a href="/docs/api/liquid/objects/product#product-price">\<code>product.price\</code>\</a>.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted price.

  * **price\_​varies**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the product's variant prices vary. Returns `false` if not.

  * **published\_​at**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A timestamp for when the product was published.

    **Tip:** Use the \<a href="/docs/api/liquid/filters/date">\<code>date\</code> filter\</a> to format the timestamp.

  * **quantity\_​price\_​breaks\_​configured?**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the product has at least one variant with quantity price breaks in the current customer context. Returns `false` if not.

  * **remote\_​details**

    [remote\_details](https://shopify.dev/docs/api/liquid/objects/remote_details)

  * Information about the remote source from which the remote product came from.

  * **requires\_​selling\_​plan**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if all of the variants of the product require a selling plan. Returns `false` if not.

    **Note:** A variant requires a selling plan if \<a href="/docs/api/liquid/objects/variant#variant-requires\_selling\_plan">\<code>\<span class="PreventFireFoxApplyingGapToWBR">variant.requires\<wbr/>\_selling\<wbr/>\_plan\</span>\</code>\</a> is \<code>true\</code>.

  * **selected\_​or\_​first\_​available\_​selling\_​plan\_​allocation**

    [selling\_plan\_allocation](https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation)

  * The currently selected, or first available, selling plan allocation.

    The following logic is used to determine which selling plan allocation is returned:

    | Selling plan allocation | Return criteria |
    | - | - |
    | The currently selected allocation | Returned if a variant and selling plan are selected. The selected variant is determined by the `variant` URL parameter, and the selected selling plan is determined by the `selling_plan` URL parameter. |
    | The first allocation on the first available variant | Returned if no allocation is currently selected. |
    | The first allocation on the first variant | Returned if no allocation is currently selected, and there are no available variants. |

    If the product doesn't have any selling plans, then `nil` is returned.

  * **selected\_​or\_​first\_​available\_​variant**

    [variant](https://shopify.dev/docs/api/liquid/objects/variant)

  * The currently selected or first available variant of the product.

    If a variant is selected, it will be returned, regardless of its availability. Otherwise, the first available variant is returned. If no available variant exists, the first variant is returned.

    A selected variant is determined by the following criteria:

    * On product pages, it is based on the variant ID set in the `variant` URL parameter.
    * In search results and filtered collections, it is the most relevant variant based on search terms and applied filters.

    For a variant to be available, it needs to meet one of the following criteria:

    * The `variant.inventory_quantity` is greater than 0.
    * The `variant.inventory_policy` is set to `continue`.
    * The `variant.inventory_management` is `nil`.

  * **selected\_​selling\_​plan**

    [selling\_plan](https://shopify.dev/docs/api/liquid/objects/selling_plan)

  * The currently selected selling plan.

    If no selling plan is selected, then `nil` is returned.

    **Note:** The selected selling plan is determined by the \<code>\<span class="PreventFireFoxApplyingGapToWBR">selling\<wbr/>\_plan\</span>\</code> URL parameter.

  * **selected\_​selling\_​plan\_​allocation**

    [selling\_plan\_allocation](https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation)

  * The currently selected selling plan allocation for the currently selected variant.

    If no variant and selling plan are selected, then `nil` is returned.

    **Note:** The selected variant is determined by the \<code>variant\</code> URL parameter, and the selected selling plan is determined by the \<code>\<span class="PreventFireFoxApplyingGapToWBR">selling\<wbr/>\_plan\</span>\</code> URL parameter.

  * **selected\_​variant**

    [variant](https://shopify.dev/docs/api/liquid/objects/variant)

  * The currently selected variant of the product.

    If no variant is currently selected, then `nil` is returned.

    **Note:** On product pages, it is based on the variant ID set in the \<code>variant\</code> URL parameter. In search results and filtered collections, it is the most relevant variant based on search terms and applied filters.

  * **selling\_​plan\_​groups**

    array of [selling\_plan\_group](https://shopify.dev/docs/api/liquid/objects/selling_plan_group)

  * The selling plan groups that the variants of the product are included in.

  * **template\_​suffix**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the custom template assigned to the product.

    **Note:** Remote products have pre-determined dedicated template names, always prefixed with \&quot;remote.\&quot; This allows them to be managed independently of regular product templates. E.g. \&quot;remote.seller\&quot;

  * **title**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The title of the product.

    **Note:** In a cart or search suggestions context, the title of a remote product is appended with \&quot;Sold by {store name}\&quot;.

  * **type**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The type of the product.

  * **url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The relative URL of the product.

    If a product is rendered in search results or a filtered collection, then the URL contains the `variant` parameter of the most relevant variant.

    ```liquid
    /products/gorgeous-wooden-computer?variant=1234567890
    ```

    If a product is rendered as a [product recommendation](https://shopify.dev/docs/themes/product-merchandising/recommendations), then the URL contains tracking parameters:

    ```liquid
    /products/gorgeous-wooden-computer?pr_choice=default&pr_prod_strat=description&pr_rec_pid=13&pr_ref_pid=17&pr_seq=alternating
    ```

  * **variants**

    array of [variant](https://shopify.dev/docs/api/liquid/objects/variant)

  * The variants of the product.

    **Note:** Returns a maximum of 250 variants when unpaginated. Tip: Use the \<a href="/docs/api/liquid/tags/paginate">paginate\</a> tag to choose how many variants to show per page, up to a limit of 50.

  * **variants\_​count**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The total number of variants for the product.

  * **vendor**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The vendor of the product.

### Directly accessible in

* [product](https://shopify.dev/themes/architecture/templates/product)

### Returned by

* [collection.products](https://shopify.dev/docs/api/liquid/objects/collection#collection-products)
* [line\_​item.product](https://shopify.dev/docs/api/liquid/objects/line_item#line_item-product)
* [search.results](https://shopify.dev/docs/api/liquid/objects/search#search-results)
* [variant.product](https://shopify.dev/docs/api/liquid/objects/variant#variant-product)

## Templates using remote\_product

[Theme architecture](https://shopify.dev/themes/architecture/templates/product)

[product template](https://shopify.dev/themes/architecture/templates/product)
