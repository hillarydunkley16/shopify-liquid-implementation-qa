---
title: 'Liquid objects: product_option_value'
description: 'A product option value, such as "red" for the option "color".'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/product_option_value'
  md: 'https://shopify.dev/docs/api/liquid/objects/product_option_value.md'
api_name: liquid
---

# product\_​option\_​value

A product option value, such as "red" for the option "color".

## Properties

* * **available**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Whether or not the option value is available.

    In the context of the selected values for previous options, indicates whether the current option value has any purchaseable combinations in any subsequent options, or whether the current option value is purchaseable if there are no subsequent options. For example, if a product comes in Color/Size/Material and Red/Small/Cotton is selected, `available` will indicate:

    * Color: Whether any variants for the Color option value are available for purchase.
    * Size: Whether any variants for Color:Red and the Size option value are available for purchase.
    * Material: Whether any variants for Color:Red, Size:Small, and the Material option value are available for purchase.

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the product option value.

  * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the product option value.

  * **product\_​url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * Returns a URL if the option value may be associated with another product, nil otherwise.

    ```liquid
    /products/gorgeous-wooden-computer
    ```

  * **selected**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Whether or not the option value is selected.

  * **swatch**

    [swatch](https://shopify.dev/docs/api/liquid/objects/swatch)

  * Returns a [swatch](https://shopify.dev/docs/api/liquid/objects/swatch) drop for the product option value. If there is no saved `color` or `image` content for the swatch, then the return value is `nil`.

  * **variant**

    [variant](https://shopify.dev/docs/api/liquid/objects/variant)

  * The variant associated with this option value combined with the other currently selected option values, if one exists.

    If this option value is selected (`selected == true`), this returns the `selected_or_first_available_variant`.

    If this option value is not selected (`selected == false`), this returns the variant that is associated with the current option value and the other currently selected option values.

    Using optionValue.variant is the recommended way to render product option values availability. For more information, refer to [rendering option value availability.](https://shopify.dev/docs/storefronts/themes/product-merchandising/variants/support-high-variant-products#option-value-availability)

##### Example

```json
{
  "available": true,
  "id": 2070385033281,
  "name": "Bronze",
  "product_url": null,
  "selected": true,
  "swatch": {},
  "variant": {}
}
```
