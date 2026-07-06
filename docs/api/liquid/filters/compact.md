---
title: 'Liquid filters: compact'
description: Removes any `nil` items from an array.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/compact'
  md: 'https://shopify.dev/docs/api/liquid/filters/compact.md'
api_name: liquid
---

# compact

```oobleck
array | compact
```

Removes any `nil` items from an array.

##### Code

```liquid
{%- assign original_prices = collection.products | map: 'compare_at_price' -%}

Original prices:

{% for price in original_prices -%}
  - {{ price }}
{%- endfor %}

{%- assign compacted_original_prices = original_prices | compact -%}

Original prices - compacted:

{% for price in compacted_original_prices -%}
  - {{ price }}
{%- endfor %}
```

##### Data

```json
{
  "collection": {
    "products": [
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": "1000000.59"
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": "10.00"
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": "25.00"
      },
      {
        "compare_at_price": "400.00"
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      }
    ]
  }
}
```

##### Output

```html
Original prices:

- 
- 
- 
- 
- 100000059
- 
- 
- 
- 1000
- 
- 2500
- 40000
- 
- 
- 
- 
- 
- 
- 

Original prices - compacted:

- 100000059
- 1000
- 2500
- 40000
```
