---
title: 'Liquid objects: content_for_header'
description: Dynamically returns all scripts required by Shopify.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/content_for_header'
  md: 'https://shopify.dev/docs/api/liquid/objects/content_for_header.md'
api_name: liquid
---

# content\_​for\_​header

Dynamically returns all scripts required by Shopify.

Include the `content_for_header` object in your [layout files](https://shopify.dev/themes/architecture/layouts) between the `<head>` and `</head>` HTML tags.

You shouldn't try to modify or parse the `content_for_header` object because the contents are subject to change, which can change the behaviour of your code.

***

**Note:** The \<code>\<span class="PreventFireFoxApplyingGapToWBR">content\<wbr/>\_for\<wbr/>\_header\</span>\</code> object is required in \<code>theme.liquid\</code>.

***

### Directly accessible in

* Global
