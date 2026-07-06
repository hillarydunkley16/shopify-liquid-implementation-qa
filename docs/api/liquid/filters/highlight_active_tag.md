---
title: 'Liquid filters: highlight_active_tag'
description: >-
  Wraps a given tag within the [`collection`
  object](https://shopify.dev/docs/api/liquid/objects/collection) in an HTML
  `<span>` tag, with a `class` attribute of `active`, if the tag is currently
  active. Only

  applies to collection tags.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/highlight_active_tag'
  md: 'https://shopify.dev/docs/api/liquid/filters/highlight_active_tag.md'
api_name: liquid
---

# highlight\_​active\_​tag

```oobleck
string | highlight_active_tag
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Wraps a given tag within the [`collection` object](https://shopify.dev/docs/api/liquid/objects/collection) in an HTML `<span>` tag, with a `class` attribute of `active`, if the tag is currently active. Only applies to collection tags.

##### Code

```liquid
{% for tag in collection.all_tags %}
  {{- tag | highlight_active_tag | link_to_tag: tag }}
{% endfor %}
```

##### Data

```json
{
  "collection": {
    "all_tags": [
      "extra-potent",
      "fresh",
      "healing",
      "ingredients"
    ]
  },
  "template": "collection"
}
```

##### Output

```html
<a href="/services/liquid_rendering/extra-potent" title="Show products matching tag extra-potent"><span class="active">extra-potent</span></a>

<a href="/services/liquid_rendering/fresh" title="Show products matching tag fresh">fresh</a>

<a href="/services/liquid_rendering/healing" title="Show products matching tag healing">healing</a>

<a href="/services/liquid_rendering/ingredients" title="Show products matching tag ingredients">ingredients</a>
```
