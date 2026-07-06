---
title: 'Liquid filters: concat'
description: Concatenates (combines) two arrays.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/concat'
  md: 'https://shopify.dev/docs/api/liquid/filters/concat.md'
api_name: liquid
---

# concat

```oobleck
array | concat: array
```

Concatenates (combines) two arrays.

***

**Note:** The \<code>concat\</code> filter won\&#39;t filter out duplicates. If you want to remove duplicates, then you need to use the \<a href="/docs/api/liquid/filters/uniq">\<code>uniq\</code> filter\</a>.

***

##### Code

```liquid
{%- assign types_and_vendors = collection.all_types | concat: collection.all_vendors -%}

Types and vendors:

{% for item in types_and_vendors -%}
  {%- if item != blank -%}
    - {{ item }}
  {%- endif -%}
{%- endfor %}
```

##### Data

```json
{
  "collection": {
    "all_types": [
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
    "all_vendors": [
      "Clover's Apothecary",
      "Polina's Potent Potions",
      "Ted's Apothecary Supply"
    ]
  }
}
```

##### Output

```html
Types and vendors:

- Animals & Pet Supplies
- Baking Flavors & Extracts
- Container
- Cooking & Baking Ingredients
- Dried Flowers
- Fruits & Vegetables
- Gift Cards
- Health
- Health & Beauty
- Invisibility
- Love
- Music & Sound Recordings
- Seasonings & Spices
- Water
- Clover's Apothecary
- Polina's Potent Potions
- Ted's Apothecary Supply
```
