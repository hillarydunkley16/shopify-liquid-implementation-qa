---
title: 'Liquid filters: newline_to_br'
description: Converts newlines (`\n`) in a string to HTML line breaks (`<br>`).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/newline_to_br'
  md: 'https://shopify.dev/docs/api/liquid/filters/newline_to_br.md'
api_name: liquid
---

# newline\_​to\_​br

```oobleck
string | newline_to_br
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Converts newlines (`\n`) in a string to HTML line breaks (`<br>`).

##### Code

```liquid
{{ product.description | newline_to_br }}
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
<h3>Are you low on health? Well we've got the potion just for you!</h3><br />
<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>
```
