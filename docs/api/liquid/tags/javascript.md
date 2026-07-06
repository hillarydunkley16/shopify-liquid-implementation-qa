---
title: 'Liquid tags: javascript'
description: >-
  JavaScript code included in
  [section](/storefronts/themes/architecture/sections),
  [block](/storefronts/themes/architecture/blocks) and
  [snippet](/storefronts/themes/architecture/snippets) files.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/javascript'
  md: 'https://shopify.dev/docs/api/liquid/tags/javascript.md'
api_name: liquid
---

# javascript

JavaScript code included in [section](https://shopify.dev/storefronts/themes/architecture/sections), [block](https://shopify.dev/storefronts/themes/architecture/blocks) and [snippet](https://shopify.dev/storefronts/themes/architecture/snippets) files.

Each section, block or snippet can have only one `{% javascript %}` tag.

To learn more about how JavaScript that's defined between the `javascript` tags is loaded and run, refer to the documentation for [javascript tags](https://shopify.dev/storefronts/themes/best-practices/javascript-and-stylesheet-tags#javascript).

***

**Caution:** Liquid isn\&#39;t rendered inside of \<code>{% javascript %}\</code> tags. Including Liquid code can cause syntax errors.

***

## Syntax

```oobleckTag
{% javascript %}
  javascript_code
{% endjavascript %}
```

### javascript\_code

The JavaScript code for the section, block or snippet.
