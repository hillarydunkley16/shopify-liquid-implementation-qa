---
title: 'Liquid tags: sections'
description: 'Renders a [section group](/themes/architecture/section-groups).'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/sections'
  md: 'https://shopify.dev/docs/api/liquid/tags/sections.md'
api_name: liquid
---

# sections

Renders a [section group](https://shopify.dev/themes/architecture/section-groups).

Use this tag to render section groups as part of the theme's [layout](https://shopify.dev/themes/architecture/layouts) content. Place the `sections` tag where you want to render it in the layout.

To learn more about section groups and how to use them in your theme, refer to [Section groups](https://shopify.dev/themes/architecture/section-groups#usage).

## Syntax

```oobleckTag
{% sections 'name' %}
```

### name

The name of the section group file you want to render.
