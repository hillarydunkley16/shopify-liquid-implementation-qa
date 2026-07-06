---
title: 'Liquid tags: unless'
description: Renders an expression unless a specific condition is `true`.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/unless'
  md: 'https://shopify.dev/docs/api/liquid/tags/unless.md'
api_name: liquid
---

# unless

Renders an expression unless a specific condition is `true`.

***

**Tip:** Similar to the \<a href="/docs/api/liquid/tags/if">\<code>if\</code> tag\</a>, you can use \<code>elsif\</code> to add more conditions to an \<code>unless\</code> tag.

***

## Syntax

```oobleckTag
{% unless condition %}
  expression
{% endunless %}
```

### condition

The condition to evaluate.

### expression

The expression to render unless the condition is met.

##### Code

```liquid
{% unless product.has_only_default_variant %}
  // Variant selection functionality
{% endunless %}
```

##### Data

```json
{
  "product": {
    "has_only_default_variant": false
  }
}
```

##### Output

```html
// Variant selection functionality
```
