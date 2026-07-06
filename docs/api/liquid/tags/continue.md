---
title: 'Liquid tags: continue'
description: >-
  Causes a [`for` loop](/docs/api/liquid/tags/for) to skip to the next
  iteration.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/continue'
  md: 'https://shopify.dev/docs/api/liquid/tags/continue.md'
api_name: liquid
---

# continue

Causes a [`for` loop](https://shopify.dev/docs/api/liquid/tags/for) to skip to the next iteration.

## Syntax

```oobleckTag
{% continue %}
```

##### Code

```liquid
{% for i in (1..5) -%}
  {%- if i == 4 -%}
    {% continue %}
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
5
```
