---
title: 'Liquid tags: echo'
description: Outputs an expression.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/echo'
  md: 'https://shopify.dev/docs/api/liquid/tags/echo.md'
api_name: liquid
---

# echo

Outputs an expression.

Using the `echo` tag is the same as wrapping an expression in curly brackets (`{{` and `}}`). However, unlike the curly bracket method, you can use the `echo` tag inside [`liquid` tags](https://shopify.dev/docs/api/liquid/tags/liquid).

***

**Tip:** You can use \<a href="/docs/api/liquid/filters">filters\</a> on expressions inside \<code>echo\</code> tags.

***

## Syntax

```oobleckTag
{% liquid
  echo expression
%}
```

### expression

The expression to be output.

##### Code

```liquid
{% echo product.title %}

{% liquid
  echo product.price | money
%}
```

##### Data

```json
{
  "product": {
    "price": "10.00",
    "title": "Health potion"
  }
}
```

##### Output

```html
Health potion

$10.00
```
