---
title: 'Liquid objects: content_for_additional_checkout_buttons'
description: >-
  Returns checkout buttons for any active payment providers with offsite
  checkouts.
source_url:
  html: >-
    https://shopify.dev/docs/api/liquid/objects/content_for_additional_checkout_buttons
  md: >-
    https://shopify.dev/docs/api/liquid/objects/content_for_additional_checkout_buttons.md
api_name: liquid
---

# content\_​for\_​additional\_​checkout\_​buttons

Returns checkout buttons for any active payment providers with offsite checkouts.

Use [`additional_checkout_buttons`](https://shopify.dev/docs/api/liquid/objects/additional_checkout_buttons) to check whether these payment providers exist, and `content_for_additional_checkout_buttons` to show the associated checkout buttons. To learn more about how to use these objects, refer to [Accelerated checkout](https://shopify.dev/themes/pricing-payments/accelerated-checkout).

```liquid
{% if additional_checkout_buttons %}
  {{ content_for_additional_checkout_buttons }}
{% endif %}
```

### Directly accessible in

* Global
