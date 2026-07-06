---
title: 'Liquid filters: has'
description: Tests if any item in an array has a specific property value.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/has'
  md: 'https://shopify.dev/docs/api/liquid/filters/has.md'
api_name: liquid
---

# has

```oobleck
array | has: string, string
```

returns [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

Tests if any item in an array has a specific property value.

This requires you to provide both the property name and the associated value.

##### Code

```liquid
{% assign has_potent_potions = collection.products | has: 'vendor', "Polina's Potent Potions" %}

{{ has_potent_potions }}
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
true
```

### Returns `false` when no items match the specified property value.

##### Code

```liquid
{% assign has_potent_potions = collection.products | has: 'vendor', "Polina's Potions" %}

{{ has_potent_potions }}
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
false
```
