---
title: 'Liquid filters: customer_register_link'
description: Generates an HTML link to the customer registration page.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/customer_register_link'
  md: 'https://shopify.dev/docs/api/liquid/filters/customer_register_link.md'
api_name: liquid
---

# customer\_​register\_​link

```oobleck
string | customer_register_link
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates an HTML link to the customer registration page.

##### Code

```liquid
{{ 'Create an account' | customer_register_link }}
```

##### Output

```html
<a href="/account/register" id="customer_register_link">Create an account</a>
```
