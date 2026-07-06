---
title: 'Liquid filters: reject'
description: Filters an array to exclude items with a specific property value.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/reject'
  md: 'https://shopify.dev/docs/api/liquid/filters/reject.md'
api_name: liquid
---

# reject

```oobleck
array | reject: string, string
```

Filters an array to exclude items with a specific property value.

This requires you to provide both the property name and the associated value.

##### Code

```liquid
{% assign polina_products = collection.products | reject: 'vendor', "Polina's Potent Potions" %}

Products from other vendors than Polina's Potent Potions:

{% for product in polina_products -%}
  - {{ product.title }}
{%- endfor %}
```

##### Data

```json
{
  "collection": {
    "products": [
      {
        "title": "Blue Mountain Flower",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Charcoal",
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "title": "Crocodile tears",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Dandelion milk",
        "vendor": "Clover's Apothecary"
      },
      {
        "title": "Draught of Immortality",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Dried chamomile",
        "vendor": "Clover's Apothecary"
      },
      {
        "title": "Forest mushroom",
        "vendor": "Clover's Apothecary"
      },
      {
        "title": "Gift Card",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Glacier ice",
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "title": "Ground mandrake root",
        "vendor": "Clover's Apothecary"
      },
      {
        "title": "Health potion",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Invisibility potion",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Komodo dragon scale",
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "title": "Love Potion",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Mana potion",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Potion beats",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Potion bottle",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Viper venom",
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "title": "Whole bloodroot",
        "vendor": "Clover's Apothecary"
      }
    ]
  }
}
```

##### Output

```html
Products from other vendors than Polina's Potent Potions:

- Charcoal
- Dandelion milk
- Dried chamomile
- Forest mushroom
- Glacier ice
- Ground mandrake root
- Komodo dragon scale
- Viper venom
- Whole bloodroot
```
