---
title: 'Liquid filters: avatar'
description: 'Generates HTML to render a customer''s avatar, if available.'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/avatar'
  md: 'https://shopify.dev/docs/api/liquid/filters/avatar.md'
api_name: liquid
---

# avatar

```oobleck
customer | avatar
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates HTML to render a customer's avatar, if available.

***

**Tip:** Use with the \<a href="/docs/api/liquid/objects/customer#customer-has\_avatar?">\<code>\<span class="PreventFireFoxApplyingGapToWBR">customer.has\<wbr/>\_avatar?\</span>\</code>\</a> method to determine if the customer has an avatar.

***

```liquid
{{ customer | avatar }}
```
