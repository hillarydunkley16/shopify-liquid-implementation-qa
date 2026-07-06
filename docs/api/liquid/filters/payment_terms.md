---
title: 'Liquid filters: payment_terms'
description: >-
  Generates the HTML for the [Shop Pay Installments
  banner](/themes/pricing-payments/installments).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/payment_terms'
  md: 'https://shopify.dev/docs/api/liquid/filters/payment_terms.md'
api_name: liquid
---

# payment\_​terms

```oobleck
form | payment_terms
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates the HTML for the [Shop Pay Installments banner](https://shopify.dev/themes/pricing-payments/installments).

The `payment_terms` filter must be used on the `form` object within a [product form](https://shopify.dev/docs/api/liquid/tags/form#form-product) or [cart form](https://shopify.dev/docs/api/liquid/tags/form#form-cart).

```liquid
{% form 'product', product %}
  {{ form | payment_terms }}
{% endform %}
```

```liquid
{% form 'cart', cart %}
  {{ form | payment_terms }}
{% endform %}
```
