---
title: 'Liquid filters: size'
description: Returns the size of a string or array.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/size'
  md: 'https://shopify.dev/docs/api/liquid/filters/size.md'
api_name: liquid
---

# size

```oobleck
variable | size
```

returns [number](https://shopify.dev/docs/api/liquid/basics#number)

Returns the size of a string or array.

The size of a string is the number of characters that the string includes. The size of an array is the number of items in the array.

##### Code

```liquid
{{ collection.title | size }}
{{ collection.products | size }}
```

##### Data

```json
{
  "collection": {
    "products": [],
    "title": "Sale potions"
  }
}
```

##### Output

```html
12
4
```

### Dot notation

You can use the `size` filter with dot notation when you need to use it inside a tag or object output.

##### Code

```liquid
{% if collection.products.size >= 10 %}
  There are 10 or more products in this collection.
{% else %}
  There are less than 10 products in this collection.
{% endif %}
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
There are less than 10 products in this collection.
```
