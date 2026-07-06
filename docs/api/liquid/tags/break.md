---
title: 'Liquid tags: break'
description: 'Stops a [`for` loop](/docs/api/liquid/tags/for) from iterating.'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/break'
  md: 'https://shopify.dev/docs/api/liquid/tags/break.md'
api_name: liquid
---

# break

Stops a [`for` loop](https://shopify.dev/docs/api/liquid/tags/for) from iterating.

## Syntax

```oobleckTag
{% break %}
```

##### Code

```liquid
{% for i in (1..5) -%}
  {%- if i == 4 -%}
    {% break %}
  {%- else -%}
    {{ i }}
  {%- endif -%}
{%- endfor %}
```

##### Output

```html
1
2
3
```
