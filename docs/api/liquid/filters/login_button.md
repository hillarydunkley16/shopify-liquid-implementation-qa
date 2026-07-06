---
title: 'Liquid filters: login_button'
description: >-
  Generates an HTML Button that enables a customer to either sign in to the
  storefront using their Shop account or follow the shop in the Shop App.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/login_button'
  md: 'https://shopify.dev/docs/api/liquid/filters/login_button.md'
api_name: liquid
---

# login\_​button

```oobleck
shop | login_button
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates an HTML Button that enables a customer to either sign in to the storefront using their Shop account or follow the shop in the Shop App.

***

**Note:** The presence of the \<a href="/docs/api/liquid/objects/shop">shop\</a> object is required for validation purposes only.

***

### action

```oobleck
shop | login_button: action: string
```

Controls the behavior of the button after authentication.

Accepts the following values:

* `default` - Authentication only
* `follow` - Performs a side-effect after authentication which follows the current shop in the Shop app. Requires additional configuration. [Learn more](https://help.shopify.com/manual/online-store/themes/customizing-themes/follow-on-shop)

```liquid
{{ shop | login_button: action: 'follow' }}
```
