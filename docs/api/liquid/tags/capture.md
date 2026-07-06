---
title: 'Liquid tags: capture'
description: Creates a new variable with a string value.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/capture'
  md: 'https://shopify.dev/docs/api/liquid/tags/capture.md'
api_name: liquid
---

# capture

Creates a new variable with a string value.

You can create complex strings with Liquid logic and variables.

***

**Caution:** Predefined Liquid objects can be overridden by variables with the same name. To make sure that you can access all Liquid objects, make sure that your variable name doesn\&#39;t match a predefined object\&#39;s name.

***

## Syntax

```oobleckTag
{% capture variable %}
  value
{% endcapture %}
```

### variable

The name of the variable being created.

### value

The value you want to assign to the variable.

##### Code

```liquid
{%- assign up_title = product.title | upcase -%}
{%- assign down_title = product.title | downcase -%}
{%- assign show_up_title = true -%}

{%- capture title -%}
  {% if show_up_title -%}
    Upcase title: {{ up_title }}
  {%- else -%}
    Downcase title: {{ down_title }}
  {%- endif %}
{%- endcapture %}

{{ title }}
```

##### Data

```json
{
  "product": {
    "title": "Health potion"
  }
}
```

##### Output

```html
Upcase title: HEALTH POTION
```
