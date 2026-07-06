---
title: 'Liquid filters: sort_natural'
description: Sorts the items in an array in case-insensitive alphabetical order.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/sort_natural'
  md: 'https://shopify.dev/docs/api/liquid/filters/sort_natural.md'
api_name: liquid
---

# sort\_​natural

```oobleck
array | sort_natural
```

Sorts the items in an array in case-insensitive alphabetical order.

***

**Caution:** You shouldn\&#39;t use the \<code>\<span class="PreventFireFoxApplyingGapToWBR">sort\<wbr/>\_natural\</span>\</code> filter to sort numerical values. When comparing items an array, each item is converted to a string, so sorting on numerical values can lead to unexpected results.

***

##### Code

```liquid
{% assign tags = collection.all_tags | sort_natural %}

{% for tag in tags -%}
  {{ tag }}
{%- endfor %}
```

##### Data

```json
{
  "collection": {
    "all_tags": [
      "Burning",
      "dried",
      "extra-potent",
      "extracts",
      "fresh",
      "healing",
      "ingredients",
      "music",
      "plant",
      "Salty",
      "supplies"
    ]
  }
}
```

##### Output

```html
Burning
dried
extra-potent
extracts
fresh
healing
ingredients
music
plant
Salty
supplies
```

### Sort by an array item property

```oobleck
array | sort_natural: string
```

You can specify an array item property to sort the array items by.

##### Code

```liquid
{% assign products = collection.products | sort_natural: 'title' %}

{% for product in products -%}
  {{ product.title }}
{%- endfor %}
```

##### Data

```json
{
  "collection": {
    "products": [
      {
        "title": "Blue Mountain Flower"
      },
      {
        "title": "Charcoal"
      },
      {
        "title": "Crocodile tears"
      },
      {
        "title": "Dandelion milk"
      },
      {
        "title": "Draught of Immortality"
      },
      {
        "title": "Dried chamomile"
      },
      {
        "title": "Forest mushroom"
      },
      {
        "title": "Gift Card"
      },
      {
        "title": "Glacier ice"
      },
      {
        "title": "Ground mandrake root"
      },
      {
        "title": "Health potion"
      },
      {
        "title": "Invisibility potion"
      },
      {
        "title": "Komodo dragon scale"
      },
      {
        "title": "Love Potion"
      },
      {
        "title": "Mana potion"
      },
      {
        "title": "Potion beats"
      },
      {
        "title": "Potion bottle"
      },
      {
        "title": "Viper venom"
      },
      {
        "title": "Whole bloodroot"
      }
    ]
  }
}
```

##### Output

```html
Blue Mountain Flower
Charcoal
Crocodile tears
Dandelion milk
Draught of Immortality
Dried chamomile
Forest mushroom
Gift Card
Glacier ice
Ground mandrake root
Health potion
Invisibility potion
Komodo dragon scale
Love Potion
Mana potion
Potion beats
Potion bottle
Viper venom
Whole bloodroot
```
