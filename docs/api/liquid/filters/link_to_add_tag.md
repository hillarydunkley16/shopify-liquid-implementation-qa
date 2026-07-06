---
title: 'Liquid filters: link_to_add_tag'
description: >-
  Generates an HTML `<a>` tag with an `href` attribute linking to the current
  blog or collection, filtered to show

  only articles or products that have a given tag, as well as any currently
  active tags.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/link_to_add_tag'
  md: 'https://shopify.dev/docs/api/liquid/filters/link_to_add_tag.md'
api_name: liquid
---

# link\_​to\_​add\_​tag

```oobleck
string | link_to_add_tag
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates an HTML `<a>` tag with an `href` attribute linking to the current blog or collection, filtered to show only articles or products that have a given tag, as well as any currently active tags.

***

**Tip:** To learn more about filtering by tag, refer to \<a href="/themes/architecture/templates/blog#filter-articles-by-tag">Filter articles by tag\</a> or \<a href="/themes/navigation-search/filtering/tag-filtering">Filter collections by tag\</a>.

***

##### Code

```liquid
{% for tag in collection.all_tags %}
  {%- if current_tags contains tag -%}
    {{ tag }}
  {%- else -%}
    {{ tag | link_to_add_tag: tag }}
  {%- endif -%}
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
<a href="/services/liquid_rendering/extra-potent" title="Narrow selection to products matching tag extra-potent">extra-potent</a>

<a href="/services/liquid_rendering/fresh" title="Narrow selection to products matching tag fresh">fresh</a>

<a href="/services/liquid_rendering/healing" title="Narrow selection to products matching tag healing">healing</a>

<a href="/services/liquid_rendering/ingredients" title="Narrow selection to products matching tag ingredients">ingredients</a>
```
