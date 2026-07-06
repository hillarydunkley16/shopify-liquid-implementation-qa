---
title: 'Liquid objects: scripts'
description: >-
  The active scripts, of each script type, on the store.

  > Caution:

  > Shopify Scripts will be sunset on August 28, 2025. Migrate your existing
  scripts to [Shopify Functions](/docs/api/functions) before this date.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/scripts'
  md: 'https://shopify.dev/docs/api/liquid/objects/scripts.md'
api_name: liquid
---

# scripts

The active scripts, of each script type, on the store.

***

**Caution:** Shopify Scripts will be sunset on August 28, 2025. Migrate your existing scripts to \<a href="/docs/api/functions">Shopify Functions\</a> before this date.

***

There can be only one active script of each type. Currently, the only type accessible in Liquid is `cart_calculate_line_items`.

***

**Tip:** To learn more about Shopify Scripts and the Script Editor, visit the \<a href="https://help.shopify.com/manual/checkout-settings/script-editor">Shopify Help Center\</a>.

***

## Properties

* * **cart\_​calculate\_​line\_​items**

    [script](https://shopify.dev/docs/api/liquid/objects/script)

  * The active line item script.

    If no line item script is currently active, then `nil` is returned.

    ExampleAdvertise the currently active line item script

    ##### Code

    ```liquid
    {% if scripts.cart_calculate_line_items %}
      <p>Don't miss our current sale: <strong>{{ scripts.cart_calculate_line_items.name }}</strong></p>
    {% endif %}
    ```

    ##### Data

    ```json
    {
      "scripts": {
        "cart_calculate_line_items": {}
      }
    }
    ```

    ##### Output

    ```html
    <p>Don't miss our current sale: <strong>10% off Whole bloodroot</strong></p>
    ```

##### Example

```json
{
  "cart_calculate_line_items": {}
}
```
