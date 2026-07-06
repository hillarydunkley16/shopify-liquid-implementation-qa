---
title: 'Liquid objects: linklists'
description: >-
  All of the
  [menus](https://help.shopify.com/manual/online-store/menus-and-links/drop-down-menus)
  in a store.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/linklists'
  md: 'https://shopify.dev/docs/api/liquid/objects/linklists.md'
api_name: liquid
---

# linklists

All of the [menus](https://help.shopify.com/manual/online-store/menus-and-links/drop-down-menus) in a store.

### Directly accessible in

* Global

You can access a specific menu through the `linklists` object using the menu's [handle](https://shopify.dev/docs/api/liquid/basics#handles).

##### Code

```liquid
<!-- Main menu -->
{% for link in linklists.main-menu.links -%}
  {{ link.title | link_to: link.url }}
{%- endfor %}

<!-- Footer menu -->
{% for link in linklists['footer'].links -%}
  {{ link.title | link_to: link.url }}
{%- endfor %}
```

##### Data

```json
{
  "linklists": {
    "footer": {
      "links": [
        "LinkDrop"
      ]
    },
    "main-menu": {
      "links": [
        "LinkDrop",
        "LinkDrop",
        "LinkDrop"
      ]
    }
  }
}
```

##### Output

```html
<!-- Main menu -->
<a href="/" title="">Home</a>
<a href="/collections/all" title="">Catalog</a>
<a href="/pages/contact" title="">Contact</a>


<!-- Footer menu -->
<a href="/search" title="">Search</a>
```
