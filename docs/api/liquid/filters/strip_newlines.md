---
title: 'Liquid filters: strip_newlines'
description: Strips all newline characters (line breaks) from a string.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/strip_newlines'
  md: 'https://shopify.dev/docs/api/liquid/filters/strip_newlines.md'
api_name: liquid
---

# strip\_​newlines

```oobleck
string | strip_newlines
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Strips all newline characters (line breaks) from a string.

##### Code

```liquid
<!-- With newlines -->
{{ product.description }}

<!-- Newlines stripped -->
{{ product.description | strip_newlines }}
```

##### Data

```json
{
  "product": {
    "description": "<h3>Are you low on health? Well we've got the potion just for you!</h3>\n<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>"
  }
}
```

##### Output

```html
<!-- With newlines -->
<h3>Are you low on health? Well we've got the potion just for you!</h3>
<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>

<!-- Newlines stripped -->
<h3>Are you low on health? Well we've got the potion just for you!</h3><p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>
```
