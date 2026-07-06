---
title: 'Liquid filters: map'
description: Creates an array of values from a specific property of the items in an array.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/map'
  md: 'https://shopify.dev/docs/api/liquid/filters/map.md'
api_name: liquid
---

# map

```oobleck
array | map: string
```

Creates an array of values from a specific property of the items in an array.

##### Code

```liquid
{%- assign product_titles = collection.products | map: 'title' -%}

{{ product_titles | join: ', ' }}
```

##### Data

```json
{
  "collection": {
    "products": [
      {
        "title": "Draught of Immortality"
      },
      {
        "title": "Glacier ice"
      },
      {
        "title": "Health potion"
      },
      {
        "title": "Invisibility potion"
      }
    ]
  }
}
```

##### Output

```html
Draught of Immortality, Glacier ice, Health potion, Invisibility potion
```
