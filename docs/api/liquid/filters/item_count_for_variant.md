---
title: 'Liquid filters: item_count_for_variant'
description: >-
  Returns the total item count for a specified variant in the
  [`cart`](https://shopify.dev/docs/api/liquid/objects/cart) object.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/item_count_for_variant'
  md: 'https://shopify.dev/docs/api/liquid/filters/item_count_for_variant.md'
api_name: liquid
---

# item\_​count\_​for\_​variant

```oobleck
cart | item_count_for_variant: {variant_id}
```

returns [number](https://shopify.dev/docs/api/liquid/basics#number)

Returns the total item count for a specified variant in the [`cart`](https://shopify.dev/docs/api/liquid/objects/cart) object.

##### Code

```liquid
{{ cart | item_count_for_variant: 39888235757633 }}
```

##### Output

```html
1
```
