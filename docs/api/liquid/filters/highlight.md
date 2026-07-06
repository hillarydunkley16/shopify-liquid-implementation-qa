---
title: 'Liquid filters: highlight'
description: >-
  Wraps all instances of a specific string, within a given string, with an HTML
  `<strong>` tag with a `class` attribute

  of `highlight`.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/highlight'
  md: 'https://shopify.dev/docs/api/liquid/filters/highlight.md'
api_name: liquid
---

# highlight

```oobleck
string | highlight: string
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Wraps all instances of a specific string, within a given string, with an HTML `<strong>` tag with a `class` attribute of `highlight`.

##### Code

```liquid
{% for item in search.results %}
  {% if item.object_type == 'product' %}
    {{ item.description | highlight: search.terms }}
  {% else %}
    {{ item.content | highlight: search.terms }}
  {% endif %}
{% endfor %}
```

##### Data

```json
{
  "search": {
    "results": [
      {
        "description": "",
        "object_type": "product"
      },
      {
        "description": "",
        "object_type": "product"
      },
      {
        "description": "Some relaxing music to stir potions to!",
        "object_type": "product"
      },
      {
        "description": "This is a love potion.",
        "object_type": "product"
      },
      {
        "description": "",
        "object_type": "product"
      },
      {
        "description": "",
        "object_type": "product"
      },
      {
        "description": "",
        "object_type": "product"
      },
      {
        "description": "",
        "object_type": "product"
      },
      {
        "description": "",
        "object_type": "product"
      }
    ],
    "terms": "love"
  }
}
```

##### Output

```html
Some relaxing music to stir potions to!
  

  
    This is a <strong class="highlight">love</strong> potion.
```
