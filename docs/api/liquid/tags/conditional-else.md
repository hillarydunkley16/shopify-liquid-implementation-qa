---
title: 'Liquid tags: else'
description: >-
  Allows you to specify a default expression to execute when no other condition
  is met.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/conditional-else'
  md: 'https://shopify.dev/docs/api/liquid/tags/conditional-else.md'
api_name: liquid
---

# else

Allows you to specify a default expression to execute when no other condition is met.

You can use the `else` tag with the following tags:

* [`case`](https://shopify.dev/docs/api/liquid/tags/case)
* [`if`](https://shopify.dev/docs/api/liquid/tags/if)
* [`unless`](https://shopify.dev/docs/api/liquid/tags/unless)

## Syntax

```oobleckTag
{% else %}
  expression
```

### expression

The expression to render if no other condition is met.

##### Code

```liquid
{% if product.available %}
  This product is available!
{% else %}
  This product is sold out!
{% endif %}
```

##### Data

```json
{
  "product": {
    "available": true
  }
}
```

##### Output

```html
This product is available!
```
