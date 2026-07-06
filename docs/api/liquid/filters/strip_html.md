---
title: 'Liquid filters: strip_html'
description: Strips all HTML tags from a string.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/strip_html'
  md: 'https://shopify.dev/docs/api/liquid/filters/strip_html.md'
api_name: liquid
---

# strip\_​html

```oobleck
string | strip_html
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Strips all HTML tags from a string.

##### Code

```liquid
<!-- With HTML -->
{{ product.description }}

<!-- HTML stripped -->
{{ product.description | strip_html }}
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
<!-- With HTML -->
<h3>Are you low on health? Well we've got the potion just for you!</h3>
<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>

<!-- HTML stripped -->
Are you low on health? Well we've got the potion just for you!
Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!
```
