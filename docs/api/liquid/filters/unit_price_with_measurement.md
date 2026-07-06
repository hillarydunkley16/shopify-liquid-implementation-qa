---
title: 'Liquid filters: unit_price_with_measurement'
description: >-
  Formats a given unit price and measurement based on the store's [**HTML
  without currency**
  setting](https://help.shopify.com/manual/payments/currency-formatting).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/unit_price_with_measurement'
  md: 'https://shopify.dev/docs/api/liquid/filters/unit_price_with_measurement.md'
api_name: liquid
---

# unit\_​price\_​with\_​measurement

```oobleck
number | unit_price_with_measurement: unit_price_measurement
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Formats a given unit price and measurement based on the store's [**HTML without currency** setting](https://help.shopify.com/manual/payments/currency-formatting).

##### Code

```liquid
{%- assign variant = product.variants.first -%}

{{ variant.unit_price | unit_price_with_measurement: variant.unit_price_measurement }}
```

##### Data

```json
{
  "product": {
    "variants": [
      {
        "unit_price": "50.00",
        "unit_price_measurement": "UnitPriceMeasurementDrop"
      },
      {
        "unit_price": "50.00",
        "unit_price_measurement": "UnitPriceMeasurementDrop"
      },
      {
        "unit_price": "25.00",
        "unit_price_measurement": "UnitPriceMeasurementDrop"
      },
      {
        "unit_price": "25.00",
        "unit_price_measurement": "UnitPriceMeasurementDrop"
      }
    ]
  }
}
```

##### Output

```html
$50.00/kg
```

### Formatted unit price

```oobleck
string | unit_price_with_measurement: unit_price_measurement
```

You can specify a formatted unit price using one of the [money filters](https://shopify.dev/docs/api/liquid/filters/payment_button#money-filters).

##### Code

```liquid
{%- assign variant = product.variants.first -%}

{{ variant.unit_price | money_with_currency | unit_price_with_measurement: variant.unit_price_measurement }}
```

##### Data

```json
{
  "product": {
    "variants": [
      {
        "unit_price": "50.00",
        "unit_price_measurement": "UnitPriceMeasurementDrop"
      },
      {
        "unit_price": "50.00",
        "unit_price_measurement": "UnitPriceMeasurementDrop"
      },
      {
        "unit_price": "25.00",
        "unit_price_measurement": "UnitPriceMeasurementDrop"
      },
      {
        "unit_price": "25.00",
        "unit_price_measurement": "UnitPriceMeasurementDrop"
      }
    ]
  }
}
```

##### Output

```html
$50.00 CAD/kg
```
