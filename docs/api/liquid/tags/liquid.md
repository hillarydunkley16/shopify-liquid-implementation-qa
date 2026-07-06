---
title: 'Liquid tags: liquid'
description: Allows you to have a block of Liquid without delimeters on each tag.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/liquid'
  md: 'https://shopify.dev/docs/api/liquid/tags/liquid.md'
api_name: liquid
---

# liquid

Allows you to have a block of Liquid without delimeters on each tag.

Because the tags don't have delimeters, each tag needs to be on its own line.

***

**Tip:** Use the \<a href="/docs/api/liquid/tags/echo">\<code>echo\</code> tag\</a> to output an expression inside \<code>liquid\</code> tags.

***

## Syntax

```oobleckTag
{% liquid
  expression
%}
```

### expression

The expression to be rendered inside the `liquid` tag.

##### Code

```liquid
{% liquid
  # Show a message that's customized to the product type

  assign product_type = product.type | downcase
  assign message = ''

  case product_type
    when 'health'
      assign message = 'This is a health potion!'
    when 'love'
      assign message = 'This is a love potion!'
    else
      assign message = 'This is a potion!'
  endcase

  echo message
%}
```

##### Data

```json
{
  "product": {
    "type": null
  }
}
```

##### Output

```html
This is a health potion!
```
