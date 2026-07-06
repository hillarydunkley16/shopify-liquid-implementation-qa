---
title: 'Liquid objects: quantity_rule'
description: A variant order quantity rule.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/quantity_rule'
  md: 'https://shopify.dev/docs/api/liquid/objects/quantity_rule.md'
api_name: liquid
---

# quantity\_​rule

A variant order quantity rule.

If no rule exists, then a default value is returned.

This rule can be set as part of a [B2B catalog](https://help.shopify.com/manual/b2b/catalogs/quantity-pricing).

***

**Note:** The default quantity rule is \<code>min=1,max=null,increment=1\</code>.

***

## Properties

* * **increment**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The number the order quantity can be incremented by. The default value is `1`.

  * **max**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The maximum order quantity.

    If there is no maximum quantity, then `nil` is returned.

  * **min**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The minimum order quantity. The default value is `1`.

##### Example

```json
{
  "min": 5,
  "max": 100,
  "increment": 5
}
```

### The variant order quantity rule

##### Code

```liquid
{{ product.variants.first.quantity_rule }}
```

##### Data

```json
{
  "product": {
    "variants": [
      {
        "quantity_rule": {
          "min": 1,
          "max": null,
          "increment": 1
        }
      },
      {
        "quantity_rule": {
          "min": 1,
          "max": null,
          "increment": 1
        }
      },
      {
        "quantity_rule": {
          "min": 1,
          "max": null,
          "increment": 1
        }
      },
      {
        "quantity_rule": {
          "min": 1,
          "max": null,
          "increment": 1
        }
      },
      {
        "quantity_rule": {
          "min": 1,
          "max": null,
          "increment": 1
        }
      },
      {
        "quantity_rule": {
          "min": 1,
          "max": null,
          "increment": 1
        }
      },
      {
        "quantity_rule": {
          "min": 1,
          "max": null,
          "increment": 1
        }
      },
      {
        "quantity_rule": {
          "min": 1,
          "max": null,
          "increment": 1
        }
      },
      {
        "quantity_rule": {
          "min": 1,
          "max": null,
          "increment": 1
        }
      }
    ]
  }
}
```

##### Output

```html
{"min"=>1, "max"=>nil, "increment"=>1}
```
