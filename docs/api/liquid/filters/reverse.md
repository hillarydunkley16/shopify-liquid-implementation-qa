---
title: 'Liquid filters: reverse'
description: Reverses the order of the items in an array.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/reverse'
  md: 'https://shopify.dev/docs/api/liquid/filters/reverse.md'
api_name: liquid
---

# reverse

```oobleck
array | reverse
```

Reverses the order of the items in an array.

##### Code

```liquid
Original order:
{{ collection.products | map: 'title' | join: ', ' }}

Reverse order:
{{ collection.products | reverse | map: 'title' | join: ', ' }}
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
Original order:
Draught of Immortality, Glacier ice, Health potion, Invisibility potion

Reverse order:
Invisibility potion, Health potion, Glacier ice, Draught of Immortality
```

### Reversing strings

You can't use the `reverse` filter on strings directly. However, you can use the [`split` filter](https://shopify.dev/docs/api/liquid/filters/split) to create an array of characters in the string, reverse that array, and then use the [`join` filter](https://shopify.dev/docs/api/liquid/filters/join) to combine them again.

##### Code

```liquid
{{ collection.title | split: '' | reverse | join: '' }}
```

##### Data

```json
{
  "collection": {
    "title": "Sale potions"
  }
}
```

##### Output

```html
snoitop elaS
```
