---
title: 'Liquid filters: customer_logout_link'
description: >-
  Generates an HTML link to log the customer out of their account and redirect
  to the homepage.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/customer_logout_link'
  md: 'https://shopify.dev/docs/api/liquid/filters/customer_logout_link.md'
api_name: liquid
---

# customer\_​logout\_​link

```oobleck
string | customer_logout_link
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates an HTML link to log the customer out of their account and redirect to the homepage.

##### Code

```liquid
{{ 'Log out' | customer_logout_link }}
```

##### Output

```html
<a href="/account/logout" id="customer_logout_link">Log out</a>
```
