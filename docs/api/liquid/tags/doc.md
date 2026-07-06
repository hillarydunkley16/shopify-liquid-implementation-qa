---
title: 'Liquid tags: doc'
description: Documents template elements with annotations.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/doc'
  md: 'https://shopify.dev/docs/api/liquid/tags/doc.md'
api_name: liquid
---

# doc

Documents template elements with annotations.

The `doc` tag allows developers to include documentation within Liquid templates. Any content inside `doc` tags is not rendered or outputted. Liquid code inside will be parsed but not executed. This facilitates tooling support for features like code completion, linting, and inline documentation.

For detailed documentation syntax and examples, see the [`LiquidDoc` reference](https://shopify.dev/docs/storefronts/themes/tools/liquid-doc).

## Syntax

```oobleckTag
{% doc %}
  Renders a message.


  @param {string} foo - A string value.
  @param {string} [bar] - An optional string value.


  @example
  {% render 'message', foo: 'Hello', bar: 'World' %}
{% enddoc %}
```
