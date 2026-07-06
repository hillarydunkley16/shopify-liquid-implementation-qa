---
title: 'Liquid objects: part'
description: A part in the navigation for pagination.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/part'
  md: 'https://shopify.dev/docs/api/liquid/objects/part.md'
api_name: liquid
---

# part

A part in the navigation for pagination.

## Properties

* * **is\_​link**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the part is a link. Returns `false` if not.

  * **title**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The page number associated with the part.

  * **url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The URL of the part.

    It consists of the current page URL path with the pagination parameter for the current part appended.

##### Example

```json
{
  "is_link": true,
  "title": "2",
  "url": "/collections/all?page=2"
}
```

### Create pagination navigation with `part`

You can create a pagination navigation by iterating over each `part` of a [`paginate` object](https://shopify.dev/docs/api/liquid/objects/paginate).

##### Code

```liquid
{% paginate collection.products by 5 -%}
  {% for part in paginate.parts -%}
    {% if part.is_link -%}
      {{ part.title | link_to: part.url}}
    {%- else -%}
      <span>{{ part.title }}</span>
    {% endif %}
  {%- endfor %}
{%- endpaginate %}
```

##### Data

```json
{
  "collection": {
    "products_count": 19
  }
}
```

##### Output

```html
<span>1</span>
    
<a href="/services/liquid_rendering/resource?page=2" title="">2</a>

<a href="/services/liquid_rendering/resource?page=3" title="">3</a>

<a href="/services/liquid_rendering/resource?page=4" title="">4</a>
```
