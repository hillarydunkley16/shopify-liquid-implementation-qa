---
title: 'Liquid tags: include'
description: 'Renders a [snippet](/themes/architecture/snippets).'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/include'
  md: 'https://shopify.dev/docs/api/liquid/tags/include.md'
api_name: liquid
---

# include

Renders a [snippet](https://shopify.dev/themes/architecture/snippets).

Inside the snippet, you can access and alter variables that are [created](https://shopify.dev/docs/api/liquid/tags/variable-tags) outside of the snippet.

**Deprecated:**

Deprecated because the way that variables are handled reduces performance and makes code harder to both read and maintain.

The `include` tag has been replaced by [`render`](https://shopify.dev/docs/api/liquid/tags/render).

## Syntax

```oobleckTag
{% include 'filename' %}
```

### filename

The name of the snippet to render, without the `.liquid` extension.
