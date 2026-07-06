---
title: 'Liquid filters: customer_login_link'
description: Generates an HTML link to the customer login page.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/customer_login_link'
  md: 'https://shopify.dev/docs/api/liquid/filters/customer_login_link.md'
api_name: liquid
---

# customer\_​login\_​link

```oobleck
string | customer_login_link
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates an HTML link to the customer login page.

##### Code

```liquid
{{ 'Log in' | customer_login_link }}
```

##### Output

```html
<a href="/account/login" id="customer_login_link">Log in</a>
```
