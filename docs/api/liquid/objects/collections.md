---
title: 'Liquid objects: collections'
description: 'All of the [collections](/docs/api/liquid/objects/collection) on a store.'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/collections'
  md: 'https://shopify.dev/docs/api/liquid/objects/collections.md'
api_name: liquid
---

# collections

All of the [collections](https://shopify.dev/docs/api/liquid/objects/collection) on a store.

### Directly accessible in

* Global

### Iterate over the collections

You can iterate over `collections` to build a collection list.

##### Code

```liquid
{% for collection in collections %}
  {{- collection.title | link_to: collection.url }}
{% endfor %}
```

##### Output

```html
<a href="/collections/empty" title="">Empty</a>

<a href="/collections/featured-potions" title="">Featured potions</a>

<a href="/collections/freebies" title="">Freebies</a>

<a href="/collections/frontpage" title="">Home page</a>

<a href="/collections/ingredients" title="">Ingredients</a>

<a href="/collections/potions" title="">Potions</a>

<a href="/collections/sale-potions" title="">Sale potions</a>
```

### Access a specific collection

You can use `collections` to access a collection by its [handle](https://shopify.dev/docs/api/liquid/basics#handles).

##### Code

```liquid
{% for product in collections['sale-potions'].products %}
  {{- product.title | link_to: product.url }}
{% endfor %}
```

##### Output

```html
<a href="/products/draught-of-immortality" title="">Draught of Immortality</a>

<a href="/products/glacier-ice" title="">Glacier ice</a>

<a href="/products/health-potion" title="">Health potion</a>

<a href="/products/invisibility-potion" title="">Invisibility potion</a>
```
