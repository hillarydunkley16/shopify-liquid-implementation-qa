---
title: 'Liquid filters: weight_with_unit'
description: >-
  Generates a formatted weight for a [`variant`
  object](/docs/api/liquid/objects/variant#variant-weight). The weight unit is

  set in the [general settings](https://www.shopify.com/admin/settings/general)
  in the Shopify admin.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/weight_with_unit'
  md: 'https://shopify.dev/docs/api/liquid/filters/weight_with_unit.md'
api_name: liquid
---

# weight\_​with\_​unit

```oobleck
number | weight_with_unit
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates a formatted weight for a [`variant` object](https://shopify.dev/docs/api/liquid/objects/variant#variant-weight). The weight unit is set in the [general settings](https://www.shopify.com/admin/settings/general) in the Shopify admin.

##### Code

```liquid
{%- assign variant = product.variants.first -%}

{{ variant.weight | weight_with_unit }}
```

##### Data

```json
{
  "product": {
    "variants": [
      {
        "weight": 200
      },
      {
        "weight": 200
      },
      {
        "weight": 400
      },
      {
        "weight": 200
      }
    ]
  }
}
```

##### Output

```html
0.2 kg
```

### Override the default unit

```oobleck
number | weight_with_unit: variable
```

You can specify a unit to override the default from the general settings.

##### Code

```liquid
{%- assign variant = product.variants.first -%}

{{ variant.weight | weight_with_unit: variant.weight_unit }}
```

##### Data

```json
{
  "product": {
    "variants": [
      {
        "weight": 200,
        "weight_unit": "g"
      },
      {
        "weight": 200,
        "weight_unit": "g"
      },
      {
        "weight": 400,
        "weight_unit": "g"
      },
      {
        "weight": 200,
        "weight_unit": "g"
      }
    ]
  }
}
```

##### Output

```html
200 g
```
