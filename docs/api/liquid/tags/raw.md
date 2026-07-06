---
title: 'Liquid tags: raw'
description: Outputs any Liquid code as text instead of rendering it.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/raw'
  md: 'https://shopify.dev/docs/api/liquid/tags/raw.md'
api_name: liquid
---

# raw

Outputs any Liquid code as text instead of rendering it.

## Syntax

```oobleckTag
{% raw %}
  expression
{% endraw %}
```

### expression

The expression to be output without being rendered.

##### Code

```liquid
{% raw %}
{{ 2 | plus: 2 }} equals 4.
{% endraw %}
```

##### Output

```html
{{ 2 | plus: 2 }} equals 4.
```
