---
title: 'Liquid objects: pages'
description: 'All of the [pages](/docs/api/liquid/objects/page) on a store.'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/pages'
  md: 'https://shopify.dev/docs/api/liquid/objects/pages.md'
api_name: liquid
---

# pages

All of the [pages](https://shopify.dev/docs/api/liquid/objects/page) on a store.

### Directly accessible in

* Global

You can access a specific page through the `pages` object using the page's [handle](https://shopify.dev/docs/api/liquid/basics#handles).

##### Code

```liquid
{{ pages.contact.title }}
{{ pages['about-us'].title }}
```

##### Output

```html
Contact
About us
```

### Paginate the `pages` object

You can [paginate](https://shopify.dev/docs/api/liquid/tags/paginate) the `pages` object, allowing you to iterate over up to 50 pages at a time.

##### Code

```liquid
{% paginate pages by 2 -%}
  {% for page in pages -%}
    {{ page.title | link_to: page.url }}
  {%- endfor %}

  {{- paginate | default_pagination }}
{%- endpaginate %}
```

##### Output

```html
<a href="/pages/about-us" title="">About us</a>
<a href="/pages/contact" title="">Contact</a>

<span class="page current">1</span> <span class="page"><a href="/services/liquid_rendering/resource?page=2" title="">2</a></span> <span class="next"><a href="/services/liquid_rendering/resource?page=2" title="">Next &raquo;</a></span>
```
