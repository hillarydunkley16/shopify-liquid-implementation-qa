---
title: 'Liquid filters: structured_data'
description: Converts an object into a schema.org structured data format.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/structured_data'
  md: 'https://shopify.dev/docs/api/liquid/filters/structured_data.md'
api_name: liquid
---

# structured\_​data

```oobleck
variable | structured_data
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Converts an object into a schema.org structured data format.

The `structured_data` filter can be used on the [`product`](https://shopify.dev/docs/api/liquid/objects/product) and [`article`](https://shopify.dev/docs/api/liquid/objects/article) objects.

Product objects are output as a [schema.org `Product`](https://schema.org/Product) if they have no variants, and a [`ProductGroup`](https://schema.org/ProductGroup) if they have one or more variants.

Article objects are output as a [schema.org `Article`.](https://schema.org/Article)

##### Code

```liquid
<script type="application/ld+json">
  {{ product | structured_data }}
</script>
```

##### Output

```html
<script type="application/ld+json">
  {"@context":"http:\/\/schema.org\/","@id":"\/products\/crocodile-tears#product","@type":"Product","brand":{"@type":"Brand","name":"Polina's Potent Potions"},"category":"","description":"","image":"https:\/\/polinas-potent-potions.myshopify.com\/cdn\/shop\/products\/amber-beard-oil-bottle.jpg?v=1650642958\u0026width=1920","name":"Crocodile tears","offers":{"@id":"\/products\/crocodile-tears?variant=39888242344001#offer","@type":"Offer","availability":"http:\/\/schema.org\/OutOfStock","price":"56.00","priceCurrency":"CAD","url":"https:\/\/polinas-potent-potions.myshopify.com\/products\/crocodile-tears?variant=39888242344001"},"url":"https:\/\/polinas-potent-potions.myshopify.com\/products\/crocodile-tears"}
</script>
```
