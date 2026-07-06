---
title: 'Liquid filters: find'
description: Returns the first item in an array with a specific property value.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/find'
  md: 'https://shopify.dev/docs/api/liquid/filters/find.md'
api_name: liquid
---

# find

```oobleck
array | find: string, string
```

Returns the first item in an array with a specific property value.

This requires you to provide both the property name and the associated value.

##### Code

```liquid
{% assign product = collection.products | find: 'vendor', "Polina's Potent Potions" %}

{{ product.title }}
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
Blue Mountain Flower
```

### Returns `nil` when no items match the specified property value.

##### Code

```liquid
{% assign product = collection.products | find: 'vendor', "Polina's Potions" %}

{{ product.title | default: "No product found" }}
```

##### Data

```json
{
  "collection": {
    "products": [
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Clover's Apothecary"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Polina's Potent Potions"
      },
      {
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "vendor": "Clover's Apothecary"
      }
    ]
  }
}
```

##### Output

```html
No product found
```
