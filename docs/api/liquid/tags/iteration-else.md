---
title: 'Liquid tags: else'
description: >-
  Allows you to specify a default expression to execute when a [`for`
  loop](/docs/api/liquid/tags/for) has zero length.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/iteration-else'
  md: 'https://shopify.dev/docs/api/liquid/tags/iteration-else.md'
api_name: liquid
---

# else

Allows you to specify a default expression to execute when a [`for` loop](https://shopify.dev/docs/api/liquid/tags/for) has zero length.

## Syntax

```oobleckTag
{% for variable in array %}
  first_expression
{% else %}
  second_expression
{% endfor %}
```

### variable

The current item in the array.

### array

The array to iterate over.

### first\_expression

The expression to render for each iteration.

### second\_expression

The expression to render if the loop has zero length.

##### Code

```liquid
{% for product in collection.products %}
  {{ product.title }}<br>
{% else %}
  There are no products in this collection.
{% endfor %}
```

##### Data

```json
{
  "collection": {
    "products": []
  }
}
```

##### Output

```html
There are no products in this collection.
```
