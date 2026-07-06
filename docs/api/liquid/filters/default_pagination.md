---
title: 'Liquid filters: default_pagination'
description: >-
  Generates HTML for a set of links for paginated results. Must be applied to
  the [`paginate` object](/docs/api/liquid/objects/paginate).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/default_pagination'
  md: 'https://shopify.dev/docs/api/liquid/filters/default_pagination.md'
api_name: liquid
---

# default\_​pagination

```oobleck
paginate | default_pagination
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates HTML for a set of links for paginated results. Must be applied to the [`paginate` object](https://shopify.dev/docs/api/liquid/objects/paginate).

##### Code

```liquid
{% paginate collection.products by 2 %}
  {% for product in collection.products %}
    {{- product.title }}
  {% endfor %}

  {{- paginate | default_pagination -}}
{% endpaginate %}
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
      }
    ],
    "products_count": 4
  }
}
```

##### Output

```html
Draught of Immortality
  
Glacier ice
  
<span class="page current">1</span> <span class="page"><a href="/services/liquid_rendering/resource?page=2" title="">2</a></span> <span class="next"><a href="/services/liquid_rendering/resource?page=2" title="">Next &raquo;</a></span>
```

### previous

```oobleck
paginate | default_pagination: previous: string
```

Specify the text for the previous page link.

##### Code

```liquid
{% paginate collection.products by 2 %}
  {% for product in collection.products %}
    {{- product.title }}
  {% endfor %}

  {{- paginate | default_pagination: previous: 'Previous' -}}
{% endpaginate %}
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
      }
    ],
    "products_count": 4
  }
}
```

##### Output

```html
Draught of Immortality
  
Glacier ice
  
<span class="page current">1</span> <span class="page"><a href="/services/liquid_rendering/resource?page=2" title="">2</a></span> <span class="next"><a href="/services/liquid_rendering/resource?page=2" title="">Next &raquo;</a></span>
```

### next

```oobleck
paginate | default_pagination: next: string
```

Specify the text for the next page link.

##### Code

```liquid
{% paginate collection.products by 2 %}
  {% for product in collection.products %}
    {{- product.title }}
  {% endfor %}

  {{- paginate | default_pagination: next: 'Next' -}}
{% endpaginate %}
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
      }
    ],
    "products_count": 4
  }
}
```

##### Output

```html
Draught of Immortality
  
Glacier ice
  
<span class="page current">1</span> <span class="page"><a href="/services/liquid_rendering/resource?page=2" title="">2</a></span> <span class="next"><a href="/services/liquid_rendering/resource?page=2" title="">Next</a></span>
```

### anchor

```oobleck
paginate | default_pagination: anchor: string
```

Specify the anchor to add to the pagination links.

##### Code

```liquid
{% paginate collection.products by 2 %}
  {% for product in collection.products %}
    {{- product.title }}
  {% endfor %}

  <div id="pagination">
    {{- paginate | default_pagination: anchor: 'pagination' -}}
  </div>
{% endpaginate %}
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
      }
    ],
    "products_count": 4
  }
}
```

##### Output

```html
Draught of Immortality
  
Glacier ice
  

  <div id="pagination"><span class="page current">1</span> <span class="page"><a href="/services/liquid_rendering/resource?page=2#pagination" title="">2</a></span> <span class="next"><a href="/services/liquid_rendering/resource?page=2#pagination" title="">Next &raquo;</a></span></div>
```
